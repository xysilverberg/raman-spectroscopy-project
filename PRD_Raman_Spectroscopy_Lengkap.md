# PRODUCT REQUIREMENT DOCUMENT (PRD)
# PROYEK MAKALAH DAN SIMULASI SPEKTROSKOPI RAMAN

**Versi:** 1.0  
**Status:** Dokumen spesifikasi kerja  
**Bahasa naskah:** Bahasa Indonesia akademik  
**Format naskah utama:** LaTeX (`.tex`)  
**Format analisis komputasi:** Jupyter Notebook (`.ipynb`)  
**Repository kerja:** https://github.com/xysilverberg/raman-spectroscopy-project.git  
**Dokumentasi komputasi:** https://ramanspy.readthedocs.io/en/latest/  
**Notebook referensi visualisasi:** `PaperB_plots.ipnyb`

---

## 0. Identitas Proyek

### 0.1 Tim

| Nama | NIM | Tanggung jawab utama |
|---|---:|---|
| Pradithya Putra Galang Islami | 182241014 | Koordinasi integrasi teori, derivasi, simulasi matematis, audit akhir |
| Naufal Lutfian Hakim | 182241015 | Kajian teori, seleksi Raman, referensi, pemeriksaan naskah |
| Hendra Maulana | 182241043 | Dataset, pemrosesan spektrum, visualisasi, dokumentasi komputasi |

**Dosen pembimbing:** Drs. Adri Supardi, M.S.

Pembagian tersebut merupakan pembagian kerja awal. Setiap anggota tetap wajib melakukan pemeriksaan silang terhadap bagian yang dikerjakan anggota lain. Hasil akhir merupakan tanggung jawab kelompok, bukan kumpulan bagian yang berdiri sendiri.

### 0.2 Ringkasan Proyek

Proyek ini menghasilkan makalah ilmiah mengenai spektroskopi Raman yang menghubungkan landasan fisika, penurunan matematis, kaidah seleksi, teori *resonance Raman*, instrumentasi, analisis data eksperimen publik, dan simulasi spektrum molekul.

Makalah tidak boleh berhenti pada uraian deskriptif. Setiap konsep utama harus dijelaskan melalui hubungan antara model fisika, persamaan, asumsi, konsekuensi fisis, dan bukti spektral. Bab komputasi harus memuat dua jalur yang saling melengkapi:

1. **Analisis spektrum Raman aktual:** mengunduh dataset publik, memeriksa metadata, membaca spektrum, melakukan preprocessing yang terkontrol, mengidentifikasi puncak, menghitung parameter spektral, dan menginterpretasikan hasil.
2. **Simulasi matematis molekul:** membangun spektrum dari parameter vibrasi dan perubahan polarizabilitas, menyusun kontribusi mode, memasukkan pelebaran garis dan faktor populasi yang relevan, lalu membandingkan model dengan spektrum aktual secara kritis.

Simulasi DFT dapat ditambahkan sebagai lapisan validasi lanjutan jika perangkat lunak, waktu, dan sumber daya tersedia. Namun, simulasi matematis berbasis persamaan fisika tetap wajib dan tidak boleh digantikan oleh grafik buatan tanpa dasar.

### 0.3 Tujuan Utama

- Menjelaskan asal-usul hamburan Raman secara klasik dan kuantum.
- Menurunkan hubungan antara polarisasi terinduksi, polarizabilitas, dan pergeseran frekuensi Raman.
- Menurunkan dan menerapkan kaidah seleksi vibrasi serta rotasi.
- Menjelaskan mekanisme *resonance Raman* dengan kerangka transisi elektronik dan pendekatan Kramers–Heisenberg–Dirac (KHD).
- Menjelaskan arsitektur spektrometer Raman nyata berdasarkan sumber instrumentasi yang dapat diverifikasi.
- Menganalisis dataset Raman aktual secara reproducible.
- Membentuk spektrum molekul secara komputasional dari parameter dan model fisika yang terdokumentasi.
- Mengintegrasikan hasil teori dan komputasi dalam makalah LaTeX yang konsisten.

---

## 1. Ketentuan Global dan Keluaran

### 1.1 Keluaran Wajib

1. Makalah ilmiah lengkap dalam LaTeX dan PDF.
2. Notebook Jupyter yang dapat dijalankan dari awal hingga akhir.
3. Dataset mentah atau mekanisme pengunduhan yang terdokumentasi, metadata, dan data hasil pemrosesan.
4. Kode sumber untuk preprocessing, analisis puncak, simulasi, evaluasi, dan visualisasi.
5. Gambar instrumen, diagram konseptual, diagram TikZ, dan grafik hasil analisis.
6. Referensi bibliografi dengan metadata yang diverifikasi.
7. README yang menjelaskan lingkungan, struktur direktori, cara menjalankan notebook, dan cara membangun PDF.
8. Log perubahan dan catatan keterbatasan analisis.

### 1.2 Keluaran Tambahan

- Simulasi DFT atau perhitungan frekuensi vibrasi menggunakan perangkat lunak kimia komputasi.
- Perbandingan spektrum dari beberapa molekul.
- Analisis sensitivitas terhadap parameter model.
- Klasifikasi spektrum atau *machine learning*, hanya jika tujuan ilmiah dan jumlah data mendukungnya.

### 1.3 Aturan Format Persamaan

Dokumen PRD Markdown ini menggunakan `$$ ... $$` untuk persamaan display. Persamaan dalam naskah LaTeX final harus menggunakan lingkungan LaTeX yang sesuai.

Contoh persamaan display di Markdown:

$$
\mathbf{p}_{\mathrm{ind}} = \boldsymbol{\alpha}\mathbf{E}
$$

Aturan naskah LaTeX:

- Persamaan utama menggunakan `equation`.
- Derivasi panjang menggunakan `equation` dengan `aligned`.
- Persamaan tambahan yang tidak dirujuk menggunakan lingkungan tanpa nomor, misalnya `equation*` atau `align*`.
- Semua simbol didefinisikan ketika pertama kali digunakan.
- Semua besaran memiliki satuan atau dinyatakan tak berdimensi.
- Tidak boleh ada persamaan yang hanya ditempel tanpa uraian asumsi dan makna fisis.

### 1.4 Bahasa dan Gaya Akademik

- Gunakan Bahasa Indonesia formal, lugas, dan presisi.
- Istilah teknis berbahasa Inggris yang belum memiliki padanan baku ditulis *italic*.
- Hindari kalimat promosi, klaim berlebihan, dan pernyataan yang tidak ditopang sumber.
- Bedakan secara eksplisit hasil eksperimen publik, hasil preprocessing, hasil simulasi, dan interpretasi penulis.
- Setiap gambar dan tabel harus dirujuk dalam teks.
- Setiap klaim faktual yang bersumber dari literatur harus disitasi.

---

## 2. Repository, Lingkungan, dan Tata Kelola Pekerjaan

### 2.1 Repository

Repository kerja:

`https://github.com/xysilverberg/raman-spectroscopy-project.git`

Seluruh pekerjaan dilakukan secara lokal pada repository tersebut. Struktur yang sudah ada harus diaudit terlebih dahulu. Jangan menghapus, memindahkan, atau mengganti nama berkas yang telah ada sebelum memahami fungsinya.

**Batasan Git yang wajib:**

- Jangan melakukan `git push`, merge, atau mengubah branch utama tanpa persetujuan eksplisit pengguna.
- Pekerjaan baru dilakukan pada branch kerja lokal setelah struktur repository diperiksa.
- Jangan memasukkan `.venv`, cache, file sementara, checkpoint besar yang tidak diperlukan, atau dataset berlisensi terbatas ke Git.
- Jangan menimpa pekerjaan anggota lain.
- Catat perubahan struktur dan keputusan penting.

### 2.2 Audit Awal Repository

Sebelum membuat atau mengubah berkas:

1. Periksa branch aktif dan status `git status`.
2. Daftar seluruh direktori dan berkas.
3. Baca README dan konfigurasi yang sudah tersedia.
4. Identifikasi template LaTeX, file referensi, notebook, gambar, serta data yang sudah ada.
5. Temukan `PaperB_plots.ipnyb` dan periksa gaya visualnya jika file tersedia.
6. Periksa apakah ada batasan halaman, struktur bab, format sitasi, atau aturan penamaan khusus dari repository.
7. Buat ringkasan kondisi awal sebelum modifikasi.

Jika nama atau lokasi notebook acuan berbeda, jangan membuat asumsi. Cari file yang tepat dan catat hasil audit.

### 2.3 Struktur Direktori Target

Struktur berikut adalah struktur target konseptual. Jika repository sudah memiliki struktur berbeda yang valid, pertahankan struktur aktual dan petakan fungsi berkas ke direktori yang tersedia.

```text
raman-spectroscopy-project/
├── README.md
├── PRD_Raman_Spectroscopy.md
├── .gitignore
├── environment.yml                 # atau requirements.txt
├── paper/
│   ├── main.tex
│   ├── references.bib
│   ├── sections/
│   │   ├── 01_pendahuluan.tex
│   │   ├── 02_dasar_raman.tex
│   │   ├── 03_kaidah_seleksi.tex
│   │   ├── 04_resonance_raman.tex
│   │   ├── 05_instrumentasi.tex
│   │   ├── 06_analisis_simulasi.tex
│   │   └── 07_kesimpulan.tex
│   ├── figures/
│   │   ├── tikz/
│   │   ├── instrument/
│   │   └── computational/
│   └── tables/
├── notebooks/
│   ├── 01_dataset_audit.ipynb
│   ├── 02_raman_data_analysis.ipynb
│   ├── 03_molecular_raman_simulation.ipynb
│   └── 04_validation_and_comparison.ipynb
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── peak_analysis.py
│   ├── raman_physics.py
│   ├── molecular_simulation.py
│   ├── validation.py
│   └── plotting.py
├── data/
│   ├── raw/
│   ├── metadata/
│   ├── interim/
│   └── processed/
├── outputs/
│   ├── figures/
│   ├── tables/
│   ├── metrics/
│   └── simulation/
├── references/
│   ├── source_register.md
│   └── instrument_sources.md
└── logs/
    ├── change_log.md
    └── validation_log.md
```

