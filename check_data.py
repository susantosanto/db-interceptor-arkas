import json, sqlcipher3 as sqlite3
cfg = json.load(open('C:/Users/USER/Documents/ARKASu Data/config.json'))
conn = sqlite3.connect(cfg['db_path'])
conn.execute(f"PRAGMA key = '{cfg['db_key']}'")
cur = conn.cursor()

# Check rapbs
print("=== rapbs sample ===")
cur.execute("SELECT * FROM rapbs LIMIT 3")
for r in cur.fetchall():
    print(r)

print("\n=== anggaran sample ===")
cur.execute("SELECT * FROM anggaran LIMIT 3")
for r in cur.fetchall():
    print(r)

print("\n=== report_bku sample ===")
cur.execute("SELECT * FROM report_bku LIMIT 3")
for r in cur.fetchall():
    print(r)