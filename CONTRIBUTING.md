# Panduan Kolaborasi Kelompok

Dokumen ini menjelaskan alur kerja Git sederhana agar seluruh anggota kelompok (3 orang) dapat mengerjakan makalah, simulasi, dan pengumpulan referensi secara bersamaan tanpa menimpa pekerjaan satu sama lain.

---

## 1. Persiapan Awal (Untuk Anggota yang Diundang)

1. Terima undangan kolaborator melalui email atau notifikasi GitHub.
2. Clone repositori ke komputer masing-masing:
   ```bash
   git clone https://github.com/xysilverberg/raman-spectroscopy-project.git
   cd raman-spectroscopy-project
   ```

---

## 2. Alur Kerja Harian (Branching Sederhana)

Agar tidak bentrok saat mengedit bagian masing-masing:

1. **Selalu tarik pembaruan terbaru dari `main` sebelum mulai:**
   ```bash
   git checkout main
   git pull origin main
   ```
2. **Buat branch sesuai topik atau nama masing-masing:**
   ```bash
   git checkout -b feat/kaidah-seleksi
   ```
3. **Kerjakan perubahan di folder yang sesuai:**
   - Penulisan LaTeX: edit file masing-masing di `paper/latex/sections/`
   - Penulisan Word: simpan dengan penamaan jelas di `paper/docx/` (mis. `draft_bagian2_kaidah_seleksi.docx`)
   - Gambar/diagram: simpan di `figures/` dengan nama deskriptif (mis. `skema_spektrometer_raman.png`)
   - Skrip simulasi/plot: simpan di `scripts/`
   - Pustaka/referensi: simpan PDF di `references/` dan catat sitasi di `paper/latex/references.bib`
4. **Commit dengan pesan yang jelas:**
   ```bash
   git add .
   git commit -m "docs(kaidah-seleksi): tambah penurunan kaidah seleksi vibrasi"
   ```
5. **Push branch dan buat Pull Request (PR) di GitHub:**
   ```bash
   git push -u origin feat/kaidah-seleksi
   ```
   Setelah di-push, buka repositori di GitHub dan klik **Compare & pull request** untuk digabungkan ke `main`.

---

## 3. Tips Menghindari Konflik

- Jangan mengedit file `.tex` milik bagian anggota lain kecuali untuk penyelarasan akhir.
- Hindari meng-commit file hasil kompilasi sementara (`*.aux`, `*.log`, `~$*.docx`); file-file ini sudah otomatis diabaikan oleh `.gitignore`.
- Untuk file biner (`.docx`, `.pdf`, `.png`), usahakan tidak diedit oleh dua orang secara bersamaan di waktu yang sama.