### 2.4 Lingkungan Python

Gunakan satu lingkungan terisolasi. Versi paket harus dicatat dan tidak boleh berubah diam-diam selama analisis.

Paket minimum:

```bash
python -m venv .venv
```

Aktivasi Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Aktivasi Linux/macOS:

```bash
source .venv/bin/activate
```

Instalasi paket inti:

```bash
python -m pip install --upgrade pip
python -m pip install numpy scipy pandas matplotlib seaborn jupyter ipykernel scikit-learn ramanspy requests h5py openpyxl
```

Simpan versi lingkungan setelah paket stabil:

```bash
python -m pip freeze > requirements.txt
```

Paket tambahan seperti `lmfit`, `periodictable`, `ase`, `pyscf`, `pymatgen`, atau perangkat lunak DFT hanya ditambahkan jika memang diperlukan dan dapat dipasang secara reproducible. Jangan menjadikan dependensi opsional sebagai syarat notebook inti.

### 2.5 Standar Kode

- Gunakan fungsi terpisah untuk pembacaan data, validasi, preprocessing, fitting, dan plotting.
- Hindari nilai numerik yang di-*hard-code* tanpa penjelasan.
- Simpan parameter eksperimen dan parameter model dalam satu konfigurasi.
- Gunakan `numpy.random.default_rng(seed)` untuk simulasi stokastik.
- Jangan menimpa data mentah.
- Setiap notebook harus dapat dijalankan dari kernel bersih menggunakan *Restart & Run All*.
- Notebook tidak boleh bergantung pada variabel tersembunyi dari sesi sebelumnya.
- Simpan keluaran numerik penting ke CSV/JSON dan gambar ke PNG/PDF/SVG.
- Kode tidak boleh mengklaim data simulasi sebagai data eksperimen.

---

## 3. Kriteria Prioritas dan Batasan Realistis

### 3.1 Bobot Penentuan Prioritas

| Kriteria | Bobot | Ukuran |
|---|---:|---|
| Kesesuaian akademik | 30% | Menjawab tujuan dan ruang lingkup tugas |
| Ketepatan fisika dan matematika | 25% | Persamaan, asumsi, derivasi, interpretasi |
| Kualitas sumber | 15% | Kredibilitas, keterlacakan, relevansi |
| Keterlaksanaan | 15% | Data, perangkat lunak, waktu, sumber daya |
| Reproduksibilitas | 10% | Kode dan hasil dapat diulang |
| Kualitas penyajian | 5% | Grafik, tabel, diagram, tata letak |

### 3.2 Prioritas P0 — Wajib

- Empat bahasan teori utama.
- Derivasi analitis yang benar.
- Minimal 10 sumber sesuai komposisi target.
- Penjelasan instrumen dengan sumber yang dapat diverifikasi.
- Dataset aktual yang dapat dibaca dan ditelusuri.
- Preprocessing dan analisis spektrum aktual.
- Simulasi matematis molekul dari parameter sampai spektrum.
- Perbandingan simulasi dengan data aktual.
- Notebook berjalan dari awal hingga akhir.
- Naskah LaTeX dapat dikompilasi dan diaudit.

### 3.3 Prioritas P1 — Memperkuat

- Analisis teori grup lebih rinci.
- Analisis intensitas relatif Stokes dan anti-Stokes.
- Analisis FWHM dan ketidakpastian.
- Analisis sensitivitas parameter.
- Perbandingan beberapa spektrum atau beberapa preprocessing pipeline.
- Pembahasan respons instrumen dan resolusi spektral.

### 3.4 Prioritas P2 — Pengembangan

- DFT dan perhitungan frekuensi vibrasi.
- Perbandingan spektrum DFT dan eksperimen.
- *Machine learning* atau klasifikasi spektrum.
- Analisis molekul tambahan di luar sampel utama.

P0 harus selesai sebelum P2 dikerjakan. P2 tidak boleh mengorbankan validasi teori, dataset, notebook, dan naskah utama.

### 3.5 Batasan Realistis

1. Tidak boleh mengklaim kelompok melakukan eksperimen laboratorium jika data berasal dari dataset publik.
2. Metadata yang tidak tersedia tidak boleh diisi dengan asumsi yang disajikan sebagai fakta.
3. Model osilator harmonik adalah pendekatan ideal; keterbatasannya harus dijelaskan.
4. Simulasi matematis bukan simulasi kuantum *ab initio*.
5. DFT hanya dilakukan jika metode, basis set, geometri, perangkat lunak, dan keluaran dapat diverifikasi.
6. Intensitas simulasi tidak boleh disamakan dengan intensitas eksperimen tanpa model respons instrumen dan faktor fisik terkait.
7. Status Q1 harus diverifikasi berdasarkan tahun dan kategori yang sesuai; jangan menebak kuartil.
8. Artikel preprint arXiv harus diberi label preprint, bukan disebut artikel *peer-reviewed*.
9. Diagram instrumen konseptual harus diberi label sebagai diagram umum, bukan foto atau spesifikasi alat tertentu.
10. Jika batas halaman berlaku, ringkas bagian sekunder terlebih dahulu; jangan menghapus derivasi wajib.

---

## 4. Spesifikasi Makalah Ilmiah

### 4.1 Struktur Makalah

Struktur bab final mengikuti template repository jika sudah ditetapkan. Secara isi, makalah harus memuat:

1. Pendahuluan.
2. Dasar teori hamburan dan spektroskopi Raman.
3. Kaidah seleksi Raman.
4. Teori *resonance Raman*.
5. Instrumentasi spektrometer Raman.
6. Analisis dataset dan simulasi molekul.
7. Kesimpulan dan saran.

### 4.2 Pendahuluan

Wajib memuat:

- Latar belakang spektroskopi Raman.
- Perbedaan umum spektroskopi Raman dan inframerah.
- Permasalahan ilmiah yang dibahas.
- Tujuan dan batasan makalah.
- Alur pendekatan teori dan komputasi.

### 4.3 Dasar Teori Hamburan dan Spektroskopi Raman

Bahasan minimum:

- Interaksi medan elektromagnetik dengan molekul.
- Momen dipol terinduksi.
- Tensor polarizabilitas.
- Hamburan elastik dan inelastik.
- Rayleigh, Stokes, dan anti-Stokes.
- Pendekatan klasik.
- Pendekatan kuantum menggunakan tingkat energi vibrasi.
- Pergeseran Raman dalam bilangan gelombang.
- Hubungan intensitas Stokes dan anti-Stokes dengan populasi termal.

#### 4.3.1 Derivasi Klasik Momen Dipol Terinduksi

Mulai dari hubungan momen dipol terinduksi dan medan listrik:

$$
\mathbf{p}_{\mathrm{ind}}(t)=\boldsymbol{\alpha}(t)\mathbf{E}(t)
$$

Untuk pendekatan satu dimensi:

$$
p_{\mathrm{ind}}(t)=\alpha(t)E(t)
$$

Medan laser monokromatik ditulis:

$$
E(t)=E_0\cos(\omega_0 t)
$$

Untuk satu koordinat normal vibrasi \(Q\), polarizabilitas dikembangkan di sekitar posisi kesetimbangan:

$$
\alpha(Q)=\alpha_0+
\left(\frac{\partial\alpha}{\partial Q}\right)_0 Q+
\frac{1}{2}\left(\frac{\partial^2\alpha}{\partial Q^2}\right)_0Q^2+\cdots
$$

Dalam pendekatan vibrasi harmonik:

$$
Q(t)=Q_0\cos(\omega_v t)
$$

Dengan mengabaikan suku orde lebih tinggi untuk derivasi awal:

$$
p_{\mathrm{ind}}(t)=
\alpha_0E_0\cos(\omega_0t)
+
\left(\frac{\partial\alpha}{\partial Q}\right)_0
Q_0E_0\cos(\omega_vt)\cos(\omega_0t)
$$

Gunakan identitas trigonometri:

$$
\cos A\cos B=\frac{1}{2}\left[\cos(A+B)+\cos(A-B)\right]
$$

Sehingga:

$$
\begin{aligned}
p_{\mathrm{ind}}(t)
={}&\alpha_0E_0\cos(\omega_0t)\\
&+\frac{1}{2}\left(\frac{\partial\alpha}{\partial Q}\right)_0Q_0E_0
\cos[(\omega_0+\omega_v)t]\\
&+\frac{1}{2}\left(\frac{\partial\alpha}{\partial Q}\right)_0Q_0E_0
\cos[(\omega_0-\omega_v)t]
\end{aligned}
$$

Interpretasi:

- Suku pada \(\omega_0\) merupakan hamburan Rayleigh.
- Suku pada \(\omega_0-\omega_v\) merupakan garis Stokes.
- Suku pada \(\omega_0+\omega_v\) merupakan garis anti-Stokes.

Aktivitas Raman untuk mode tersebut memerlukan:

$$
\left(\frac{\partial\alpha}{\partial Q}\right)_0\neq 0
$$

Derivasi harus dilanjutkan untuk tensor polarizabilitas dan menjelaskan bahwa intensitas bergantung pada geometri hamburan, polarisasi, dan komponen tensor yang relevan.

#### 4.3.2 Pergeseran Raman

Bilangan gelombang laser dan hamburan:

