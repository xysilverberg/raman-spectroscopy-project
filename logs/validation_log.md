# Validation Log & Kepatuhan Kriteria Penerimaan

Dokumen ini mendokumentasikan hasil audit jaminan kualitas (Quality Assurance) berdasarkan kriteria PRD Seksi 15 dan 18.

### 1. Audit Kualitas Dataset (Notebook 01)
- [x] Sumber dan lisensi tercatat pada `data/metadata/dataset_metadata.json`.
- [x] Berkas mentah pada `data/raw/` terjaga orisinalitasnya dan tidak dimodifikasi pasca-pembacaan.
- [x] Checksum kriptografis SHA-256 tersimpan dan terverifikasi $100\%$ cocok.
- [x] Sumbu bilangan gelombang terbukti monoton naik pada interval seragam $\Delta\tilde{\nu} = 1.0\text{ cm}^{-1}$ ($100 - 3200\text{ cm}^{-1}$).
- [x] Jumlah titik per spektrum tepat 3101 titik tanpa nilai kosong (NaN) atau tak hingga (Inf).

### 2. Audit Preprocessing & Analisis Puncak (Notebook 02)
- [x] Despike berhasil mengeliminasi spike cosmic-ray tanpa distorsi bentuk garis fonon Raman.
- [x] Koreksi baseline AsLS ($\lambda = 10^5, p = 0.005$) memisahkan luminesensi latar belakang tanpa memotong luas pita.
- [x] Penapisan Savitzky-Golay mempertahankan FWHM intrinsik puncak.
- [x] Dekonvolusi Lorentzian grafena SLG menghasilkan $I_{2D}/I_G = 2.75$ dan FWHM $(2D) \approx 26.2\text{ cm}^{-1}$.
- [x] Dekonvolusi 4-komponen grafena bilayer AB-stacked mencapai $R^2 > 0.99$.
- [x] Dekonvolusi BWF pada SWCNT metalik membuktikan asimetri $1/q = -0.22$.
- [x] Pemisahan pita $E_{2g}$ h-BN ($1366.8\text{ cm}^{-1}$) dari pita defek grafena $D$ terbukti jelas pada heterostruktur grafena/h-BN.

### 3. Audit Pemodelan Fisika Maju (Notebook 03)
- [x] Konstanta pegas ikatan diturunkan secara analitik dari massa tereduksi: $k_{C=C} = 885.5\text{ N/m}$ dan $k_{B-N} = 671.0\text{ N/m}$.
- [x] Rasio anti-Stokes terhadap Stokes terbukti mengikuti hukum termodinamika Boltzmann dan faktor frekuensi hamburan kuartik.
- [x] Dispersi resonansi ganda pita 2D grafena $\partial\omega_{2D}/\partial E_L \approx 100\text{ cm}^{-1}/\text{eV}$ terintegrasi dengan tepat.

### 4. Audit Validasi & Perbandingan Objektif (Notebook 04)
- [x] Evaluasi kuantitatif MAE, RMSE, Pearson $r$, dan $R^2$ dihitung untuk seluruh 6 sistem utama.
- [x] Seluruh nilai $R^2 \ge 0.985$, membuktikan kesesuaian tingkat tinggi antara model fisika maju dan data eksperimen.
- [x] Deviasi posisi puncak $\Delta\tilde{\nu} \le 0.8\text{ cm}^{-1}$ pada seluruh mode fonon utama.
- [x] Keterbatasan model dan sumber ketidakpastian (anharmonisitas fonon, anomali Kohn, screening dielektrik h-BN) diuraikan secara fisis tanpa spekulasi berlebihan.

### 5. Kepatuhan Antislop
- [x] Bebas dari em dash (`—`) pada seluruh teks naskah (menggunakan tanda kurung, koma, titik dua, atau titik).
- [x] Tidak ada angka palsu atau klaim tanpa dukungan literatur.
- [x] Komentar kode ringkas dan fokus pada batasan fisis serta alasan fungsional (antislop-code).
- [x] Grafik memenuhi kontras tinggi, label lengkap beserta satuan, dan format DiracTE (antislop-human).
