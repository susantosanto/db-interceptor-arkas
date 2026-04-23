import json, sqlcipher3 as sqlite3
cfg = json.load(open('C:/Users/USER/Documents/ARKASu Data/config.json'))
conn = sqlite3.connect(cfg['db_path'])
conn.execute(f"PRAGMA key = '{cfg['db_key']}'")
cur = conn.cursor()

print("=== RESEARCH DATABASE ARKAS ===\n")

# List all tables
print("--- ALL TABLES ---")
cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
tables = [r[0] for r in cur.fetchall()]
for t in tables:
    print(f"  - {t}")

# Get row counts for main tables
print("\n--- ROW COUNTS ---")
main_tables = ['kas_umum', 'rpt_bku', 'rapbs', 'anggaran', 'ref_bku', 'report_bku', 'ptk', 'rapbs_periode']
for t in main_tables:
    try:
        cur.execute(f"SELECT COUNT(*) FROM {t}")
        count = cur.fetchone()[0]
        print(f"  {t}: {count} rows")
    except:
        print(f"  {t}: TIDAK ADA")

# Check struktur kas_umum
print("\n--- KAS_UMUM STRUCTURE ---")
cur.execute("PRAGMA table_info(kas_umum)")
for col in cur.fetchall():
    print(f"  {col[1]} ({col[2]})")

# Check struktur ref_bku
print("\n--- REF_BKU (referensi kode BKU) ---")
cur.execute("SELECT * FROM ref_bku LIMIT 10")
for r in cur.fetchall():
    print(f"  {r}")

# Check struktur report_bku
print("\n--- REPORT_BKU STRUCTURE ---")
cur.execute("PRAGMA table_info(report_bku)")
for col in cur.fetchall():
    print(f"  {col[1]} ({col[2]})")

# Sample data from each table
print("\n--- KAS_UMUM SAMPLE (3 rows) ---")
cur.execute("SELECT * FROM kas_umum LIMIT 3")
for r in cur.fetchall():
    print(f"  {r}")

print("\n--- RPT_BKU SAMPLE (3 rows) ---")
cur.execute("SELECT * FROM rpt_bku LIMIT 3")
for r in cur.fetchall():
    print(f"  {r}")

print("\n--- ANGGARAN SAMPLE (3 rows) ---")
cur.execute("SELECT * FROM anggaran LIMIT 3")
for r in cur.fetchall():
    print(f"  {r}")

print("\n--- RAPBS SAMPLE (3 rows) ---")
cur.execute("SELECT kode_rekening, uraian, volume, satuan, harga_satuan, jumlah FROM rapbs LIMIT 3")
for r in cur.fetchall():
    print(f"  {r}")

# Check data by tahun
print("\n--- KAS_UMUM by TAHUN ---")
cur.execute("SELECT CAST(strftime('%Y', tanggal_transaksi) AS INTEGER) as tahun, COUNT(*) FROM kas_umum GROUP BY tahun ORDER BY tahun")
for r in cur.fetchall():
    print(f"  {r[0]}: {r[1]} rows")

print("\n--- RAPBS by TAHUN ---")
cur.execute("SELECT id_ref_tahun_anggaran, COUNT(*) FROM rapbs GROUP BY id_ref_tahun_anggaran ORDER BY id_ref_tahun_anggaran")
for r in cur.fetchall():
    print(f"  {r[0]}: {r[1]} rows")