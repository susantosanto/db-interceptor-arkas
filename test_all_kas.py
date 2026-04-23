import sys, os, json
sys.path.append('C:/Users/USER/Documents/ARKASu Data')
import app

print("=== Testing all Kas functions for 2026 ===")

df = app.get_kas_umum(tahun=2026, bulan=1)
print(f'get_kas_umum: {len(df)} rows')

df = app.get_kas_bank(tahun=2026, bulan=1)
print(f'get_kas_bank: {len(df)} rows')

df = app.get_kas_pajak(tahun=2026, bulan=1)
print(f'get_kas_pajak: {len(df)} rows')

df = app.get_kas_tunai(tahun=2026, bulan=1)
print(f'get_kas_tunai: {len(df)} rows')