$$
\tilde{\nu}_0=\frac{1}{\lambda_0}
\qquad
\tilde{\nu}_s=\frac{1}{\lambda_s}
$$

Pergeseran Raman Stokes:

$$
\Delta\tilde{\nu}_{S}=\tilde{\nu}_0-\tilde{\nu}_s
$$

Pergeseran anti-Stokes:

$$
\Delta\tilde{\nu}_{AS}=\tilde{\nu}_s-\tilde{\nu}_0
$$

Pastikan satuan panjang gelombang dikonversi secara benar. Jika \(\lambda\) dinyatakan dalam nm, konversi bilangan gelombang harus konsisten ke cm\(^{-1}\).

Contoh numerik harus menghitung pergeseran dari panjang gelombang laser dan panjang gelombang hamburan yang benar-benar diberikan. Jangan mencampur panjang gelombang dengan bilangan gelombang tanpa konversi.

#### 4.3.3 Pendekatan Kuantum Osilator Harmonik

Energi vibrasi:

$$
E_v=\hbar\omega_v\left(v+\frac{1}{2}\right)
$$

Operator koordinat:

$$
\hat Q=\sqrt{\frac{\hbar}{2\mu\omega_v}}(\hat a+\hat a^\dagger)
$$

Elemen matriks koordinat:

