import sys, os, json
sys.path.append('C:/Users/USER/Documents/ARKASu Data')
import app

from io import BytesIO

print("=== Testing ALL Reports for 2026 ===\n")

# Test all report functions
tests = [
    # Kas reports
    ('kas_umum', lambda: app.get_kas_umum(tahun=2026, bulan=1)),
    ('kas_bank', lambda: app.get_kas_bank(tahun=2026, bulan=1)),
    ('kas_pajak', lambda: app.get_kas_pajak(tahun=2026, bulan=1)),
    ('kas_tunai', lambda: app.get_kas_tunai(tahun=2026, bulan=1)),
    # KK
    ('kertas_kerja', lambda: app.get_kertas_kerja(tahun=2026)),
    ('kk_tahunan', lambda: app.get_kertas_kerja(tahun=2026)),
    ('kk_tahapan', lambda: app.get_kertas_kerja(tahun=2026, tahapan=1)),
    ('kk_bulanan', lambda: app.get_kertas_kerja(tahun=2026, bulan=1)),
    # RKAS
    ('rkas', lambda: app.get_rkas(tahun=2026)),
    ('rkas_tahapan', lambda: app.get_rkas(tahun=2026, tahapan=1)),
    # Realisasi
    ('realisasi', lambda: app.get_realisasi(tahun=2026, bulan=1)),
    ('realisasi_tahapan', lambda: app.get_realisasi(tahun=2026, tahapan=1)),
    ('realisasi_bhp', lambda: app.get_realisasi_barang_habis(tahun=2026, bulan=1)),
    ('realisasi_modal', lambda: app.get_realisasi_barang_modal(tahun=2026, bulan=1)),
    # BP Objek
    ('bpobjek', lambda: app.get_buku_pembantu_objek(tahun=2026, bulan=1)),
    # BOSP
    ('bosp', lambda: app.get_laporan_bosp(tahun=2026, semester=1)),
]

headers_simple = ['Tanggal', 'Uraian', 'Saldo', 'No. Bukti']

for name, func in tests:
    try:
        data = func()
        print(f'{name}: {len(data)} rows')
    except Exception as e:
        print(f'{name}: ERROR - {e}')

print("\nDone!")