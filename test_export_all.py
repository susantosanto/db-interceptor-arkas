import sys, os, json
sys.path.append('C:/Users/USER/Documents/ARKASu Data')
import app

from io import BytesIO

print("=== Testing all Kas exports for 2026 ===")

# Test each export
tests = [
    ('kas_umum', lambda: app.get_kas_umum(tahun=2026, bulan=1)),
    ('kas_bank', lambda: app.get_kas_bank(tahun=2026, bulan=1)),
    ('kas_pajak', lambda: app.get_kas_pajak(tahun=2026, bulan=1)),
    ('kas_tunai', lambda: app.get_kas_tunai(tahun=2026, bulan=1)),
]

headers = ['Tanggal', 'Uraian', 'Saldo', 'No. Bukti']

for name, func in tests:
    try:
        data = func()
        print(f'{name}: {len(data)} rows')
        
        if len(data) > 0:
            # Create Excel file
            output = app.export_to_excel(data, headers, f'{name}.xlsx', title=f'Test {name}')
            filepath = f'C:/Users/USER/Documents/ARKASu Data/{name}_export.xlsx'
            with open(filepath, 'wb') as f:
                f.write(output.getvalue())
            print(f'  -> Written to {filepath}')
    except Exception as e:
        print(f'{name}: ERROR - {e}')

print("\nDone!")