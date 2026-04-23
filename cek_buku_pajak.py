import json
import sqlcipher3

# Load config
config_path = r"C:\Users\USER\.config\opencode\arkas_config.json"
with open(config_path, 'r') as f:
    config = json.load(f)

db_path = config['arkas']['db_path']
key = config['arkas']['key']
cipher_comp = config['arkas']['cipher_compatibility']

# Connect
db = sqlcipher3.connect(db_path)
db.execute(f"PRAGMA key = '{key}'")
db.execute(f"PRAGMA cipher_compatibility = {cipher_comp}")

# Get table structure - cari tabel buku pembantu pajak
print("=== MENCARI TABLE BUKU PAJAK ===")
cursor = db.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

buku_pajak_tables = []
for t in tables:
    nama = t[0].lower()
    if 'pajak' in nama or 'buku' in nama or 'pph' in nama or 'simp' in nama:
        buku_pajak_tables.append(t[0])
        
print(f"Tables found: {tables}")

# Look for data in kas_umum for tax related entries
print("\n=== BUKU PEMBANTU PAJAK (KAS UMUM) - MARET 2025 ===")
cursor = db.execute("""
    SELECT tanggal, uraian, debit, kredit 
    FROM kas_umum 
    WHERE (uraian LIKE '%pajak%' OR uraian LIKE '%pph%' OR uraian LIKE '%potongan%')
    AND tanggal >= '2025-03-01' AND tanggal <= '2025-03-31'
    ORDER BY tanggal
""")
rows = cursor.fetchall()

print(f"Tanggal       | Uraian                              | Debit      | Kredit")
print("-" * 80)
for row in rows:
    print(f"{row[0]} | {row[1][:35]:<35} | {row[2]} | {row[3]}")

# Check if there's a specific table for pajak
print("\n=== SEMUA TABLE ===")
for t in tables:
    print(t[0])

db.close()