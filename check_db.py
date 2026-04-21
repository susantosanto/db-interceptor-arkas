"""Cek struktur database ARKAS"""
import sqlcipher3
import json

# Load config
config_path = r"C:\Users\USER\.config\opencode\arkas_config.json"
with open(config_path, 'r') as f:
    config = json.load(f)

db_path = config['arkas']['db_path']
key = config['arkas']['key']

print(f'DB Path: {db_path}')
print(f'Key: {key}')

# Connect
db = sqlcipher3.connect(db_path)
db.execute(f"PRAGMA key = '{key}'")
db.execute("PRAGMA cipher_compatibility = 4")

# Get tables
cursor = db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name")
tables = cursor.fetchall()
print(f'\n=== TABLES ({len(tables)}) ===')
for t in tables:
    print(f'  - {t[0]}')

# Get sample data from kas_umum
print('\n=== Sample kas_umum (5 rows) ===')
cursor = db.execute('SELECT COUNT(*) FROM kas_umum')
count = cursor.fetchone()[0]
print(f'  Total rows: {count}')

if count > 0:
    # Get schema
    cursor = db.execute('PRAGMA table_info(kas_umum)')
    cols = cursor.fetchall()
    print('  Schema:')
    for c in cols:
        print(f'    {c[1]} ({c[2]})')
    
    # Get sample data
    cursor = db.execute('SELECT tanggal_transaksi, uraian, saldo, status_bku, no_bukti FROM kas_umum ORDER BY tanggal_transaksi DESC LIMIT 5')
    rows = cursor.fetchall()
    print('  Sample data (newest first):')
    for r in rows:
        print(f'    {r}')
else:
    print('  No data!')

# Get table structure
print('\n=== kas_umum schema ===')
cursor = db.execute('PRAGMA table_info(kas_umum)')
cols = cursor.fetchall()
for c in cols:
    print(f'  {c}')

# Get format tanggal
print('\n=== Sample tanggal format ===')
cursor = db.execute('SELECT typeof(tanggal), tanggal FROM kas_umum LIMIT 3')
rows = cursor.fetchall()
for r in rows:
    print(f'  type: {r[0]}, value: {r[1]}')

# Check tables for kas pembantu
print('\n=== Check kas_pembantu tables ===')
tables_to_check = ['kas_pembantu_bank', 'kas_pembantu_pajak', 'kas_pembantu_tunai', 'rpt_bku', 'report_bku']
for t in tables_to_check:
    try:
        cursor = db.execute(f'SELECT COUNT(*) FROM {t}')
        count = cursor.fetchone()[0]
        print(f'  {t}: {count} rows')
    except Exception as e:
        print(f'  {t}: TIDAK ADA')

# Check rpt_bku schema
print('\n=== rpt_bku schema ===')
cursor = db.execute('PRAGMA table_info(rpt_bku)')
cols = cursor.fetchall()
for c in cols:
    print(f'  {c[1]} ({c[2]})')

# Check sample rpt_bku
print('\n=== Sample rpt_bku ===')
cursor = db.execute('SELECT * FROM rpt_bku LIMIT 3')
rows = cursor.fetchall()
for r in rows:
    print(f'  {r}')

# Get count for various tables
print('\n=== Row counts ===')
tables_to_check = [
    'kas_umum', 'rapbs', 'anggaran', 'ptk', 'mst_sekolah',
    'rpt_bku', 'report_bku', 'rapbs_periode'
]
for table in tables_to_check:
    try:
        cursor = db.execute(f'SELECT COUNT(*) FROM {table}')
        count = cursor.fetchone()[0]
        print(f'  {table}: {count} rows')
    except Exception as e:
        print(f'  {table}: ERROR - {e}')

# Check rpt_bku (alternative table?)
print('\n=== Sample rpt_bku ===')
cursor = db.execute('SELECT COUNT(*) FROM rpt_bku')
count = cursor.fetchone()[0]
print(f'  Total rows: {count}')
if count > 0:
    cursor = db.execute('PRAGMA table_info(rpt_bku)')
    cols = cursor.fetchall()
    print('  Schema:')
    for c in cols:
        print(f'    {c}')
    
    cursor = db.execute('SELECT * FROM rpt_bku LIMIT 3')
    rows = cursor.fetchall()
    print('  Data:')
    for r in rows:
        print(f'    {r}')

# Check tables for kas pembantu
print('\n=== Check kas_pembantu tables ===')
tables_to_check = ['kas_pembantu_bank', 'kas_pembantu_pajak', 'kas_pembantu_tunai', 'rpt_bku', 'report_bku']
for t in tables_to_check:
    try:
        cursor = db.execute(f'SELECT COUNT(*) FROM {t}')
        count = cursor.fetchone()[0]
        print(f'  {t}: {count} rows')
    except Exception as e:
        print(f'  {t}: TIDAK ADA')

# Check rpt_bku schema if exists
print('\n=== Check rpt_bku ===')
try:
    cursor = db.execute('SELECT COUNT(*) FROM rpt_bku')
    count = cursor.fetchone()[0]
    print(f'  rpt_bku: {count} rows')
    if count > 0:
        cursor = db.execute('PRAGMA table_info(rpt_bku)')
        cols = cursor.fetchall()
        print('  Schema:')
        for c in cols:
            print(f'    {c[1]} ({c[2]})')
except Exception as e:
    print(f'  rpt_bku: ERROR - {e}')

db.close()
print('\n=== DONE ===')