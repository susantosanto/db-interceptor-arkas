import sys, os, json
sys.path.append('C:/Users/USER/Documents/ARKASu Data')
import app

print("=== VERIFIKASI SEMUA LAPORAN ===\n")

reports = [
    ("BKU (Buku Kas Umun)", lambda: app.get_kas_umum(tahun=2026)),
    ("Kas Bank", lambda: app.get_kas_bank(tahun=2026)),
    ("Kas Pajak", lambda: app.get_kas_pajak(tahun=2026)),
    ("Kas Tunai", lambda: app.get_kas_tunai(tahun=2026)),
    ("Kertas Kerja", lambda: app.get_kertas_kerja(tahun=2026)),
    ("RKAS", lambda: app.get_rkas(tahun=2026)),
    ("Realisasi", lambda: app.get_realisasi(tahun=2026)),
    ("BHP (Barang Habis Pakai)", lambda: app.get_realisasi_barang_habis(tahun=2026)),
    ("Modal (Barang Modal)", lambda: app.get_realisasi_barang_modal(tahun=2026)),
    ("BP Objek (Rincian Objek)", lambda: app.get_buku_pembantu_objek(tahun=2026)),
    ("BOSP", lambda: app.get_laporan_bosp(tahun=2026)),
]

for name, func in reports:
    try:
        data = func()
        print(f"{name}: {len(data)} baris")
        if len(data) > 0:
            # Show first 2 rows
            print(f"  Contoh: {data[0][:3]}...")
    except Exception as e:
        print(f"{name}: ERROR - {e}")

print("\n=== CEK Masing-masing kolom ===\n")

# Check headers for each report group
print("--- KAS (4 kolom) ---")
data = app.get_kas_umum(tahun=2026)
if data:
    print(f"  Kode Rekening: {data[0][0]}")
    print(f"  Uraian: {data[0][1]}")

print("--- KK/RKAS (5 kolom) ---")
data = app.get_kertas_kerja(tahun=2026)
if data:
    print(f"  Kode Rekening: {data[0][0]}")
    print(f"  Uraian: {data[0][1]}")
    print(f"  Volume: {data[0][2]}")
    print(f"  Satuan: {data[0][3]}")
    print(f"  Jumlah: {data[0][4]}")

print("--- Realisasi (5 kolom) ---")
data = app.get_realisasi(tahun=2026)
if data:
    print(f"  Kolom: {data[0]}")

print("--- BHP (5 kolom) ---")
data = app.get_realisasi_barang_habis(tahun=2026)
if data:
    print(f"  Kode: {data[0][0]}")
    print(f"  Uraian: {data[0][1]}")
    print(f"  Volume: {data[0][2]}")
    print(f"  Satuan: {data[0][3]}")
    print(f"  Jumlah: {data[0][4]}")

print("--- Modal (5 kolom) ---")
data = app.get_realisasi_barang_modal(tahun=2026)
if data:
    print(f"  Kode: {data[0][0]}")
    print(f"  Uraian: {data[0][1]}")
    print(f"  Volume: {data[0][2]}")
    print(f"  Satuan: {data[0][3]}")
    print(f"  Jumlah: {data[0][4]}")

print("--- BP Objek (5 kolom) ---")
data = app.get_buku_pembantu_objek(tahun=2026)
if data:
    print(f"  Kode: {data[0][0]}")
    print(f"  Uraian: {data[0][1]}")
    print(f"  Volume total: {data[0][2]}")
    print(f"  Satuan: {data[0][3]}")
    print(f"  Jumlah total: {data[0][4]}")

print("\n=== DONE ===")