$$
\langle v'|\hat Q|v\rangle
=
\sqrt{\frac{\hbar}{2\mu\omega_v}}
\left[
\sqrt{v}\,\delta_{v',v-1}
+
\sqrt{v+1}\,\delta_{v',v+1}
\right]
$$

Untuk transisi vibrasi fundamental, bahas \(\Delta v=\pm1\) sebagai hasil elemen matriks operator koordinat dalam pendekatan harmonik. Jelaskan bahwa kaidah Raman berasal dari ketergantungan polarizabilitas pada koordinat normal, bukan menyamakan begitu saja kaidah transisi dipol listrik IR dengan Raman.

#### 4.3.4 Rasio Stokes dan Anti-Stokes

Populasi termal tingkat vibrasi mengikuti distribusi Boltzmann:

$$
N_v\propto \exp\left(-\frac{E_v}{k_BT}\right)
$$

Untuk satu mode vibrasi, rasio intensitas anti-Stokes terhadap Stokes secara umum memiliki faktor populasi dan faktor frekuensi hamburan:

$$
\frac{I_{AS}}{I_S}
\approx
\left(\frac{\omega_0+\omega_v}{\omega_0-\omega_v}\right)^4
\exp\left(-\frac{\hbar\omega_v}{k_BT}\right)
$$

Jelaskan asumsi pendekatan ini dan bahwa faktor frekuensi dapat ditulis dalam bentuk panjang gelombang atau bilangan gelombang yang ekuivalen apabila definisi frekuensinya konsisten.

### 4.4 Kaidah Seleksi Raman

Bahasan minimum:

- Koordinat normal dan mode vibrasi.
- Perubahan polarizabilitas terhadap koordinat normal.
- Elemen matriks transisi Raman.
- Kaidah seleksi vibrasi.
- Kaidah seleksi rotasi.
- Simetri molekul dan teori grup.
- Perbedaan aktivitas Raman dan IR.
- Contoh molekul CO₂ dan H₂O.

#### 4.4.1 Kaidah Seleksi Vibrasi

Ekspansi tensor polarizabilitas:

$$
\alpha_{ij}(Q)=
\alpha_{ij}^{(0)}
+
\sum_k
\left(\frac{\partial\alpha_{ij}}{\partial Q_k}\right)_0Q_k+\cdots
$$

Syarat aktivitas mode \(k\):

$$
\left(\frac{\partial\alpha_{ij}}{\partial Q_k}\right)_0\neq0
$$

Untuk pendekatan harmonik, elemen matriks koordinat memberikan:

$$
\Delta v_k=\pm1
$$

Tunjukkan bahwa mode vibrasi harus mentransformasikan seperti salah satu komponen tensor polarizabilitas yang relevan. Bahas komponen diagonal dan luar diagonal tensor.

#### 4.4.2 Kaidah Seleksi Rotasi

Untuk hamburan Raman rotasi molekul linear pada pendekatan rotor yang sesuai, jelaskan kaidah seleksi:

$$
\Delta J=0,\pm2
$$

Jelaskan arti cabang O, Q, dan S jika relevan, serta kondisi ketika cabang tertentu tidak muncul atau tidak teramati. Jangan menerapkan kaidah molekul linear secara otomatis pada semua molekul.

#### 4.4.3 Contoh Teori Grup: CO₂

CO₂ memiliki simetri linear centrosimetrik. Gunakan karakter tabel yang tepat untuk grup titik yang sesuai, dan verifikasi representasi mode vibrasinya dari sumber teori grup molekul.

Target analisis:

- Tentukan jumlah mode vibrasi normal.
- Identifikasi simetri masing-masing mode.
- Tentukan aktivitas IR dan Raman.
- Jelaskan konsekuensi pusat inversi melalui aturan eksklusi mutual untuk mode yang relevan.

Jangan mengunci representasi irreducible atau label simetri sebelum memeriksa konvensi grup titik dan notasi yang digunakan. Untuk molekul linear, gunakan notasi yang sesuai dan jelaskan pemetaan ke notasi karakter tabel yang dipakai.

#### 4.4.4 Contoh H₂O

H₂O digunakan sebagai contoh molekul non-centrosimetrik dengan grup titik \(C_{2v}\). Identifikasi mode vibrasi, simetri, dan aktivitas Raman/IR menggunakan karakter tabel \(C_{2v}\). Sajikan tabel ringkas dengan dasar karakter tabel yang benar.

### 4.5 Teori Resonance Raman

Bahasan minimum:

- Keadaan elektronik dasar dan tereksitasi.
- Interaksi radiasi-materi.
- Amplitudo hamburan Raman.
- Persamaan Kramers–Heisenberg–Dirac.
- Kondisi resonansi.
- Faktor penguatan intensitas.
- Mekanisme Franck–Condon dan Herzberg–Teller.
- Pelebaran garis dan redaman.
- Perbedaan Raman biasa dan *resonance Raman*.

#### 4.5.1 Hamiltonian Interaksi

Dalam pendekatan dipol listrik:

$$
\hat H_{\mathrm{int}}=-\hat{\boldsymbol{\mu}}\cdot\mathbf E(t)
$$

Pembahasan harus menunjukkan bagaimana interaksi dua foton menghasilkan amplitudo hamburan orde kedua. Jelaskan keadaan awal, keadaan antara, dan keadaan akhir.

#### 4.5.2 Bentuk KHD

Gunakan bentuk KHD yang konsisten dengan konvensi energi dan redaman yang dirujuk. Secara skematis, amplitudo hamburan dapat ditulis:

$$
\mathcal A_{fi}\propto
\sum_n
\left[
\frac{
\langle f|\hat{\boldsymbol{\mu}}\cdot\mathbf e_s|n\rangle
\langle n|\hat{\boldsymbol{\mu}}\cdot\mathbf e_i|i\rangle
}{
E_n-E_i-\hbar\omega_i-i\Gamma_n
}
+
\frac{
\langle f|\hat{\boldsymbol{\mu}}\cdot\mathbf e_i|n\rangle
\langle n|\hat{\boldsymbol{\mu}}\cdot\mathbf e_s|i\rangle
}{
E_n-E_i+\hbar\omega_s+i\Gamma_n
}
\right]
$$

Persamaan di atas bersifat skematis. Naskah final wajib memeriksa tanda, definisi energi, faktor prefaktor, dan konvensi redaman terhadap referensi primer yang digunakan. Jangan menyalin bentuk persamaan tanpa memastikan konsistensi notasi.

Kondisi resonansi terjadi ketika energi foton datang mendekati selisih energi elektronik yang relevan:

$$
\hbar\omega_i\approx E_n-E_i
$$

Jelaskan bahwa penyebut amplitudo menjadi kecil secara efektif, tetapi redaman \(\Gamma_n\) mencegah divergensi matematis dan merepresentasikan pelebaran keadaan antara.

#### 4.5.3 Mekanisme Penguatan

Bahas secara terpisah:

- *Franck–Condon mechanism*: perubahan koordinat kesetimbangan dan overlap vibrasi pada permukaan energi potensial elektronik.
- *Herzberg–Teller mechanism*: ketergantungan momen transisi elektronik terhadap koordinat vibrasi dan pencampuran keadaan elektronik.

Berikan diagram tingkat energi menggunakan TikZ jika diagram dapat dibuat dengan jelas dan tidak bertumpuk.

### 4.6 Instrumentasi Spektrometer Raman

Jelaskan jalur optik dan elektronik:

1. Sumber laser.
2. Optik pengarah dan pemfokus.
3. Sampel dan geometri pengumpulan hamburan.
4. Filter penolak Rayleigh, misalnya *edge filter* atau *notch filter*.
5. Celah dan optik pencitraan.
6. Kisi difraksi atau *spectrograph*.
7. Detektor CCD, EMCCD, InGaAs, atau detektor lain sesuai instrumen.
8. Elektronika pembacaan dan perangkat lunak.

Diagram blok minimal:

```text
Laser
  |
  v
Optik pengarah/pemfokus
  |
  v
Sampel
  |
  v
Optik pengumpul
  |
  v
Filter Rayleigh
  |
  v
Celah + kisi difraksi
  |
  v
Detektor
  |
  v
Akuisisi dan pemrosesan spektrum
```

Bahasan kuantitatif:

- Panjang gelombang laser dan energi foton.
- Persamaan kisi difraksi.
- Resolusi spektral.
- Rentang bilangan gelombang.
- Peran filter terhadap hamburan Rayleigh.
- Respons detektor dan rasio signal-to-noise.
- Pengaruh daya laser dan pemanasan sampel.
- Kalibrasi bilangan gelombang.

Persamaan kisi:

$$
m\lambda=d(\sin\theta_i+\sin\theta_d)
$$

dengan konvensi sudut yang dinyatakan secara eksplisit. Jangan menggunakan persamaan kisi tanpa mendefinisikan geometri dan orde difraksi.

Gunakan foto atau diagram dari sumber produsen/publikasi yang dapat diverifikasi. Cantumkan model instrumen, panjang gelombang laser, detektor, resolusi, dan rentang spektrum hanya jika tersedia dalam dokumentasi sumber. Jika tidak, gunakan diagram konseptual dan tandai sebagai konfigurasi umum.

### 4.7 Bab Analisis Dataset dan Simulasi

Bab ini merupakan bagian inti integrasi antara teori dan komputasi. Semua gambar utama yang berasal dari analisis harus dibuat dari notebook, bukan digambar ulang secara manual.

---

## 5. Dataset Raman Aktual

### 5.1 Dataset Utama yang Direkomendasikan

Gunakan dataset dari artikel:

Flanagan, A. R., & Glavin, F. G. (2025). *Open-source Raman spectra of chemical compounds for active pharmaceutical ingredient development*. Scientific Data, 12, 498.  
DOI: https://doi.org/10.1038/s41597-025-04848-6

Artikel melaporkan dataset terbuka berisi 3.510 spektrum dari 32 zat kimia. Dataset ini menjadi kandidat utama karena menyediakan spektrum Raman eksperimental untuk analisis dan pemodelan. Sebelum analisis, unduh data dari tautan data resmi yang dicantumkan artikel dan periksa lisensi serta struktur berkas.

Sumber artikel:
- https://www.nature.com/articles/s41597-025-04848-6
- https://pubmed.ncbi.nlm.nih.gov/40128276/

Lokasi data:
- Gunakan tautan Figshare atau repositori data yang ditautkan langsung dari artikel versi penerbit.
- Catat URL unduhan final, tanggal akses, nama berkas, ukuran, checksum, lisensi, dan versi data pada `data/metadata/`.

**Penting:** jumlah titik spektral, rentang bilangan gelombang, resolusi, jumlah replikasi per senyawa, dan format berkas harus diverifikasi langsung dari file dataset yang diunduh. Jangan menjadikan angka ringkasan sebagai pengganti pemeriksaan data aktual.

### 5.2 Prosedur Audit Dataset

Notebook `01_dataset_audit.ipynb` wajib:

1. Menampilkan daftar file dan ukuran.
2. Membaca format file yang disediakan.
3. Mengidentifikasi kolom atau array bilangan gelombang dan intensitas.
4. Memeriksa satuan sumbu spektral.
5. Memeriksa nilai kosong, NaN, inf, duplikasi, dan nilai tidak wajar.
6. Memeriksa apakah sumbu bilangan gelombang seragam antar-spektrum.
7. Menghitung jumlah senyawa, jumlah spektrum, dan jumlah titik per spektrum.
8. Memeriksa distribusi jumlah replikasi per senyawa.
9. Menampilkan beberapa spektrum mentah.
10. Menyimpan ringkasan metadata dalam CSV/JSON.

Kriteria lolos:

- Sumbu spektral monoton.
- Intensitas numerik dan terbaca.
- Tidak ada kesalahan pemetaan antara label senyawa dan spektrum.
- Unit dan rentang sumbu diketahui atau diberi status tidak diketahui.
- File mentah tidak dimodifikasi.

### 5.3 Struktur Metadata Minimum

Simpan metadata dengan field berikut jika tersedia:

| Field | Keterangan |
|---|---|
| `dataset_name` | Nama dataset |
| `source_doi` | DOI artikel |
| `source_url` | URL repositori data |
| `download_date` | Tanggal pengunduhan |
| `license` | Lisensi |
| `file_name` | Nama berkas |
| `file_hash` | SHA-256 |
| `compound` | Identitas senyawa |
| `spectrum_id` | ID spektrum |
| `wavenumber_unit` | Unit sumbu |
| `intensity_unit` | Unit intensitas atau arbitrary units |
| `instrument` | Instrumen jika dilaporkan |
| `excitation_wavelength` | Panjang gelombang laser jika dilaporkan |
| `notes` | Catatan metadata |

---

## 6. Notebook 1 — Audit dan Pembacaan Dataset

**Nama:** `01_dataset_audit.ipynb`

### 6.1 Struktur Notebook

1. Judul dan tujuan.
2. Penjelasan sumber dataset.
3. Import seluruh library.
4. Definisi direktori dan konfigurasi.
5. Pemeriksaan keberadaan file.
6. Pembacaan data.
7. Validasi struktur dan metadata.
8. Pemeriksaan kualitas data.
9. Visualisasi spektrum mentah.
10. Ekspor metadata dan ringkasan audit.

### 6.2 Import Awal

Notebook harus dimulai dengan import library yang digunakan pada notebook tersebut. Contoh:

```python
from pathlib import Path
import json
import hashlib
import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.signal import find_peaks
from scipy.stats import describe

RANDOM_SEED = 42
rng = np.random.default_rng(RANDOM_SEED)

PROJECT_ROOT = Path.cwd()
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_METADATA = PROJECT_ROOT / "data" / "metadata"
OUTPUT_FIGURES = PROJECT_ROOT / "outputs" / "figures"

for directory in [DATA_RAW, DATA_METADATA, OUTPUT_FIGURES]:
    directory.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "figure.dpi": 120,
    "savefig.dpi": 300,
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 11,
    "legend.fontsize": 8,
    "figure.figsize": (8, 5),
    "axes.spines.top": False,
    "axes.spines.right": False,
})
```

Kode final harus disesuaikan dengan struktur data yang benar-benar diunduh. Jangan mengarang nama kolom atau nama file sebelum memeriksa dataset.

### 6.3 Pemeriksaan Checksum

Gunakan SHA-256 agar file yang dianalisis dapat diidentifikasi:

```python
def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()
```

Simpan checksum bersama metadata. Jika dataset diperbarui, catat perubahan hash.

### 6.4 Visualisasi Data Mentah

Wajib menampilkan:

- Beberapa spektrum dari senyawa yang sama.
- Spektrum dari beberapa senyawa berbeda.
- Overlay spektrum untuk melihat variasi.
- Peta intensitas atau *heatmap* jika bentuk dataset mendukungnya.

Jangan menormalisasi semua spektrum sebelum visualisasi awal. Spektrum mentah perlu diperiksa terlebih dahulu agar karakteristik noise, baseline, dan rentang intensitas terlihat.

---

## 7. Notebook 2 — Preprocessing dan Analisis Spektrum Aktual

**Nama:** `02_raman_data_analysis.ipynb`

### 7.1 Tujuan

- Menghilangkan gangguan yang dapat diidentifikasi tanpa merusak pita Raman.
- Memisahkan baseline dari sinyal spektral.
- Menghasilkan spektrum yang dapat dibandingkan.
- Mengidentifikasi posisi puncak.
- Mengukur intensitas, lebar puncak, dan luas puncak.
- Menginterpretasikan fitur spektral dengan dukungan literatur.

### 7.2 Tahap Preprocessing

Urutan umum yang harus dievaluasi:

1. Validasi sumbu spektral dan intensitas.
2. Pemeriksaan cosmic-ray spike.
3. Denoising secukupnya.
4. Koreksi baseline.
5. Pemotongan rentang spektral yang relevan.
6. Normalisasi untuk tujuan perbandingan tertentu.

Jangan menerapkan seluruh tahap secara otomatis tanpa membandingkan spektrum sebelum dan sesudahnya. Simpan spektrum pada setiap tahap.

### 7.3 RamanSPy

Dokumentasi:
- https://ramanspy.readthedocs.io/en/latest/
- https://ramanspy.readthedocs.io/en/latest/preprocessing.html
- https://ramanspy.readthedocs.io/en/stable/auto_examples/plot_i_preprocessing_pipelines.html

RamanSPy menyediakan fungsi untuk *cosmic-ray removal*, denoising, koreksi baseline, normalisasi, serta pipeline preprocessing. Gunakan API sesuai versi paket yang terpasang. Periksa dokumentasi versi yang digunakan sebelum menulis kode final.

Pipeline awal yang dapat diuji:

```python
import ramanspy as rp

pipeline = rp.preprocessing.Pipeline([
    rp.preprocessing.despike.WhitakerHayes(),
    rp.preprocessing.denoise.SavGol(
        window_length=9,
        polyorder=3
    ),
    rp.preprocessing.baseline.ASLS(),
    rp.preprocessing.normalise.Vector()
])
```

Kode di atas merupakan contoh pola pipeline, bukan jaminan langsung cocok untuk semua bentuk input. Bentuk objek data, sumbu spektral, dan versi API harus diperiksa. Jika data berbentuk array sederhana, preprocessing dapat dilakukan menggunakan SciPy atau implementasi tervalidasi sendiri.

### 7.4 Baseline Correction

Jelaskan bahwa spektrum terukur dapat dimodelkan sebagai:

$$
y(\tilde{\nu})=s(\tilde{\nu})+b(\tilde{\nu})+\epsilon(\tilde{\nu})
$$

dengan:

- \(s\): sinyal Raman.
- \(b\): baseline.
- \(\epsilon\): noise.

Metode Asymmetric Least Squares (AsLS) dapat dinyatakan sebagai minimisasi:

$$
\min_{\mathbf z}
\left\{
\sum_{i=1}^{N}w_i(y_i-z_i)^2
+
\lambda\sum_{i=2}^{N-1}(\Delta^2 z_i)^2
\right\}
$$

Jelaskan peran parameter \(\lambda\), bobot asimetris, dan operator beda kedua. Lakukan pemeriksaan sensitivitas parameter agar baseline tidak memotong puncak Raman.

### 7.5 Denoising

Savitzky–Golay melakukan pendekatan polinomial lokal. Parameter `window_length` dan `polyorder` harus dicatat. Pastikan:

- `window_length` ganjil.
- `polyorder < window_length`.
- Jendela tidak terlalu lebar dibandingkan lebar puncak.
- Hasil dibandingkan dengan data sebelum filtering.

### 7.6 Normalisasi

Metode normalisasi yang boleh dievaluasi:

- Vector normalization.
- Min-max normalization.
- Area-under-curve normalization.
- Normalisasi terhadap puncak referensi jika terdapat alasan fisik.

Normalisasi mengubah skala intensitas. Karena itu, jangan menggunakan spektrum ternormalisasi untuk menyimpulkan intensitas absolut atau konsentrasi tanpa kalibrasi yang sesuai.

### 7.7 Analisis Puncak

Gunakan `scipy.signal.find_peaks` sebagai alat identifikasi awal. Parameter prominence, distance, dan width harus dicatat serta diuji.

Untuk setiap puncak, hitung:

- Posisi puncak \(\tilde{\nu}_p\).
- Intensitas puncak.
- *Prominence*.
- FWHM.
- Luas puncak jika fitting dilakukan.

FWHM:

$$
\mathrm{FWHM}=\tilde{\nu}_{+}-\tilde{\nu}_{-}
$$

dengan \(\tilde{\nu}_{+}\) dan \(\tilde{\nu}_{-}\) adalah posisi pada setengah tinggi maksimum setelah baseline lokal diperhitungkan.

### 7.8 Fitting Puncak

Model Gaussian:

$$
I_G(\tilde{\nu})=
A\exp\left[
-\frac{(\tilde{\nu}-\tilde{\nu}_0)^2}{2\sigma^2}
\right]
$$

Hubungan FWHM Gaussian:

$$
\mathrm{FWHM}_G=2\sqrt{2\ln2}\,\sigma
$$

Model Lorentzian:

$$
I_L(\tilde{\nu})=
A\frac{\gamma^2}{(\tilde{\nu}-\tilde{\nu}_0)^2+\gamma^2}
$$

Hubungan FWHM Lorentzian:

$$
\mathrm{FWHM}_L=2\gamma
$$

Voigt dapat digunakan jika ada alasan untuk menggabungkan pelebaran Gaussian dan Lorentzian. Pilihan model harus dinilai dari residual, kualitas fitting, dan konteks fisika, bukan hanya nilai \(R^2\).

### 7.9 Interpretasi Spektrum

Interpretasi tidak boleh hanya menyebut bahwa puncak tertentu “menunjukkan ikatan tertentu” tanpa dukungan. Untuk setiap penugasan pita:

1. Laporkan posisi puncak.
2. Laporkan ketidakpastian atau variasi antar-replikasi jika tersedia.
3. Bandingkan dengan literatur atau basis data spektral yang relevan.
4. Jelaskan mode vibrasi yang mungkin.
5. Nyatakan kemungkinan tumpang tindih pita.
6. Bedakan penugasan yang kuat dan yang tentatif.

### 7.10 Keluaran Notebook 2

- `outputs/figures/raw_spectra.png`
- `outputs/figures/preprocessing_comparison.png`
- `outputs/figures/processed_spectra.png`
- `outputs/figures/peak_detection.png`
- `outputs/tables/peak_table.csv`
- `outputs/tables/preprocessing_parameters.csv`
- `outputs/metrics/data_quality_report.json`

Nama file dapat disesuaikan, tetapi semua keluaran harus konsisten dan terdokumentasi.

---

## 8. Notebook 3 — Simulasi Matematis Molekul dari Dasar Fisika

**Nama:** `03_molecular_raman_simulation.ipynb`

### 8.1 Tujuan

Notebook ini wajib membangun spektrum Raman dari persamaan dan parameter molekul, bukan hanya melakukan fitting pada data eksperimen. Semua parameter simulasi harus memiliki asal-usul yang jelas: diambil dari literatur, dihitung, atau dipilih sebagai parameter ilustratif dan diberi label demikian.

### 8.2 Model Fisis Minimum

Model minimum mencakup:

1. Mode vibrasi molekul.
2. Frekuensi vibrasi tiap mode.
3. Perubahan polarizabilitas terhadap koordinat normal.
4. Aktivitas Raman.
5. Posisi garis Stokes dan/atau anti-Stokes.
6. Intensitas relatif yang sesuai dengan model yang digunakan.
7. Pelebaran garis spektral.
8. Penjumlahan kontribusi beberapa mode.
9. Noise dan baseline sintetis opsional.
10. Perbandingan spektrum simulasi dengan spektrum aktual.

### 8.3 Osilator Harmonik Molekul

Untuk mode vibrasi yang diperlakukan sebagai osilator harmonik:

$$
\mu\frac{d^2Q}{dt^2}+kQ=0
$$

Frekuensi sudut:

$$
\omega_v=\sqrt{\frac{k}{\mu}}
$$

Frekuensi dalam Hz:

$$
f_v=\frac{\omega_v}{2\pi}
$$

Bilangan gelombang vibrasi:

$$
\tilde{\nu}_v=\frac{\omega_v}{2\pi c}
$$

Gunakan satuan SI secara konsisten. Jika \(\mu\) adalah massa tereduksi dalam kg dan \(k\) dalam N m\(^{-1}\), hasil \(\omega_v\) dalam rad s\(^{-1}\). Konversi ke cm\(^{-1}\) harus menggunakan \(c\) dalam cm s\(^{-1}\) atau konversi eksplisit.

Massa tereduksi untuk diatomik:

$$
\mu=\frac{m_1m_2}{m_1+m_2}
$$

### 8.4 Hubungan dengan Polarizabilitas

Untuk mode \(j\):

$$
\alpha_j(Q_j)=\alpha_{j,0}+
\left(\frac{\partial\alpha_j}{\partial Q_j}\right)_0Q_j+\cdots
$$

Definisikan parameter aktivitas Raman:

$$
R_j=\left(\frac{\partial\alpha_j}{\partial Q_j}\right)_0
$$

Dalam model sederhana, intensitas relatif mode dapat diparameterkan dengan:

$$
I_j\propto C_j|R_j|^2
$$

dengan \(C_j\) memuat faktor geometrik dan frekuensi sesuai pendekatan yang dipilih. Jika \(C_j\) tidak dihitung dari model lengkap, nyatakan bahwa intensitas adalah intensitas relatif model, bukan intensitas absolut eksperimen.

### 8.5 Posisi Stokes dan Anti-Stokes

Untuk bilangan gelombang laser \(\tilde{\nu}_0\) dan mode vibrasi \(\tilde{\nu}_j\):

$$
\tilde{\nu}_{S,j}=\tilde{\nu}_0-\tilde{\nu}_j
$$

$$
\tilde{\nu}_{AS,j}=\tilde{\nu}_0+\tilde{\nu}_j
$$

Jika spektrum diplot sebagai Raman shift, sumbu x harus didefinisikan sebagai pergeseran Raman dan bukan bilangan gelombang foton hamburan. Pilih satu konvensi dan gunakan secara konsisten.

### 8.6 Intensitas Termal

Populasi vibrasi pada temperatur \(T\):

$$
P(v)=
\left(1-e^{-\hbar\omega_v/(k_BT)}\right)
e^{-v\hbar\omega_v/(k_BT)}
$$

Untuk model harmonik, rasio anti-Stokes/Stokes dapat menggunakan:

$$
\frac{I_{AS}}{I_S}
\approx
\left(\frac{\omega_0+\omega_v}{\omega_0-\omega_v}\right)^4
\exp\left(-\frac{\hbar\omega_v}{k_BT}\right)
$$

Catat temperatur, frekuensi laser, dan mode vibrasi. Jika hanya Stokes yang dimodelkan, nyatakan batasan tersebut.

### 8.7 Profil Garis Spektral

Gunakan profil Gaussian atau Lorentzian. Contoh Lorentzian ternormalisasi:

$$
L(\tilde{\nu};\tilde{\nu}_0,\gamma)=
\frac{1}{\pi}
\frac{\gamma}{(\tilde{\nu}-\tilde{\nu}_0)^2+\gamma^2}
$$

Spektrum total:

$$
S(\tilde{\nu})=
\sum_{j=1}^{M}A_j
L(\tilde{\nu};\tilde{\nu}_j,\gamma_j)
$$

Untuk Gaussian:

$$
G(\tilde{\nu};\tilde{\nu}_0,\sigma)=
\frac{1}{\sigma\sqrt{2\pi}}
\exp\left[
-\frac{(\tilde{\nu}-\tilde{\nu}_0)^2}{2\sigma^2}
\right]
$$

Spektrum total dengan baseline dan noise:

$$
S_{\mathrm{obs}}(\tilde{\nu})=
S(\tilde{\nu})+b(\tilde{\nu})+\epsilon(\tilde{\nu})
$$

Noise sintetis harus dipisahkan dari spektrum ideal dan diberi seed acak agar dapat direproduksi.

### 8.8 Model Multi-Mode

Buat tabel parameter setiap mode:

| Parameter | Makna | Sumber |
|---|---|---|
| `mode_id` | Identitas mode | Definisi simulasi |
| `wavenumber_cm1` | Frekuensi vibrasi | Literatur/perhitungan |
| `raman_activity` | Aktivitas atau intensitas relatif | Literatur/perhitungan/asumsi eksplisit |
| `linewidth_cm1` | Lebar garis | Literatur atau asumsi model |
| `symmetry` | Simetri mode | Analisis teori grup |
| `assignment` | Penugasan vibrasi | Literatur/analisis |

Minimal gunakan beberapa mode agar terbentuk spektrum multi-puncak yang dapat dibandingkan dengan data aktual. Jika parameter molekul belum tersedia, gunakan parameter ilustratif hanya untuk menguji implementasi, lalu pisahkan hasil ilustratif dari hasil molekul yang dianalisis.

### 8.9 Struktur Fungsi Kode

Kode simulasi harus modular, minimal memuat fungsi:

```python
def reduced_mass(m1, m2):
    """Menghitung massa tereduksi dalam satuan SI."""
    raise NotImplementedError

def harmonic_wavenumber(force_constant, reduced_mass_kg):
    """Menghitung bilangan gelombang vibrasi dalam cm^-1."""
    raise NotImplementedError

def stokes_shift(laser_wavenumber, vibrational_wavenumber):
    """Menghitung posisi Stokes pada konvensi sumbu yang ditetapkan."""
    raise NotImplementedError

def anti_stokes_shift(laser_wavenumber, vibrational_wavenumber):
    """Menghitung posisi anti-Stokes."""
    raise NotImplementedError

def lorentzian(x, center, gamma, amplitude):
    """Profil garis Lorentzian."""
    raise NotImplementedError

def gaussian(x, center, sigma, amplitude):
    """Profil garis Gaussian."""
    raise NotImplementedError

def build_spectrum(x, modes, profile="lorentzian"):
    """Menjumlahkan kontribusi seluruh mode."""
    raise NotImplementedError
```

`NotImplementedError` di atas hanya merupakan kontrak fungsi dalam PRD. Implementasi final wajib menggantinya dengan kode yang benar dan diuji.

### 8.10 Eksperimen Numerik yang Wajib

Lakukan setidaknya eksperimen numerik berikut:

1. Variasi frekuensi vibrasi untuk melihat pergeseran garis.
2. Variasi aktivitas Raman untuk melihat perubahan intensitas relatif.
3. Variasi linewidth untuk melihat pelebaran puncak.
4. Variasi temperatur untuk membandingkan intensitas Stokes dan anti-Stokes.
5. Variasi panjang gelombang laser untuk melihat perubahan posisi absolut garis hamburan dan faktor frekuensi jika dimodelkan.
6. Variasi noise untuk menguji kestabilan deteksi puncak.
7. Variasi baseline untuk menguji ketahanan koreksi baseline.

Setiap eksperimen numerik harus memiliki pertanyaan, parameter yang diubah, parameter tetap, hasil, dan interpretasi.

### 8.11 Keluaran Notebook 3

- Tabel parameter molekul.
- Grafik spektrum ideal.
- Grafik Stokes dan anti-Stokes.
- Grafik variasi linewidth.
- Grafik variasi temperatur.
- Grafik variasi laser.
- Grafik spektrum multi-mode.
- File parameter simulasi JSON/CSV.
- File hasil spektrum simulasi CSV.
- Catatan asumsi dan keterbatasan.

---

## 9. Notebook 4 — Validasi dan Perbandingan Simulasi dengan Data Aktual

**Nama:** `04_validation_and_comparison.ipynb`

### 9.1 Tujuan

Membandingkan model matematis dengan spektrum aktual tanpa menyatakan bahwa model sederhana harus cocok sempurna dengan eksperimen.

### 9.2 Penyelarasan Sumbu

Sebelum perbandingan:

- Pastikan keduanya memakai Raman shift dalam cm\(^{-1}\).
- Pastikan orientasi sumbu sama.
- Pastikan rentang spektrum tumpang tindih.
- Jika diperlukan, lakukan interpolasi pada grid yang terdokumentasi.
- Jangan melakukan ekstrapolasi tanpa alasan.
- Catat resolusi dan interval sampling.

### 9.3 Parameter Perbandingan

Gunakan metrik sesuai tujuan:

Mean Absolute Error:

$$
\mathrm{MAE}=
\frac{1}{N}\sum_{i=1}^{N}|y_i-\hat y_i|
$$

Root Mean Squared Error:

$$
\mathrm{RMSE}=
\sqrt{
\frac{1}{N}\sum_{i=1}^{N}(y_i-\hat y_i)^2
}
$$

Koefisien determinasi:

$$
R^2=
1-
\frac{\sum_i(y_i-\hat y_i)^2}
{\sum_i(y_i-\bar y)^2}
$$

Catatan:

- Metrik intensitas hanya bermakna jika skala dan normalisasi telah didefinisikan.
- MAE/RMSE tidak menggantikan evaluasi posisi puncak.
- \(R^2\) tidak cukup untuk menyatakan model fisika benar.
- Laporkan residual dan kesesuaian posisi puncak secara terpisah.

### 9.4 Perbandingan Posisi Puncak

Untuk puncak yang dapat dipasangkan:

$$
\Delta\tilde{\nu}_j=
\tilde{\nu}_{j,\mathrm{sim}}-
\tilde{\nu}_{j,\mathrm{exp}}
$$

Laporkan tabel:

| Mode | Puncak simulasi | Puncak aktual | Selisih | Interpretasi |
|---|---:|---:|---:|---|
| Mode 1 | ... | ... | ... | ... |
| Mode 2 | ... | ... | ... | ... |

Jangan memasangkan puncak secara sembarang. Jelaskan kriteria pencocokan, toleransi, dan kemungkinan pita yang tumpang tindih.

### 9.5 Validasi Model

Wajib dilakukan:

- Pemeriksaan satuan.
- Pemeriksaan batas frekuensi.
- Pemeriksaan nilai intensitas negatif yang tidak masuk akal untuk model intensitas.
- Pemeriksaan bahwa linewidth positif.
- Pemeriksaan parameter finite.
- Uji fungsi untuk kasus sederhana.
- Pemeriksaan konvergensi grid spektral.
- Pemeriksaan reproduksibilitas dengan seed tetap.
- Analisis residual.

### 9.6 Interpretasi Fisika

Diskusikan sumber selisih:

- Pendekatan osilator harmonik.
- Anharmonisitas.
- Interaksi antarmode.
- Lingkungan kimia dan fase sampel.
- Temperatur.
- Resolusi instrumen.
- Baseline dan noise.
- Respons spektral detektor.
- Ketidakpastian parameter vibrasi dan aktivitas Raman.

### 9.7 Keluaran Notebook 4

- Overlay data eksperimen dan simulasi.
- Residual plot.
- Tabel perbandingan puncak.
- Tabel MAE/RMSE/\(R^2\) dengan catatan normalisasi.
- Ringkasan keterbatasan model.
- Grafik final untuk dimasukkan ke makalah.

---

## 10. Pengembangan DFT (Prioritas P2, Bukan Pengganti Simulasi Wajib)

Jika dilakukan, DFT harus menjadi jalur tambahan untuk mendapatkan frekuensi vibrasi dan aktivitas Raman berbasis struktur elektronik.

Tahapan:

1. Pilih molekul dan sumber struktur.
2. Verifikasi geometri dan muatan/spin.
3. Pilih perangkat lunak, fungsional, basis set, dan parameter.
4. Lakukan optimasi geometri.
5. Pastikan struktur merupakan minimum lokal melalui pemeriksaan frekuensi imajiner.
6. Hitung frekuensi vibrasi dan aktivitas Raman jika modul mendukung.
7. Catat faktor skala frekuensi dan alasan penggunaannya.
8. Bandingkan dengan spektrum eksperimen.
9. Dokumentasikan versi perangkat lunak dan input lengkap.

Batasan:

- Hasil DFT bukan data eksperimen.
- Frekuensi harmonik umumnya memerlukan interpretasi terhadap anharmonisitas dan faktor skala.
- Pemilihan fungsional dan basis set memengaruhi hasil.
- Jangan menyajikan hasil DFT jika input, output, atau metode tidak dapat direproduksi.

Jika DFT gagal karena keterbatasan komputasi, laporkan sebagai pekerjaan yang tidak dilaksanakan dan tetap tuntaskan simulasi matematis wajib.

---

## 11. Standar Visualisasi dan Gambar

### 11.1 Notebook Acuan

Seluruh grafik harus mengikuti gaya visual notebook `PaperB_plots.ipnyb` yang diberikan pengguna. Sebelum plotting final:

1. Buka notebook acuan.
2. Identifikasi ukuran gambar, rasio aspek, jenis font, ukuran font, ketebalan garis, warna, grid, legenda, format sumbu, dan tata letak.
3. Buat konfigurasi plotting terpusat.
4. Terapkan gaya yang sama pada semua notebook.
5. Jangan menebak gaya notebook acuan jika file belum tersedia.

### 11.2 Persyaratan Plot

- Gunakan `plt.tight_layout()` sebelum penyimpanan.
- Simpan gambar minimal 300 dpi untuk raster.
- Utamakan PDF/SVG untuk grafik garis jika sesuai.
- Label sumbu harus memuat besaran dan satuan.
- Gunakan ukuran font yang terbaca.
- Hindari legenda menutupi data.
- Hindari warna yang sulit dibedakan.
- Jangan menggunakan smoothing yang mengubah posisi puncak tanpa justifikasi.
- Simpan grafik mentah dan grafik hasil preprocessing secara terpisah.

Contoh pola:

```python
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(wavenumber, intensity, linewidth=1.2, label="Spektrum")
ax.set_xlabel(r"Raman shift (cm$^{-1}$)")
ax.set_ylabel("Intensity (a.u.)")
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig("outputs/figures/raman_spectrum.png", dpi=300, bbox_inches="tight")
plt.show()
```

### 11.3 TikZ dan Gambar Aktual

TikZ digunakan untuk:

- Diagram proses hamburan.
- Diagram tingkat energi Raman.
- Diagram alur spektrometer.
- Diagram hubungan tahapan analisis.

Gambar aktual digunakan untuk:

- Foto instrumen Raman.
- Konfigurasi optik dari sumber produsen.
- Contoh perangkat spektrometer.

Setiap gambar harus memiliki atribusi. Jangan mengambil gambar tanpa memeriksa lisensi atau ketentuan penggunaan.

---

## 12. Referensi dan Standar Literatur

### 12.1 Komposisi

Target minimal 10 referensi dengan komposisi:

- 80% artikel jurnal atau publikasi ilmiah.
- 20% buku teks.

Untuk jumlah minimal 10, target praktis adalah sekurang-kurangnya 8 artikel/publikasi ilmiah dan 2 buku teks. Jika jumlah referensi bertambah, pertahankan proporsi sedekat mungkin dengan 80:20.

### 12.2 Prioritas Sumber

1. Artikel jurnal *peer-reviewed* yang relevan.
2. Artikel Q1 Scopus jika status tahun dan kategorinya terverifikasi.
3. Artikel metodologi dan dataset primer.
4. Dokumentasi resmi perangkat lunak.
5. Buku teks spektroskopi dan fisika molekul.
6. Preprint arXiv sebagai sumber pendukung, dengan status preprint dinyatakan.

### 12.3 Kandidat Referensi Awal

Daftar berikut adalah titik awal penelusuran. Metadata akhir, halaman, volume, DOI, dan status publikasi wajib diverifikasi sebelum dimasukkan ke `references.bib`.

**Artikel dan publikasi ilmiah:**

1. Raman, C. V., & Krishnan, K. S. (1928). A new type of secondary radiation. *Nature*. DOI/metadata harus diverifikasi dari arsip penerbit.
2. Albrecht, A. C. (1961). On the theory of Raman intensities. *The Journal of Chemical Physics*. Verifikasi volume, halaman, dan DOI.
3. Long, D. A. (2002). *The Raman Effect: A Unified Treatment of the Theory of Raman Scattering by Molecules*. Buku, bukan artikel; gunakan hanya jika diklasifikasikan sebagai buku.
4. Georgiev, D., Pedersen, S. V., Xie, R., Fernández-Galiana, A., Stevens, M. M., & Barahona, M. (2024 atau versi publikasi yang terverifikasi). RamanSPy: An open-source Python package for integrative Raman spectroscopy data analysis. Verifikasi metadata versi jurnal dan DOI dari PubMed/penerbit: https://pmc.ncbi.nlm.nih.gov/articles/PMC11140669/
5. Flanagan, A. R., & Glavin, F. G. (2025). Open-source Raman spectra of chemical compounds for active pharmaceutical ingredient development. *Scientific Data, 12*, 498. https://doi.org/10.1038/s41597-025-04848-6
6. Whitaker, D. A., & Hayes, K. (2018). A simple algorithm for despiking Raman spectra. Verifikasi metadata jurnal dan DOI sebelum sitasi final.
7. Artikel primer tentang Asymmetric Least Squares baseline correction. Verifikasi artikel Eilers dan metadata bibliografi sebelum penggunaan.
8. Artikel primer atau review tentang Raman selection rules dan teori grup molekul.
9. Artikel primer atau review tentang Kramers–Heisenberg–Dirac dan resonance Raman.
10. Artikel instrumentasi Raman yang menjelaskan desain spektrometer, filter, grating, dan detektor.

**Buku teks:**

11. Bernath, P. F. *Spectra of Atoms and Molecules*. Verifikasi edisi dan tahun yang digunakan.
12. Smith, E., & Dent, G. *Modern Raman Spectroscopy: A Practical Approach*. Verifikasi edisi, tahun, dan penerbit.

**Catatan:** jumlah kandidat di atas bukan berarti seluruhnya otomatis memenuhi komposisi. Pilih minimal delapan publikasi ilmiah yang telah diverifikasi dan minimal dua buku teks. Long (2002) adalah buku, bukan artikel jurnal. Jangan menghitung dokumentasi perangkat lunak sebagai artikel jurnal.

### 12.4 Audit Referensi

Untuk setiap referensi, catat:

- Penulis.
- Tahun.
- Judul.
- Jurnal/penerbit.
- Volume, nomor, halaman/artikel.
- DOI atau URL permanen.
- Jenis sumber: artikel, buku, preprint, dokumentasi.
- Status peer review.
- Status indeks dan kuartil jika relevan.
- Klaim atau bagian makalah yang didukung.

Tidak boleh menyatakan jurnal Q1 tanpa verifikasi melalui sumber indeks yang sesuai dan tahun yang relevan.

---

## 13. Integrasi LaTeX

### 13.1 Prinsip

- Ikuti template repository yang tersedia.
- Jangan mengganti kelas dokumen atau format sitasi sebelum memeriksa template.
- Pecah bab menjadi file terpisah jika struktur template mendukung.
- Gunakan `references.bib` untuk bibliografi.
- Gunakan label dan referensi silang untuk persamaan, gambar, dan tabel.
- Gunakan path gambar relatif dari direktori naskah.

### 13.2 Persamaan

Contoh persamaan utama:

```latex
\begin{equation}
\mathbf{p}_{\mathrm{ind}}(t)
=
\boldsymbol{\alpha}(t)\mathbf{E}(t).
\label{eq:induced_dipole}
\end{equation}
```

Contoh derivasi panjang:

```latex
\begin{equation}
\begin{aligned}
p_{\mathrm{ind}}(t)
={}&\alpha_0 E_0\cos(\omega_0 t)\\
&+\frac{1}{2}\alpha'_0 Q_0E_0
\cos[(\omega_0-\omega_v)t]\\
&+\frac{1}{2}\alpha'_0 Q_0E_0
\cos[(\omega_0+\omega_v)t].
\end{aligned}
\label{eq:raman_components}
\end{equation}
```

### 13.3 Integrasi Grafik

- Grafik diekspor dari notebook ke direktori gambar.
- Jangan menyunting nilai data secara manual setelah ekspor.
- Caption menjelaskan sampel, metode preprocessing, parameter penting, dan satuan.
- Setiap grafik disebutkan dalam pembahasan.
- Simpan versi final grafik beserta data sumbernya.

### 13.4 Build dan Audit

- Kompilasi sesuai toolchain template, misalnya `latexmk`, `pdflatex`/`biber`, atau konfigurasi yang telah ditentukan repository.
- Periksa referensi silang yang belum terdefinisi.
- Periksa sitasi yang tidak ditemukan.
- Periksa gambar hilang.
- Periksa overflow, persamaan terpotong, dan tabel keluar margin.
- Periksa konsistensi penomoran bab, persamaan, tabel, dan gambar.

---

## 14. Rencana Kerja dan Milestone

Urutan berikut bersifat dependency-driven. Tenggat kalender mengikuti jadwal tugas yang berlaku.

| Tahap | Pekerjaan | Keluaran | Syarat selesai |
|---|---|---|---|
| M0 | Audit repository dan template | Audit struktur | Semua file penting teridentifikasi |
| M1 | Audit sumber ilmiah | Source register dan BibTeX | Metadata dapat diverifikasi |
| M2 | Derivasi dasar Raman | Draft teori 1 | Persamaan dan asumsi benar |
| M3 | Kaidah seleksi | Draft teori 2 | Contoh molekul tervalidasi |
| M4 | Resonance Raman | Draft teori 3 | KHD dan mekanisme dijelaskan |
| M5 | Instrumentasi | Draft teori 4 | Diagram dan spesifikasi bersumber |
| M6 | Audit dataset | Notebook 1 | Data dan metadata lolos pemeriksaan |
| M7 | Preprocessing dan peak analysis | Notebook 2 | Pipeline dan parameter tercatat |
| M8 | Simulasi molekul | Notebook 3 | Spektrum dibangun dari model |
| M9 | Validasi/perbandingan | Notebook 4 | Residual dan metrik tersedia |
| M10 | Integrasi naskah | PDF kandidat | Semua bagian terintegrasi |
| M11 | Audit akhir | Laporan QA | Semua kriteria P0 lolos |

### 14.1 Pembagian Kerja

Pembagian awal yang disarankan:

- **Pradithya:** koordinasi, teori dasar, integrasi persamaan, simulasi matematis, validasi akhir.
- **Naufal:** kaidah seleksi, teori grup, resonance Raman, audit literatur.
- **Hendra:** audit dataset, preprocessing, analisis puncak, visualisasi dan dokumentasi notebook.

Semua anggota melakukan peer review. Pembagian ini dapat disesuaikan melalui kesepakatan kelompok dan dicatat di log perubahan.

---

## 15. Quality Assurance dan Kriteria Penerimaan

### 15.1 Pemeriksaan Teori

- [ ] Semua simbol didefinisikan.
- [ ] Satuan konsisten.
- [ ] Derivasi mengikuti asumsi yang dinyatakan.
- [ ] Kaidah seleksi sesuai simetri dan operator.
- [ ] Persamaan KHD diperiksa terhadap referensi primer.
- [ ] Interpretasi fisika tidak melampaui model.

### 15.2 Pemeriksaan Dataset

- [ ] Sumber dan lisensi tercatat.
- [ ] File mentah tidak diubah.
- [ ] Checksum disimpan.
- [ ] Sumbu dan unit diverifikasi.
- [ ] Label senyawa dan spektrum benar.
- [ ] Data kosong dan anomali diperiksa.
- [ ] Jumlah spektrum dan titik dihitung dari file aktual.

### 15.3 Pemeriksaan Notebook

- [ ] Semua import berada di awal.
- [ ] Semua bagian kode memiliki penjelasan Markdown.
- [ ] Notebook berjalan dari kernel bersih.
- [ ] Tidak ada variabel tersembunyi.
- [ ] Parameter disimpan.
- [ ] Grafik memiliki unit dan label.
- [ ] `plt.tight_layout()` digunakan.
- [ ] Keluaran disimpan pada direktori yang ditetapkan.
- [ ] Tidak ada data simulasi yang dilabeli sebagai eksperimen.

### 15.4 Pemeriksaan Simulasi

- [ ] Model dimulai dari persamaan fisika.
- [ ] Parameter memiliki sumber atau label asumsi.
- [ ] Konversi satuan benar.
- [ ] Posisi Stokes dan anti-Stokes benar.
- [ ] Linewidth positif.
- [ ] Intensitas sesuai definisi model.
- [ ] Seed noise tetap.
- [ ] Uji sensitivitas dilakukan.
- [ ] Perbandingan dengan eksperimen tidak dipaksakan.
- [ ] Keterbatasan model dinyatakan.

### 15.5 Pemeriksaan Referensi

- [ ] Minimal 10 referensi.
- [ ] Target 80% artikel/publikasi dan 20% buku.
- [ ] Metadata diverifikasi.
- [ ] DOI/URL berfungsi.
- [ ] Status Q1 tidak diklaim tanpa bukti.
- [ ] Preprint diberi label.
- [ ] Semua sitasi di teks terdapat dalam bibliografi dan sebaliknya.

### 15.6 Pemeriksaan PDF

- [ ] PDF berhasil dibangun.
- [ ] Tidak ada persamaan terpotong.
- [ ] Tidak ada gambar hilang.
- [ ] Tidak ada tabel keluar halaman.
- [ ] Tidak ada referensi silang rusak.
- [ ] Grafik terbaca.
- [ ] Batas halaman dipatuhi jika berlaku.
- [ ] Format sesuai template repository.

### 15.7 Kriteria Keberhasilan Akhir

Proyek dinyatakan memenuhi target utama apabila seluruh P0 selesai. P1 memperkuat kualitas, sedangkan P2 merupakan pengembangan tambahan. Tidak boleh menandai proyek selesai hanya karena PDF berhasil dikompilasi apabila notebook atau simulasi belum dapat direproduksi.

---

## 16. Scope Control dan Keputusan Jika Terjadi Kendala

| Kondisi | Tindakan |
|---|---|
| Dataset tidak dapat diunduh | Periksa tautan resmi dan format alternatif yang disediakan artikel; catat kegagalan |
| Metadata instrumen tidak tersedia | Jangan mengarang; batasi interpretasi dan nyatakan keterbatasan |
| RamanSPy tidak kompatibel | Catat versi dan gunakan implementasi SciPy yang tervalidasi |
| Preprocessing mengubah bentuk puncak | Bandingkan pipeline, kurangi smoothing, dan dokumentasikan |
| Parameter vibrasi tidak ditemukan | Gunakan sumber lain yang dapat diverifikasi atau model ilustratif yang diberi label |
| DFT tidak dapat dijalankan | Selesaikan model matematis wajib; DFT dicatat tidak dilaksanakan |
| Waktu terbatas | Hentikan P2, pertahankan P0 |
| Naskah terlalu panjang | Ringkas pembahasan sekunder tanpa menghapus derivasi inti |
| Notebook gagal dijalankan ulang | Perbaiki dependensi, path, urutan sel, dan variabel tersembunyi sebelum integrasi |

Semua keputusan harus dicatat di `logs/change_log.md` atau `logs/validation_log.md`.

---

## 17. Ketentuan Privasi, Data, dan Reproduksibilitas

- Data, rancangan, analisis, dan hasil kerja kelompok diperlakukan sebagai materi kerja privat.
- Dataset publik tetap harus mengikuti lisensi dan atribusi pemiliknya.
- Jangan mengunggah data internal atau berkas yang tidak diizinkan ke layanan eksternal.
- Repository tidak boleh dibuat publik atau diubah pengaturan aksesnya tanpa keputusan pemilik.
- Simpan sumber data, parameter, versi perangkat lunak, dan checksum agar analisis dapat direproduksi.
- Jangan menghapus file sumber atau data mentah setelah preprocessing.
- Jangan melakukan push atau merge tanpa persetujuan eksplisit.

---

## 18. Daftar Periksa Final

### A. Repository dan Lingkungan

- [ ] Repository telah diaudit.
- [ ] Struktur aktual dipertahankan atau perubahan terdokumentasi.
- [ ] Lingkungan Python tercatat.
- [ ] `.gitignore` mengabaikan cache dan lingkungan virtual.
- [ ] Tidak ada push/merge tanpa persetujuan.

### B. Teori

- [ ] Dasar hamburan Raman.
- [ ] Derivasi klasik momen dipol.
- [ ] Pendekatan kuantum.
- [ ] Kaidah seleksi vibrasi.
- [ ] Kaidah seleksi rotasi.
- [ ] Teori grup CO₂ dan H₂O.
- [ ] Resonance Raman dan KHD.
- [ ] Instrumentasi nyata dan diagram.

### C. Dataset dan Analisis

- [ ] Dataset resmi telah diunduh.
- [ ] Lisensi dan metadata dicatat.
- [ ] Data mentah diperiksa.
- [ ] Preprocessing dijelaskan dan diuji.
- [ ] Puncak dan FWHM dianalisis.
- [ ] Interpretasi didukung sumber.

### D. Simulasi

- [ ] Model osilator harmonik.
- [ ] Parameter vibrasi.
- [ ] Turunan polarizabilitas/aktivitas Raman.
- [ ] Posisi Stokes dan anti-Stokes.
- [ ] Profil garis.
- [ ] Spektrum multi-mode.
- [ ] Variasi temperatur, linewidth, dan laser.
- [ ] Noise dan baseline sintetis bila digunakan.
- [ ] Perbandingan dengan spektrum aktual.
- [ ] Residual dan metrik evaluasi.
- [ ] Keterbatasan model.

### E. Naskah dan Presentasi Ilmiah

- [ ] LaTeX mengikuti template.
- [ ] Referensi minimal 10 dan proporsinya sesuai.
- [ ] Grafik berasal dari notebook.
- [ ] Gambar dan tabel memiliki sumber/caption.
- [ ] PDF lolos audit.
- [ ] Kesimpulan menjawab tujuan dan tidak melampaui bukti.

---

## 19. Definisi Selesai (*Definition of Done*)

Proyek dinyatakan selesai apabila:

1. Empat topik utama telah dibahas secara mendalam.
2. Derivasi matematis utama benar dan dapat ditelusuri.
3. Dataset Raman aktual telah dibaca dan diaudit.
4. Spektrum aktual telah diproses dan dianalisis.
5. Simulasi matematis molekul telah dibangun dari persamaan hingga spektrum.
6. Hasil simulasi dibandingkan dengan data aktual secara kritis.
7. Seluruh notebook berjalan dari awal hingga akhir.
8. Grafik dan tabel dapat dihasilkan ulang.
9. Referensi dan metadata dapat diverifikasi.
10. Naskah LaTeX berhasil dikompilasi dan sesuai template.
11. Keterbatasan, asumsi, dan sumber ketidakpastian dijelaskan.
12. Tidak ada perubahan Git jarak jauh tanpa persetujuan.

---

## 20. Sumber Utama dan Dokumentasi

### Sumber proyek dan perangkat lunak

- Repository proyek: https://github.com/xysilverberg/raman-spectroscopy-project.git
- RamanSPy documentation: https://ramanspy.readthedocs.io/en/latest/
- RamanSPy preprocessing: https://ramanspy.readthedocs.io/en/latest/preprocessing.html
- RamanSPy overview: https://ramanspy.readthedocs.io/en/stable/overview.html
- RamanSPy preprocessing examples: https://ramanspy.readthedocs.io/en/stable/auto_examples/plot_i_preprocessing_pipelines.html
- RamanSPy paper: https://pmc.ncbi.nlm.nih.gov/articles/PMC11140669/

### Dataset utama

- Flanagan & Glavin (2025), Scientific Data: https://www.nature.com/articles/s41597-025-04848-6
- DOI: https://doi.org/10.1038/s41597-025-04848-6
- PubMed record: https://pubmed.ncbi.nlm.nih.gov/40128276/

### Berkas acuan internal proyek

- `PaperB_plots.ipnyb`: acuan gaya visualisasi; periksa file asli sebelum menetapkan konfigurasi plot.
- Template LaTeX yang tersedia di repository: wajib menjadi acuan format final.
- Berkas ketentuan tugas yang diberikan pengguna: wajib diutamakan jika terdapat perbedaan dengan spesifikasi umum dalam PRD ini.

---

## 21. Instruksi Eksekusi untuk Pelaksana

Laksanakan proyek secara berurutan dan berbasis bukti. Jangan langsung menulis seluruh kode atau mengubah repository sebelum audit awal. Setelah audit, kerjakan teori, dataset, analisis, dan simulasi dalam unit yang dapat diuji. Setiap notebook harus memiliki penjelasan Markdown sebelum blok kode, seluruh hasil penting harus disimpan, dan setiap keputusan parameter harus dicatat.

**Urutan wajib:** audit repository → verifikasi template dan sumber → derivasi teori → audit dataset → preprocessing → analisis puncak → simulasi matematis → validasi dan perbandingan → integrasi LaTeX → audit final.

Jangan menganggap pekerjaan selesai hanya karena kode berhasil dijalankan satu kali. Lakukan *Restart & Run All*, periksa kembali keluaran, verifikasi gambar, kompilasi PDF, dan cocokkan klaim dalam naskah dengan data yang benar-benar dihasilkan.

**Larangan utama:** jangan mengarang data, spesifikasi instrumen, metadata, DOI, status Q1, hasil simulasi, atau kesesuaian model. Jika suatu informasi tidak tersedia, tandai sebagai tidak tersedia dan jelaskan konsekuensinya terhadap analisis.
