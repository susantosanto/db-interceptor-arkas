import json, sqlcipher3 as sqlite3
cfg = json.load(open('C:/Users/USER/Documents/ARKASu Data/config.json'))
conn = sqlite3.connect(cfg['db_path'])
conn.execute(f"PRAGMA key = '{cfg['db_key']}'")
cur = conn.cursor()

# BP Objek should be grouped by kode_rekening (unique objects)
print("=== BP Objek (grouped by kode_rekening) for 2026 ===")
cur.execute("""
    SELECT kode_rekening, uraian, SUM(volume) as total_volume, satuan, SUM(jumlah) as total_jumlah
    FROM rapbs
    WHERE id_ref_tahun_anggaran = 2026
    GROUP BY kode_rekening
    ORDER BY kode_rekening
""")
print(f"Total grouped: {cur.rowcount} objects")
for r in cur.fetchall()[:10]:
    print(f"  {r[0]}: {r[1]} | Vol: {r[2]} {r[3]} | Jumlah: {r[4]:,}")