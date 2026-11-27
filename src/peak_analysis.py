"""Peak detection, line shape fitting (Lorentzian, Gaussian, Voigt, BWF), and spectral feature extraction."""

import numpy as np
from scipy.signal import find_peaks, peak_widths
from scipy.optimize import curve_fit


def lorentzian(x: np.ndarray, x0: float, gamma: float, A: float) -> np.ndarray:
    """Lorentzian profile with amplitude A, center x0, half-width gamma (FWHM = 2*gamma)."""
    return A * (gamma**2) / ((x - x0)**2 + gamma**2)


def gaussian(x: np.ndarray, x0: float, sigma: float, A: float) -> np.ndarray:
    """Gaussian profile with amplitude A, center x0, standard deviation sigma."""
    return A * np.exp(-((x - x0)**2) / (2.0 * sigma**2))


def pseudo_voigt(x: np.ndarray, x0: float, fwhm: float, A: float, eta: float) -> np.ndarray:
    """Pseudo-Voigt linear combination of Lorentzian (eta) and Gaussian (1 - eta)."""
    gamma = fwhm / 2.0
    sigma = fwhm / (2.0 * np.sqrt(2.0 * np.log(2.0)))
    L = (gamma**2) / ((x - x0)**2 + gamma**2)
    G = np.exp(-((x - x0)**2) / (2.0 * sigma**2))
    return A * (eta * L + (1.0 - eta) * G)


def bwf(x: np.ndarray, x0: float, gamma: float, A: float, q: float) -> np.ndarray:
    """Breit-Wigner-Fano (BWF) profile for metallic CNT G- band.
    
    Characterized by asymmetry parameter 1/q due to continuum plasmon coupling.
    """
    eps = (x - x0) / gamma
    return A * ((1.0 + eps / q)**2) / (1.0 + eps**2)


def multi_lorentzian(x: np.ndarray, *params) -> np.ndarray:
    """Sum of N Lorentzians. params: (x0_1, gamma_1, A_1, x0_2, gamma_2, A_2, ...)."""
    n_peaks = len(params) // 3
    total = np.zeros_like(x)
    for i in range(n_peaks):
        x0 = params[3 * i]
        gamma = params[3 * i + 1]
        A = params[3 * i + 2]
        total += lorentzian(x, x0, gamma, A)
    return total


def detect_peaks_auto(wavenumber: np.ndarray, intensity: np.ndarray,
                      prominence: float = 0.05, distance: int = 15,
                      width: int = 3) -> list:
    """Detect prominent Raman peaks and calculate empirical FWHM and intensity."""
    peaks, props = find_peaks(intensity, prominence=prominence, distance=distance, width=width)
    results = []
    if len(peaks) == 0:
        return results

    widths_res = peak_widths(intensity, peaks, rel_height=0.5)
    fwhm_pixels = widths_res[0]
    dw = np.median(np.diff(wavenumber))

    for idx, p in enumerate(peaks):
        results.append({
            "peak_index": int(p),
            "wavenumber_cm1": float(wavenumber[p]),
            "intensity": float(intensity[p]),
            "prominence": float(props["prominences"][idx]),
            "fwhm_cm1": float(fwhm_pixels[idx] * dw),
        })
    return results


def fit_single_peak(wavenumber: np.ndarray, intensity: np.ndarray,
                     center_guess: float, model: str = "lorentzian",
                     window_cm1: float = 60.0) -> dict:
    """Fit a single peak within a localized wavenumber window."""
    mask = np.abs(wavenumber - center_guess) <= window_cm1
    x_sub = wavenumber[mask]
    y_sub = intensity[mask]
    if len(x_sub) < 5:
        return {"success": False, "error": "Insufficient points in window"}

    peak_idx = np.argmax(y_sub)
    A_guess = y_sub[peak_idx]
    x0_guess = x_sub[peak_idx]
    gamma_guess = 10.0

    try:
        if model == "lorentzian":
            popt, pcov = curve_fit(lorentzian, x_sub, y_sub,
                                   p0=[x0_guess, gamma_guess, A_guess],
                                   bounds=([x0_guess - 25.0, 1.0, 0.0],
                                           [x0_guess + 25.0, 60.0, A_guess * 5.0]),
                                   maxfev=5000)
            x0, gamma, A = popt
            fwhm = 2.0 * gamma
            y_fit = lorentzian(x_sub, *popt)
        elif model == "gaussian":
            sigma_guess = gamma_guess / (2.0 * np.sqrt(2.0 * np.log(2.0)))
            popt, pcov = curve_fit(gaussian, x_sub, y_sub,
                                   p0=[x0_guess, sigma_guess, A_guess],
                                   bounds=([x0_guess - 25.0, 1.0, 0.0],
                                           [x0_guess + 25.0, 40.0, A_guess * 5.0]),
                                   maxfev=5000)
            x0, sigma, A = popt
            fwhm = 2.0 * np.sqrt(2.0 * np.log(2.0)) * sigma
            y_fit = gaussian(x_sub, *popt)
        else:
            raise ValueError(f"Unsupported single peak model: {model}")

        ss_res = np.sum((y_sub - y_fit)**2)
        ss_tot = np.sum((y_sub - np.mean(y_sub))**2)
        r2 = 1.0 - (ss_res / ss_tot) if ss_tot > 0 else 0.0

        return {
            "success": True,
            "center_cm1": float(x0),
            "fwhm_cm1": float(fwhm),
            "amplitude": float(A),
            "area": float(np.trapz(y_fit, x_sub)),
            "r2": float(r2),
            "popt": popt.tolist(),
            "x_sub": x_sub,
            "y_sub": y_sub,
            "y_fit": y_fit,
        }
    except Exception as e:
        return {"success": False, "error": str(e)}


