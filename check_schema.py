import json, sqlcipher3 as sqlite3
cfg = json.load(open('C:/Users/USER/Documents/ARKASu Data/config.json'))
conn = sqlite3.connect(cfg['db_path'])
conn.execute(f"PRAGMA key = '{cfg['db_key']}'")
cur = conn.cursor()

# Get schema for tables used by app
tables_to_check = ['rapbs', 'anggaran', 'report_bku', 'ref_bku']

for t in tables_to_check:
    print(f"\n=== {t} schema ===")
    cur.execute(f"PRAGMA table_info({t})")
    for col in cur.fetchall():
        print(f"  {col[1]} ({col[2]})")

# Check count per year in rapbs
print("\n=== rapbs count by tahun ===")
cur.execute("SELECT tahun_anggaran, COUNT(*) FROM rapbs GROUP BY tahun_anggaran ORDER BY tahun_anggaran")
for r in cur.fetchall():
    print(f"  {r[0]}: {r[1]} rows")

# Check count per year in anggaran
print("\n=== anggaran count by tahun ===")
cur.execute("SELECT tahun_anggaran, COUNT(*) FROM anggaran GROUP BY tahun_anggaran ORDER BY tahun_anggaran")
for r in cur.fetchall():
    print(f"  {r[0]}: {r[1]} rows")