"""Quantitative model validation, peak position matching, and residual statistical analysis."""

import numpy as np
import pandas as pd


def compute_metrics(y_exp: np.ndarray, y_sim: np.ndarray) -> dict:
    """Compute MAE, RMSE, Pearson r, and coefficient of determination R^2."""
    diff = y_exp - y_sim
    mae = np.mean(np.abs(diff))
    rmse = np.sqrt(np.mean(diff**2))

    ss_res = np.sum(diff**2)
    ss_tot = np.sum((y_exp - np.mean(y_exp))**2)
    r2 = 1.0 - (ss_res / ss_tot) if ss_tot > 0 else 0.0

    std_exp = np.std(y_exp)
    std_sim = np.std(y_sim)
    if std_exp > 0 and std_sim > 0:
        pearson_r = np.corrcoef(y_exp, y_sim)[0, 1]
    else:
        pearson_r = 0.0

    return {
        "MAE": float(mae),
        "RMSE": float(rmse),
        "R2": float(r2),
        "Pearson_r": float(pearson_r),
    }


def match_peaks_and_residuals(peaks_exp: list, peaks_sim: list, tolerance_cm1: float = 20.0) -> pd.DataFrame:
    """Match experimental and simulated Raman peaks within a given wavenumber tolerance."""
    records = []
    matched_sim = set()

    for p_exp in peaks_exp:
        wn_exp = p_exp["wavenumber_cm1"]
        best_match = None
        min_diff = 1e9

        for j, p_sim in enumerate(peaks_sim):
            if j in matched_sim:
                continue
            wn_sim = p_sim.get("center", p_sim.get("wavenumber_cm1", 0.0))
            diff = np.abs(wn_sim - wn_exp)
            if diff <= tolerance_cm1 and diff < min_diff:
                min_diff = diff
                best_match = (j, p_sim, wn_sim)

        if best_match is not None:
            j_idx, p_sim_obj, wn_sim_val = best_match
            matched_sim.add(j_idx)
            records.append({
                "assignment": p_sim_obj.get("assignment", "Phonon mode"),
                "exp_wavenumber_cm1": wn_exp,
                "sim_wavenumber_cm1": wn_sim_val,
                "delta_wavenumber_cm1": wn_sim_val - wn_exp,
                "exp_intensity": p_exp.get("intensity", 0.0),
                "exp_fwhm_cm1": p_exp.get("fwhm_cm1", 0.0),
                "sim_fwhm_cm1": p_sim_obj.get("fwhm", 0.0),
            })
        else:
            records.append({
                "assignment": "Unassigned experimental peak",
                "exp_wavenumber_cm1": wn_exp,
                "sim_wavenumber_cm1": np.nan,
                "delta_wavenumber_cm1": np.nan,
                "exp_intensity": p_exp.get("intensity", 0.0),
                "exp_fwhm_cm1": p_exp.get("fwhm_cm1", 0.0),
                "sim_fwhm_cm1": np.nan,
            })

    return pd.DataFrame(records)
