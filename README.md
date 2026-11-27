# Proyek Makalah Ilmiah dan Simulasi Spektroskopi Raman

Proyek komputasi dan naskah akademik spektroskopi Raman pada nanomaterial karbon berdimensi rendah dan heterostruktur 2D: **Graphene, Single-Walled Carbon Nanotubes (SWCNTs), dan Heterostruktur Graphene/h-BN**.

**Tim Penulis:**
- Pradithya Putra Galang Islami (NIM: 182241014)
- Naufal Lutfian Hakim (NIM: 182241015)
- Hendra Maulana (NIM: 182241043)

**Dosen Pembimbing:** Drs. Adri Supardi, M.S.  
**Afiliasi:** Departemen Fisika, Fakultas Sains dan Teknologi, Universitas Airlangga  
**Mata Kuliah:** Spektroskopi (Semester Gasal 2026/2026)

---

## 1. Struktur Direktori Proyek

```text
Tugas Spektoroskopi/
├── README.md                           # Dokumentasi komprehensif proyek
├── PRD_Raman_Spectroscopy_Lengkap.md   # Product Requirement Document (PRD)
├── requirements.txt                    # Dependensi lingkungan Python
├── paper/                              # Berkas naskah akademik LaTeX
│   ├── main.tex                        # Berkas induk LaTeX
│   ├── references.bib                  # Bibliografi BibTeX terverifikasi DOI
│   ├── sections/                       # Naskah bab per bagian
│   │   ├── 01_pendahuluan.tex          # Latar belakang dan rumusan masalah
│   │   ├── 02_dasar_raman.tex          # Teori klasik & kuantum hamburan Raman
│   │   ├── 03_kaidah_seleksi.tex       # Kaidah seleksi & teori grup (CO2, H2O, 2D)
│   │   ├── 04_resonance_raman.tex      # Teori resonansi KHD & Franck-Condon
│   │   ├── 05_instrumentasi.tex        # Arsitektur spektrometer mikro-Raman
│   │   ├── 06_analisis_simulasi.tex    # Hasil eksperimen & validasi simulasi
│   │   └── 07_kesimpulan.tex          # Kesimpulan & keterbatasan
│   ├── figures/
│   │   ├── tikz/                       # Diagram vektor TikZ
│   │   ├── instrument/                 # Diagram skema instrumen
│   │   └── computational/              # Grafik komputasi beresolusi tinggi (PDF/PNG)
│   └── tables/                         # Tabel-tabel ringkasan
├── notebooks/                          # 4 Jupyter Notebooks terverifikasi
│   ├── 01_dataset_audit.ipynb          # Audit integritas kriptografis & metadata
│   ├── 02_raman_data_analysis.ipynb    # Preprocessing & dekonvolusi puncak
│   ├── 03_molecular_raman_simulation.ipynb # Simulasi fisika maju multi-mode
│   └── 04_validation_and_comparison.ipynb # Validasi kuantitatif MAE, RMSE, R^2
├── src/                                # Modul pustaka Python modular
│   ├── data_loader.py                  # Pemuatan data & SHA-256
│   ├── preprocessing.py                # Despike, baseline AsLS, Savitzky-Golay
│   ├── peak_analysis.py                # Fitting Lorentzian, Gaussian, BWF
│   ├── raman_physics.py                # Fisika massa tereduksi, pegas, Boltzmann
│   ├── molecular_simulation.py         # Forward physical model
│   ├── validation.py                   # Metrik validasi & matching residual
│   └── plotting.py                     # Standar visualisasi DiracTE (PaperB)
├── data/
│   ├── raw/                            # 7 berkas spektrum mentah eksperimental
│   ├── metadata/                       # Manifest & metadata terstruktur
│   ├── interim/                        # Data antara
│   └── processed/                      # Spektrum bersih hasil preprocessing
├── outputs/
│   ├── figures/                        # Grafik keluaran publikasi
│   ├── tables/                         # Tabel metrik & parameter CSV
│   ├── metrics/                        # Laporan JSON kualitas & validasi
│   └── simulation/                     # Spektrum hasil pemodelan maju
├── references/
│   ├── source_register.md              # Register audit literatur & kuartil Scopus
│   └── instrument_sources.md           # Rujukan teknis spektrometer Horiba
└── logs/
    ├── change_log.md                   # Log perubahan & keputusan metodologi
    └── validation_log.md               # Log pengujian jaminan kualitas (QA)
```

---

## 2. Cara Menjalankan Kode dan Notebook

1. **Aktivasi Lingkungan Python:**
   Pastikan Python 3.10+ terpasang beserta pustaka pada `requirements.txt`.
   ```powershell
   pip install -r requirements.txt
   ```

2. **Eksekusi Seluruh Notebook:**
   Jalankan skrip pembangun dan eksekusi notebook otomatis:
   ```powershell
   python build_all_notebooks.py
   ```
   Atau buka Jupyter Notebook secara interaktif:
   ```powershell
   jupyter notebook notebooks/
   ```

3. **Kompilasi Naskah LaTeX Menjadi PDF:**
   Masuk ke direktori `paper/` dan jalankan compiler `pdflatex`:
   ```powershell
   cd paper
   pdflatex -interaction=nonstopmode main.tex
   bibtex main
   pdflatex -interaction=nonstopmode main.tex
   pdflatex -interaction=nonstopmode main.tex
   ```
   Dokumen akhir `main.pdf` akan terbentuk secara utuh.

---

## 3. Ringkasan Temuan Utama

1. **Single-Layer Graphene (SLG):** Spektrum didominasi pita tajam $2D$ ($\sim 2685\text{ cm}^{-1}$, FWHM $\approx 26.2\text{ cm}^{-1}$) dengan rasio intensitas $I_{2D}/I_G = 2.75$, menandakan grafena monolayer pristine berkualitas tinggi.
2. **Bilayer Graphene (BLG):** Terpecahnya pita $2D$ menjadi 4 komponen Lorentzian subband elektronik ($2D_{11}, 2D_{12}, 2D_{21}, 2D_{22}$) dengan FWHM gabungan $\approx 54\text{ cm}^{-1}$ dan $I_{2D}/I_G \approx 1.03$, sesuai dengan kopling inter-layer Bernal AB.
3. **Defective Graphene:** Kemunculan pita defek inter-valley $D$ ($\sim 1348\text{ cm}^{-1}$) dan intra-valley $D'$ ($\sim 1621.5\text{ cm}^{-1}$) dengan $I_D/I_G = 0.90$, berkorespondensi dengan kerapatan defek kisi $n_D \approx 1.8 \times 10^{11}\text{ cm}^{-2}$.
4. **Metallic SWCNT:** Pita $G^-$ menunjukkan profil asimetris Breit-Wigner-Fano (BWF) dengan $1/q = -0.22$, membuktikan kopling fonon diskrit dengan eksitasi kontinu plasmonik elektron konduksi.
5. **Heterostruktur Graphene/h-BN:** Pemisahan tegas antara mode $E_{2g}$ substrat h-BN ($1366.8\text{ cm}^{-1}$) dengan ketiadaan defek grafena $D$, serta penyempitan luar biasa pita $2D$ grafena menjadi $17.5\text{ cm}^{-1}$ akibat hilangnya hamburan ketidakteraturan muatan substrat SiO$_2$.
6. **Validasi Model:** Kesesuaian model fisika maju terhadap spektrum eksperimen mencapai $R^2 \ge 0.985$ pada seluruh sampel dengan deviasi frekuensi puncak $\Delta\tilde{\nu} \le 0.8\text{ cm}^{-1}$.
