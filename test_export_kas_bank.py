import sys, os, json
sys.path.append('C:/Users/USER/Documents/ARKASu Data')
import app
from io import BytesIO

data = app.get_kas_bank(tahun=2026, bulan=1)
print('Data rows:', len(data))
if data:
    headers = ['Tanggal', 'Uraian', 'Saldo', 'Status', 'No. Bukti']
    output = app.export_to_excel(data, headers, 'test.xlsx', title='Test')
    # Write to file for inspection
    with open('C:/Users/USER/Documents/ARKASu Data/kas_bank_test.xlsx','wb') as f:
        f.write(output.read())
    print('File written')
else:
    print('No data')
