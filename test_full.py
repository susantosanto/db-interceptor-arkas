import sys, os, json
sys.path.append('C:/Users/USER/Documents/ARKASu Data')
import app

print("=== TEST ALL REPORTS for 2026 ===\n")

tests = [
    ("1. BKU (Buku Kas Umum)", lambda: app.get_kas_umum(tahun=2026)),
    ("2. Kas Bank", lambda: app.get_kas_bank(tahun=2026)),
    ("3. Kas Pajak", lambda: app.get_kas_pajak(tahun=2026)),
    ("4. Kas Tunai", lambda: app.get_kas_tunai(tahun=2026)),
    ("5. Kertas Kerja", lambda: app.get_kertas_kerja(tahun=2026)),
    ("6. RKAS", lambda: app.get_rkas(tahun=2026)),
    ("7. Realisasi", lambda: app.get_realisasi(tahun=2026)),
    ("8. BHP", lambda: app.get_realisasi_barang_habis(tahun=2026)),
    ("9. Modal", lambda: app.get_realisasi_barang_modal(tahun=2026)),
    ("10. BP Objek", lambda: app.get_buku_pembantu_objek(tahun=2026)),
    ("11. BOSP", lambda: app.get_laporan_bosp(tahun=2026)),
]

for name, func in tests:
    try:
        data = func()
        print(f"\n{name}")
        print(f"  Rows: {len(data)}")
        if data:
            print(f"  Columns: {len(data[0])}")
            print(f"  Sample row: {data[0]}")
        else:
            print(f"  ❌ TIDAK ADA DATA")
    except Exception as e:
        print(f"  ❌ ERROR: {e}")

print("\n=== END ===")