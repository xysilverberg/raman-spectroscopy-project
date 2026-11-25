# Proyek Kelompok Spektroskopi Raman

Repositori kolaborasi proyek kelompok (3 orang) mata kuliah **Spektroskopi** (Semester 5) mengenai **Spektroskopi Raman**.

Dokumen soal/instruksi asli tersedia pada [PROYEK KELOMPOK.pdf](./PROYEK%20KELOMPOK.pdf).

---

## Ruang Lingkup Materi

Makalah ilmiah ini membahas empat topik utama:

1. **Teori Dasar Hamburan dan Spektroskopi Raman**
   - Hamburan elastis (Rayleigh) vs inelastis (Stokes & Anti-Stokes)
   - Pendekatan klasik (polarisabilitas) dan kuantum (tingkat energi vibrasi/rotasi & keadaan virtual)
2. **Perhitungan Kaidah Seleksi**
   - Kaidah seleksi vibrasi dan rotasi Raman ($\Delta v = \pm 1$, $\Delta J = 0, \pm 2$)
   - Analisis simetri / teori grup (tabel karakter, representasi tereduksi & tak tereduksi, aktivitas IR vs Raman)
3. **Teori Raman Resonansi**
   - Mekanisme *Resonance Raman Scattering* (eksitasi mendekati transisi elektronik)
   - Peningkatan intensitas, aturan pemilihan khusus (mekanisme Franck-Condon / Herzberg-Teller), serta aplikasinya
4. **Perangkat Spektrometer Raman**
   - Sumber laser, optik pengumpul, filter penolak garis Rayleigh (*notch/edge filter*), monokromator/spektrograf, dan detektor (CCD)
   - Konfigurasi umum (FT-Raman, Konfokal / Mikro-Raman, SERS)

---

## Ketentuan Tugas

- **Jumlah Anggota:** 3 orang per kelompok
- **Ukuran Font:** 12 pt
- **Format:** Mengikuti standar makalah ilmiah
- **Panjang Maksimum:** 20 halaman
- **Batas Pengumpulan:** 14 Desember 2026 pukul 15.00

---

## Struktur Repositori

```text
.
├── PROYEK KELOMPOK.pdf          # Instruksi resmi proyek kelompok
├── README.md                    # Dokumentasi utama proyek
├── CONTRIBUTING.md              # Panduan alur kerja Git & kolaborasi kelompok
├── .gitignore                   # Daftar file sementara yang diabaikan Git
├── paper/
│   ├── latex/                   # Draft makalah versi LaTeX (modular per bagian)
│   │   ├── main.tex             # Dokumen utama (12pt, standar artikel ilmiah)
│   │   ├── references.bib       # Daftar pustaka BibTeX
│   │   └── sections/            # File per bab/topik agar mudah dikerjakan paralel
│   │       ├── 01_teori_dasar.tex
│   │       ├── 02_kaidah_seleksi.tex
│   │       ├── 03_raman_resonansi.tex
│   │       └── 04_spektrometer_raman.tex
│   └── docx/                    # Alternatif / final draft dalam format Word (.docx)
├── scripts/                     # Skrip Python untuk simulasi spektrum atau plotting grafik
│   ├── README.md
│   └── requirements.txt
├── figures/                     # Gambar diagram skema, spektrum, dan ilustrasi
└── references/                  # Jurnal, buku, atau artikel referensi (PDF)
```

---

## Pembagian Tugas Kelompok

| Anggota | Username GitHub | Bagian Tanggung Jawab | Status |
| :--- | :--- | :--- | :--- |
| Anggota 1 | `@xysilverberg` | *Isi bagian & koordinasi* | In Progress |
| Anggota 2 | `@username-teman-1` | *Isi bagian* | Pending |
| Anggota 3 | `@username-teman-2` | *Isi bagian* | Pending |

---

## Cara Mulai Kolaborasi

Lihat panduan lengkap di [CONTRIBUTING.md](./CONTRIBUTING.md) untuk cara clone repositori, membuat branch per bagian, dan melakukan pull request agar tidak terjadi konflik file.
