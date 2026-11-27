"""Data loading and verification module for Raman spectroscopy datasets."""

from pathlib import Path
import hashlib
import json
import numpy as np
import pandas as pd


def compute_sha256(filepath: Path) -> str:
    """Compute SHA-256 digest of a file to guarantee data provenance."""
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def load_spectrum_csv(filepath: Path) -> pd.DataFrame:
    """Load a two-column Raman spectrum CSV file with integrity validation."""
    filepath = Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(f"Spectrum file not found: {filepath}")

    df = pd.read_csv(filepath)
    if "wavenumber_cm1" not in df.columns or "intensity_counts" not in df.columns:
        if len(df.columns) >= 2:
            df.columns = ["wavenumber_cm1", "intensity_counts"] + list(df.columns[2:])
        else:
            raise ValueError(f"Invalid columns in {filepath}: {df.columns.tolist()}")

    df = df.dropna(subset=["wavenumber_cm1", "intensity_counts"])
    df["wavenumber_cm1"] = pd.to_numeric(df["wavenumber_cm1"], errors="coerce")
    df["intensity_counts"] = pd.to_numeric(df["intensity_counts"], errors="coerce")
    df = df.dropna().sort_values(by="wavenumber_cm1").reset_index(drop=True)

    diffs = np.diff(df["wavenumber_cm1"].values)
    if not np.all(diffs > 0):
        raise ValueError(f"Wavenumber axis in {filepath} is not strictly monotonic.")

    return df


def load_all_datasets(data_dir: Path) -> dict:
    """Load all raw spectral datasets found in data_dir into a structured dictionary."""
    data_dir = Path(data_dir)
    spectra = {}
    for csv_file in sorted(data_dir.glob("*.csv")):
        spec_id = csv_file.stem
        df = load_spectrum_csv(csv_file)
        sha256 = compute_sha256(csv_file)
        spectra[spec_id] = {
            "file_name": csv_file.name,
            "path": csv_file,
            "sha256": sha256,
            "data": df,
            "wavenumber": df["wavenumber_cm1"].values,
            "intensity": df["intensity_counts"].values,
            "n_points": len(df),
            "wn_range": (float(df["wavenumber_cm1"].iloc[0]), float(df["wavenumber_cm1"].iloc[-1])),
        }
    return spectra


def load_metadata(metadata_path: Path) -> list:
    """Load dataset metadata JSON records."""
    metadata_path = Path(metadata_path)
    if not metadata_path.exists():
        raise FileNotFoundError(f"Metadata file not found: {metadata_path}")
    with open(metadata_path, "r", encoding="utf-8") as f:
        return json.load(f)
