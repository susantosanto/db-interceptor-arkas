import json, sqlcipher3 as sqlite3
cfg = json.load(open('C:/Users/USER/Documents/ARKASu Data/config.json'))
conn = sqlite3.connect(cfg['db_path'])
conn.execute(f"PRAGMA key = '{cfg['db_key']}'")
cur = conn.cursor()

# Check counts
tables = ['rapbs', 'anggaran', 'report_bku', 'kas_umum', 'rpt_bku']
for t in tables:
    cur.execute(f"SELECT COUNT(*) FROM {t}")
    print(f"{t}: {cur.fetchone()[0]} rows")

print("\n=== rapbs by id_ref_tahun_anggaran ===")
cur.execute("SELECT id_ref_tahun_anggaran, COUNT(*) FROM rapbs GROUP BY id_ref_tahun_anggaran ORDER BY id_ref_tahun_anggaran")
for r in cur.fetchall():
    print(f"  {r[0]}: {r[1]} rows")

print("\n=== anggaran by tahun_anggaran ===")
cur.execute("SELECT tahun_anggaran, COUNT(*) FROM anggaran GROUP BY tahun_anggaran ORDER BY tahun_anggaran")
for r in cur.fetchall():
    print(f"  {r[0]}: {r[1]} rows")

print("\n=== Sample rapbs ===")
cur.execute("SELECT id_ref_tahun_anggaran, kode_rekening, uraian FROM rapbs LIMIT 3")
for r in cur.fetchall():
    print(r)