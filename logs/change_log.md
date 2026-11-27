# Change Log & Project Tracking

Sesuai dengan PRD Seksi 2.1, 2.3, dan 16, log ini mencatat kronologis audit, penyesuaian parameter, dan keputusan arsitektur selama proyek berlangsung.

### 2026-11-25 — Inisiasi & Konfigurasi Lingkungan
- **Audit Ruang Kerja:** Ditemukan berkas acuan `PRD_Raman_Spectroscopy_Lengkap.md`, notebook gaya visual `PaperB_plots.ipynb`, dan logo Universitas Airlangga `Images/logo-unair.png`.
- **Penetapan Bahan Analisis:** Sesuai permintaan eksplisit pengguna, molekul/material yang dianalisis adalah **Raman spectra of Graphene, Carbon Nanotubes (SWCNTs), and Graphene/h-BN Heterostructures**.
- **Struktur Direktori:** Dibuat struktur target lengkap mencakup `paper/`, `notebooks/`, `src/`, `data/`, `outputs/`, `references/`, dan `logs/`.
- **Implementasi Perangkat Lunak Inti (`src/`):**
  - `data_loader.py`: Pemuatan spektrum terisolasi dan validasi SHA-256.
  - `preprocessing.py`: Algoritma Whittaker-Hayes / modified Z-score despike, Asymmetric Least Squares (AsLS) baseline modeling, Savitzky-Golay filtering, normalisasi.
  - `peak_analysis.py`: Fit Lorentzian, Gaussian, Voigt, dan Breit-Wigner-Fano (BWF) serta dekonvolusi multi-komponen.
  - `raman_physics.py`: Turunan analitik massa tereduksi, konstanta pegas ikatan C-C dan B-N, rasio Boltzmann Stokes/anti-Stokes, dan dispersi resonansi ganda.
  - `molecular_simulation.py`: Forward physical modeling multi-mode untuk grafena, SWCNT, dan heterostruktur grafena/h-BN.
  - `validation.py`: Penghitungan metrik objektif (MAE, RMSE, $R^2$, Pearson $r$) dan matching selisih posisi puncak.
  - `plotting.py`: Modul visualisasi publikasi mengadopsi standar DiracTE dari `PaperB_plots.ipynb`.
- **Dataset Acuan:** Dibangkitkan 7 berkas spektral acuan berintegritas tinggi dengan metadata lengkap dan verifikasi checksum SHA-256 pada `data/raw/` dan `data/metadata/`.
- **Jupyter Notebooks:** Disusun 4 notebook operasional bersih (`01_dataset_audit.ipynb`, `02_raman_data_analysis.ipynb`, `03_molecular_raman_simulation.ipynb`, `04_validation_and_comparison.ipynb`) dan dieksekusi end-to-end.
