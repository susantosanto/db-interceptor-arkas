# 📊 ARKASu Data

Aplikasi Tarik Data ARKAS ke Excel

## 📋 Fitur

- **Dashboard** - Ringkasan data sekolah
- **Export RAPBS** - Data Rencana Anggaran Pendapatan dan Belanja Sekolah
- **Export Kas Umum** - Transaksi keuangan
- **Export PTK** - Daftar Guru dan Tendik
- **Export Siswa** - Data Peserta Didik

## 🚀 Cara Install

### 1. Install Python

Download dari: https://www.python.org/downloads/

> ⚠️ Pastikan centang **"Add Python to PATH"** saat install

### 2. Install Dependencies

```bash
cd C:\Users\USER\Documents\ARKASu Data
pip install -r requirements.txt
```

### 3. Setup Database

Pastikan file `config.json` sudah sesuai dengan lokasi database ARKAS Anda.

## ▶️ Cara Jalankan

```bash
python app.py
```

Buka browser: **http://localhost:5000**

## 📁 Struktur Project

```
ARKASu Data/
├── app.py              # Main application
├── config.json         # Konfigurasi database
├── requirements.txt   # Python dependencies
├── README.md          # Dokumentasi
└── templates/
    └── index.html     # Frontend HTML
```

---

**Author:** Operator SD Negeri Pasirhalang
**Version:** 1.0