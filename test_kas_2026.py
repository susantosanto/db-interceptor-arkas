import sys, os, json
sys.path.append('C:/Users/USER/Documents/ARKASu Data')
import app

df = app.get_kas_bank(tahun=2026, bulan=1)
print('Rows:', len(df))
print(df.head())
