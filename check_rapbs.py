import json, sqlcipher3 as sqlite3
cfg = json.load(open('C:/Users/USER/Documents/ARKASu Data/config.json'))
conn = sqlite3.connect(cfg['db_path'])
conn.execute(f"PRAGMA key = '{cfg['db_key']}'")
cur = conn.cursor()

# Check kode_rekening patterns - BHP usually starts with 5.1.02 or similar
# Let's check distinct prefixes
print("=== Distinct kode_rekening prefixes in rapbs 2026 ===")
cur.execute("""
    SELECT DISTINCT SUBSTR(kode_rekening, 1, 3) as prefix, COUNT(*) as cnt 
    FROM rapbs 
    WHERE id_ref_tahun_anggaran = 2026 
    GROUP BY prefix 
    ORDER BY prefix
""")
for r in cur.fetchall():
    print(f"  {r[0]}: {r[1]}")

print("\n=== Sample rows by prefix ===")
cur.execute("SELECT kode_rekening, uraian FROM rapbs WHERE id_ref_tahun_anggaran = 2026 LIMIT 10")
for r in cur.fetchall():
    print(r)