def deconvolve_cnt_g_band(wavenumber: np.ndarray, intensity: np.ndarray,
                          is_metallic: bool = True) -> dict:
    """Deconvolve SWCNT G-band into G+ (axial) and G- (circumferential) modes.
    
    For metallic SWCNTs, G- uses Breit-Wigner-Fano (BWF) due to plasmon coupling.
    For semiconducting SWCNTs, both G+ and G- use standard Lorentzian profiles.
    """
    mask = (wavenumber >= 1480.0) & (wavenumber <= 1680.0)
    x = wavenumber[mask]
    y = intensity[mask]

    if is_metallic:
        def model_func(w, x0_m, gamma_m, A_m, q_m, x0_p, gamma_p, A_p):
            return bwf(w, x0_m, gamma_m, A_m, q_m) + lorentzian(w, x0_p, gamma_p, A_p)

        p0 = [1548.0, 18.0, np.max(y) * 0.45, -4.5, 1592.0, 8.0, np.max(y)]
        bounds = (
            [1520.0, 5.0, 0.0, -15.0, 1580.0, 3.0, 0.0],
            [1570.0, 45.0, np.max(y) * 2.0, -1.0, 1605.0, 20.0, np.max(y) * 3.0]
        )
    else:
        def model_func(w, x0_m, gamma_m, A_m, x0_p, gamma_p, A_p):
            return lorentzian(w, x0_m, gamma_m, A_m) + lorentzian(w, x0_p, gamma_p, A_p)

        p0 = [1568.0, 7.0, np.max(y) * 0.4, 1591.5, 6.0, np.max(y)]
        bounds = (
            [1550.0, 2.0, 0.0, 1580.0, 2.0, 0.0],
            [1580.0, 20.0, np.max(y) * 2.0, 1605.0, 18.0, np.max(y) * 3.0]
        )

    popt, _ = curve_fit(model_func, x, y, p0=p0, bounds=bounds, maxfev=10000)
    y_fit = model_func(x, *popt)
    r2 = 1.0 - np.sum((y - y_fit)**2) / np.sum((y - np.mean(y))**2)

    if is_metallic:
        gm_curve = bwf(x, popt[0], popt[1], popt[2], popt[3])
        gp_curve = lorentzian(x, popt[4], popt[5], popt[6])
        return {
            "is_metallic": True,
            "G_minus_center": float(popt[0]),
            "G_minus_fwhm": float(2.0 * popt[1]),
            "G_minus_amp": float(popt[2]),
            "bwf_q": float(popt[3]),
            "bwf_asymmetry_1_over_q": float(1.0 / popt[3]),
            "G_plus_center": float(popt[4]),
            "G_plus_fwhm": float(2.0 * popt[5]),
            "G_plus_amp": float(popt[6]),
            "r2": float(r2),
            "x": x, "y": y, "y_fit": y_fit,
            "G_minus_curve": gm_curve, "G_plus_curve": gp_curve
        }
    else:
        gm_curve = lorentzian(x, popt[0], popt[1], popt[2])
        gp_curve = lorentzian(x, popt[3], popt[4], popt[5])
        return {
            "is_metallic": False,
            "G_minus_center": float(popt[0]),
            "G_minus_fwhm": float(2.0 * popt[1]),
            "G_minus_amp": float(popt[2]),
            "G_plus_center": float(popt[3]),
            "G_plus_fwhm": float(2.0 * popt[4]),
            "G_plus_amp": float(popt[5]),
            "r2": float(r2),
            "x": x, "y": y, "y_fit": y_fit,
            "G_minus_curve": gm_curve, "G_plus_curve": gp_curve
        }


def deconvolve_bilayer_2d_band(wavenumber: np.ndarray, intensity: np.ndarray) -> dict:
    """Deconvolve Bilayer Graphene 2D band into 4 constituent Lorentzian components.
    
    Corresponds to transitions between 2 conduction and 2 valence subbands (Ferrari 2006).
    """
    mask = (wavenumber >= 2580.0) & (wavenumber <= 2800.0)
    x = wavenumber[mask]
    y = intensity[mask]

    p0 = [2652.0, 14.0, np.max(y) * 0.5,
          2680.0, 13.5, np.max(y) * 0.85,
          2700.0, 13.8, np.max(y) * 0.8,
          2724.0, 14.2, np.max(y) * 0.5]
    bounds = (
        [2630.0, 6.0, 0.0, 2665.0, 6.0, 0.0, 2688.0, 6.0, 0.0, 2710.0, 6.0, 0.0],
        [2665.0, 25.0, np.max(y) * 2.0, 2690.0, 25.0, np.max(y) * 2.0, 2712.0, 25.0, np.max(y) * 2.0, 2740.0, 25.0, np.max(y) * 2.0]
    )

    popt, _ = curve_fit(multi_lorentzian, x, y, p0=p0, bounds=bounds, maxfev=10000)
    y_fit = multi_lorentzian(x, *popt)
    r2 = 1.0 - np.sum((y - y_fit)**2) / np.sum((y - np.mean(y))**2)

    components = []
    labels = ["2D_11", "2D_12", "2D_21", "2D_22"]
    for i in range(4):
        x0 = popt[3 * i]
        gamma = popt[3 * i + 1]
        amp = popt[3 * i + 2]
        c_curve = lorentzian(x, x0, gamma, amp)
        components.append({
            "name": labels[i],
            "center_cm1": float(x0),
            "fwhm_cm1": float(2.0 * gamma),
            "amplitude": float(amp),
            "curve": c_curve
        })

    return {
        "r2": float(r2),
        "x": x,
        "y": y,
        "y_fit": y_fit,
        "components": components,
    }
