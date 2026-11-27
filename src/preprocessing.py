"""Signal preprocessing module for Raman spectroscopy: despiking, baseline, smoothing, normalization."""

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve
from scipy.signal import savgol_filter


def despike_modified_zscore(intensity: np.ndarray, threshold: float = 6.0) -> np.ndarray:
    """Remove cosmic ray spikes using modified Z-score on intensity first differences.
    
    Spikes appear as sharp single-point or two-point discontinuities with extreme
    first-difference gradients exceeding typical Raman phonon peak slopes.
    """
    y = intensity.copy()
    diff = np.diff(y)
    median_diff = np.median(diff)
    mad = np.median(np.abs(diff - median_diff))
    if mad == 0:
        return y

    modified_z_scores = 0.6745 * np.abs(diff - median_diff) / mad
    spike_indices = np.where(modified_z_scores > threshold)[0]

    for idx in spike_indices:
        left = max(0, idx - 2)
        right = min(len(y) - 1, idx + 3)
        window = [j for j in range(left, right + 1) if j not in spike_indices and j != idx]
        if window:
            y[idx] = np.mean(y[window])
            if idx + 1 < len(y):
                y[idx + 1] = np.mean(y[window])
    return y


def baseline_asls(intensity: np.ndarray, lam: float = 1e5, p: float = 0.005, n_iter: int = 15) -> np.ndarray:
    """Asymmetric Least Squares (AsLS) baseline estimation (Eilers & Boelens 2005).
    
    Minimizes: sum_i w_i (y_i - z_i)^2 + lam * sum_i (Delta^2 z_i)^2
    with asymmetric weights w_i = p if y_i > z_i else (1 - p).
    """
    y = intensity.copy()
    L = len(y)
    D = sparse.diags([1, -2, 1], [0, 1, 2], shape=(L - 2, L), format="csc")
    H = lam * (D.T @ D)
    w = np.ones(L)

    for _ in range(n_iter):
        W = sparse.diags(w, 0, shape=(L, L), format="csc")
        Z = W + H
        z = spsolve(Z, w * y)
        w = p * (y > z) + (1.0 - p) * (y <= z)

    return z


def denoise_savgol(intensity: np.ndarray, window_length: int = 11, polyorder: int = 3) -> np.ndarray:
    """Savitzky-Golay polynomial smoothing without peak attenuation."""
    if window_length % 2 == 0:
        window_length += 1
    if window_length <= polyorder:
        window_length = polyorder + 2 if (polyorder + 2) % 2 != 0 else polyorder + 3
    return savgol_filter(intensity, window_length=window_length, polyorder=polyorder)


def normalize_spectrum(intensity: np.ndarray, method: str = "vector", reference_idx: int = None) -> np.ndarray:
    """Normalize spectral intensity using vector (L2), min-max, area, or peak reference."""
    y = intensity.copy()
    if method == "vector":
        norm = np.linalg.norm(y)
        return y / norm if norm > 0 else y
    elif method == "minmax":
        y_min, y_max = np.min(y), np.max(y)
        return (y - y_min) / (y_max - y_min) if y_max > y_min else y
    elif method == "area":
        area = np.trapz(np.maximum(0, y))
        return y / area if area > 0 else y
    elif method == "reference":
        if reference_idx is None:
            reference_idx = np.argmax(y)
        ref_val = y[reference_idx]
        return y / ref_val if ref_val > 0 else y
    else:
        raise ValueError(f"Unknown normalization method: {method}")


class RamanPipeline:
    """Standardized preprocessing pipeline for reproducible Raman analysis."""

    def __init__(self, despike: bool = True, despike_threshold: float = 6.0,
                 baseline: bool = True, lam: float = 1e5, p: float = 0.005,
                 smooth: bool = True, sg_window: int = 11, sg_order: int = 3,
                 normalize: str = "vector"):
        self.despike = despike
        self.despike_threshold = despike_threshold
        self.baseline = baseline
        self.lam = lam
        self.p = p
        self.smooth = smooth
        self.sg_window = sg_window
        self.sg_order = sg_order
        self.normalize = normalize

    def transform(self, wavenumber: np.ndarray, intensity: np.ndarray) -> dict:
        """Execute full preprocessing pipeline and return each stage for audit."""
        raw = intensity.copy()
        current = raw.copy()

        despiked = despike_modified_zscore(current, self.despike_threshold) if self.despike else current
        current = despiked.copy()

        if self.baseline:
            base = baseline_asls(current, lam=self.lam, p=self.p)
            corrected = np.maximum(0, current - base)
        else:
            base = np.zeros_like(current)
            corrected = current.copy()
        current = corrected.copy()

        smoothed = denoise_savgol(current, window_length=self.sg_window, polyorder=self.sg_order) if self.smooth else current
        current = smoothed.copy()

        normed = normalize_spectrum(current, method=self.normalize) if self.normalize else current

        return {
            "wavenumber": wavenumber,
            "raw": raw,
            "despiked": despiked,
            "baseline": base,
            "corrected": corrected,
            "smoothed": smoothed,
            "normalized": normed,
        }
