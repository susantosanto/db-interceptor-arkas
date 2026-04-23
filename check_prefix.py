import json, sqlcipher3 as sqlite3
cfg = json.load(open('C:/Users/USER/Documents/ARKASu Data/config.json'))
conn = sqlite3.connect(cfg['db_path'])
conn.execute(f"PRAGMA key = '{cfg['db_key']}'")
cur = conn.cursor()

# Check exact prefixes - first 9 chars
print("=== Distinct kode_rekening prefixes (9 chars) in rapbs 2026 ===")
cur.execute("""
    SELECT DISTINCT SUBSTR(kode_rekening, 1, 9) as prefix, COUNT(*) as cnt 
    FROM rapbs 
    WHERE id_ref_tahun_anggaran = 2026 
    GROUP BY prefix 
    ORDER BY prefix
    LIMIT 20
""")
for r in cur.fetchall():
    print(f"  {r[0]}: {r[1]}")