# Spesifikasi dan Sumber Teknis Instrumentasi Spektrometer Raman

Dokumen ini mendokumentasikan spesifikasi teknis dan rujukan pabrikan/literatur instrumen spektrometer mikro-Raman confocal yang menjadi acuan pemodelan pada Bab 5 dan eksperimen pada Bab 6.

### 1. Model Acuan Spektrometer
- **Model:** Horiba Jobin Yvon LabRAM HR Evolution Confocal Micro-Raman Spectrometer
- **Tipe Konfigurasi:** Confocal upright microscope coupling dengan spectrometer Czerny-Turner fokal panjang (focal length $f = 800\text{ mm}$).
- **Dokumentasi Sumber:** Horiba Scientific Technical Application Note & User Manual (LabRAM HR Series); Smith & Dent (2019), Bab 3.

### 2. Sumber Eksitasi Laser
- **Laser Utama:** Diode-Pumped Solid-State (DPSS) Laser kontinu ($\text{CW}$), $\lambda_0 = 532.0\text{ nm}$ ($E_L = 2.3305\text{ eV}$).
- **Stabilitas Panjang Gelombang:** $< 0.005\text{ nm}$ drift jangka panjang.
- **Daya pada Sampel:** Dibatasi pada $0.5 - 2.0\text{ mW}$ melalui filter densitas netral (Neutral Density / ND filter) untuk mencegah laser heating, dekomposisi termal, atau pergeseran posisi puncak akibat ekspansi kisi grafena.

### 3. Optik Pengarah dan Penolak Hamburan Elastik Rayleigh
- **Objektif Mikroskop:** Olympus BX41 confocal coupling, pembesaran 100x, Numerical Aperture (NA) = 0.90, working distance $0.21\text{ mm}$. Ukuran berkas fokus (spot size): $d_{\text{spot}} \approx 1.22 \lambda / \text{NA} \approx 0.72\text{ \mu m}$.
- **Pemisah Berkas (Beam Splitter):** Dichroic edge beam splitter.
- **Filter Penolak Rayleigh:** Edge filter bertingkat tinggi (optical density $\text{OD} > 6$ pada $532\text{ nm}$), dengan cut-off edge $\le 50\text{ cm}^{-1}$ dari garis laser Rayleigh.

### 4. Sistem Monokromator / Spektrograf
- **Desain Optik:** Konfigurasi Czerny-Turner asimetris teroptimasi koma dan aberasi speris ($f = 800\text{ mm}$).
- **Kisi Difraksi (Diffraction Grating):**
  - Kerapatan alur: $1800\text{ grooves/mm}$ ($d = 10^6 / 1800 \approx 555.56\text{ nm}$).
  - Sudut blaze dioptimalkan pada wilayah tampak ($500\text{ nm}$).
  - Persamaan kisi: $m\lambda = d(\sin\theta_i + \sin\theta_d)$, di mana $m=1$ pada moda transmisi standar.
- **Resolusi Spektral:** $\le 0.5\text{ cm}^{-1}/\text{pixel}$ pada rentang sidik jari grafena.
- **Celah Konfokal (Confocal Pinhole):** Aperture variabel $50 - 100\text{ \mu m}$ untuk menjamin resolusi spasial aksial ($z \le 1.5\text{ \mu m}$) dan resolusi lateral ($x, y \le 1.0\text{ \mu m}$).

### 5. Detektor Spektral
- **Tipe Detektor:** Synapse Open-Electrode Charge-Coupled Device (CCD) Array.
- **Ukuran Matriks Sensor:** $1024 \times 256\text{ pixels}$, ukuran piksel $26\text{ \mu m} \times 26\text{ \mu m}$.
- **Pendinginan:** Pendingin termoelektrik (Peltier) tertutup hingga temperatur operasi $-70^\circ\text{C}$ untuk meminimalkan arus gelap (dark current $< 0.002\text{ e}^-/\text{pixel/s}$).
- **Noise Pembacaan (Readout Noise):** $< 5\text{ e}^-\text{ rms}$ pada kecepatan pembacaan $20\text{ kHz}$.

### 6. Kalibrasi Sumbu Spektral
- **Standar Kalibrasi Primer:** Kristal tunggal Silikon monokristalin $\text{Si}(100)$ dengan garis fonon optik terstandarisasi pada $520.7\text{ cm}^{-1}$.
- **Toleransi Kalibrasi:** Maksimum simpangan pergeseran $\le 0.2\text{ cm}^{-1}$.
