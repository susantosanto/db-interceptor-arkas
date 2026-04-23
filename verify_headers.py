import sys, os, json
sys.path.append('C:/Users/USER/Documents/ARKASu Data')
import app

print("=== VERIFIKASI KOLOM DAN DATA ===\n")

# Define expected header count per report (based on current app.py)
reports = [
    ("BKU", lambda: app.get_kas_umum(tahun=2026), ['Tanggal', 'Uraian', 'Saldo', 'No. Bukti'], 4),
    ("Kas Bank", lambda: app.get_kas_bank(tahun=2026), ['Tanggal', 'Uraian', 'Saldo', 'No. Bukti'], 4),
    ("Kas Pajak", lambda: app.get_kas_pajak(tahun=2026), ['Tanggal', 'Uraian', 'Saldo', 'No. Bukti'], 4),
    ("Kas Tunai", lambda: app.get_kas_tunai(tahun=2026), ['Tanggal', 'Uraian', 'Saldo', 'No. Bukti'], 4),
    ("Kertas Kerja", lambda: app.get_kertas_kerja(tahun=2026), ['Kode Rekening', 'Uraian', 'Volume', 'Satuan', 'Jumlah'], 5),
    ("RKAS", lambda: app.get_rkas(tahun=2026), ['Kode Rekening', 'Uraian', 'Volume', 'Satuan', 'Jumlah'], 5),
    ("Realisasi", lambda: app.get_realisasi(tahun=2026), ['ID Anggaran', 'Tahun', 'Jumlah', 'Sisa', 'Status'], 5),
    ("BHP", lambda: app.get_realisasi_barang_habis(tahun=2026), ['Kode Rekening', 'Uraian', 'Volume', 'Satuan', 'Jumlah'], 5),
    ("Modal", lambda: app.get_realisasi_barang_modal(tahun=2026), ['Kode Rekening', 'Uraian', 'Volume', 'Satuan', 'Jumlah'], 5),
    ("BP Objek", lambda: app.get_buku_pembantu_objek(tahun=2026), ['Kode Rekening', 'Uraian', 'Volume Total', 'Satuan', 'Jumlah Total'], 5),
    ("BOSP", lambda: app.get_laporan_bosp(tahun=2026), ['ID Anggaran', 'Tahun', 'Jumlah', 'Sisa', 'Status'], 5),
]

all_ok = True
for name, func, expected_headers, expected_cols in reports:
    try:
        data = func()
        actual_cols = len(data[0]) if data else 0
        status = "✅" if actual_cols == expected_cols else "❌"
        print(f"{status} {name}: {len(data)} baris, {actual_cols} kolom (esperado: {expected_cols})")
        if actual_cols != expected_cols:
            print(f"   Contoh data: {data[0] if data else 'TIDAK ADA'}")
            all_ok = False
    except Exception as e:
        print(f"❌ {name}: ERROR - {e}")
        all_ok = False

print(f"\n{'='*40}")
if all_ok:
    print("✅ SEMUA KOLOM SESUAI!")
else:
    print("❌ ADA KOLOM YANG TIDAK SESUAI")
print(f"{'='*40}")