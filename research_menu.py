import json, sqlcipher3 as sqlite3
cfg = json.load(open('C:/Users/USER/Documents/ARKASu Data/config.json'))
conn = sqlite3.connect(cfg['db_path'])
conn.execute(f"PRAGMA key = '{cfg['db_key']}'")
cur = conn.cursor()

print("=== RESEARCH SETIAP MENU LAPORAN ===\n")

# 1. BUKU KAS UMUM -Semua transaksi kas dengan JOIN ref_bku untuk status
print("--- 1. BUKU KAS UMUM (kas_umum + ref_bku) ---")
cur.execute("""
    SELECT k.tanggal_transaksi, r.bku as status, k.uraian, k.saldo, k.no_bukti
    FROM kas_umum k
    LEFT JOIN ref_bku r ON k.id_ref_bku = r.id_ref_bku
    WHERE k.tanggal_transaksi IS NOT NULL
    ORDER BY k.tanggal_transaksi DESC
    LIMIT 5
""")
for r in cur.fetchall():
    print(f"  {r}")

# 2. KAS BANK - Transaksi bank (ref_bku id 2=Terima Dana BOS, 8=Saldo Awal Bank)
print("\n--- 2. KAS BANK (id_ref_bku = 2 atau 8) ---")
cur.execute("""
    SELECT k.tanggal_transaksi, r.bku as status, k.uraian, k.saldo, k.no_bukti
    FROM kas_umum k
    LEFT JOIN ref_bku r ON k.id_ref_bku = r.id_ref_bku
    WHERE k.id_ref_bku IN (2, 8)
    ORDER BY k.tanggal_transaksi DESC
    LIMIT 5
""")
for r in cur.fetchall():
    print(f"  {r}")

# 3. KAS PAJAK - Transaksi pajak (ref_bku id 7=Pajak Bunga, 10=Pajak Belanja Terima)
print("\n--- 3. KAS PAJAK (id_ref_bku = 7 atau 10) ---")
cur.execute("""
    SELECT k.tanggal_transaksi, r.bku as status, k.uraian, k.saldo, k.no_bukti
    FROM kas_umum k
    LEFT JOIN ref_bku r ON k.id_ref_bku = r.id_ref_bku
    WHERE k.id_ref_bku IN (7, 10)
    ORDER BY k.tanggal_transaksi DESC
    LIMIT 5
""")
for r in cur.fetchall():
    print(f"  {r}")

# 4. KAS TUNAI - Transaksi tunai (ref_bku id 3, 5, 9)
print("\n--- 4. KAS TUNAI (id_ref_bku = 3, 5, 9) ---")
cur.execute("""
    SELECT k.tanggal_transaksi, r.bku as status, k.uraian, k.saldo, k.no_bukti
    FROM kas_umum k
    LEFT JOIN ref_bku r ON k.id_ref_bku = r.id_ref_bku
    WHERE k.id_ref_bku IN (3, 5, 9)
    ORDER BY k.tanggal_transaksi DESC
    LIMIT 5
""")
for r in cur.fetchall():
    print(f"  {r}")

# 5. KERTAS KERJA / RKAS - Dari rapbs
print("\n--- 5. KERTAS KERJA (dari rapbs) ---")
cur.execute("""
    SELECT kode_rekening, uraian, volume, satuan, jumlah
    FROM rapbs
    WHERE id_ref_tahun_anggaran = 2026
    ORDER BY kode_rekening
    LIMIT 5
""")
for r in cur.fetchall():
    print(f"  {r}")

# 6. REALISASI - Dari anggaran dengan join rapbs
print("\n--- 6. REALISASI (anggaran + rapbs) ---")
cur.execute("""
    SELECT r.kode_rekening, r.uraian, a.jumlah as anggaran, 
           (SELECT COALESCE(SUM(k.saldo), 0) FROM kas_umum k WHERE k.id_anggaran = a.id_anggaran) as realisasi,
           a.jumlah - (SELECT COALESCE(SUM(k.saldo), 0) FROM kas_umum k WHERE k.id_anggaran = a.id_anggaran) as selisih
    FROM anggaran a
    LEFT JOIN rapbs r ON a.id_anggaran = r.id_anggaran
    WHERE a.tahun_anggaran = 2026
    LIMIT 5
""")
for r in cur.fetchall():
    print(f"  {r}")

# 7. BHP - Barang Habis Pakai (prefix 5.1.02.01)
print("\n--- 7. BHP (prefix 5.1.02.01) ---")
cur.execute("""
    SELECT kode_rekening, uraian, volume, satuan, jumlah
    FROM rapbs
    WHERE id_ref_tahun_anggaran = 2026 AND SUBSTR(kode_rekening, 1, 9) = '5.1.02.01'
    ORDER BY kode_rekening
    LIMIT 5
""")
for r in cur.fetchall():
    print(f"  {r}")

# 8. MODAL - Barang Modal (prefix 5.1.02.02)
print("\n--- 8. MODAL (prefix 5.1.02.02) ---")
cur.execute("""
    SELECT kode_rekening, uraian, volume, satuan, jumlah
    FROM rapbs
    WHERE id_ref_tahun_anggaran = 2026 AND SUBSTR(kode_rekening, 1, 9) = '5.1.02.02'
    ORDER BY kode_rekening
    LIMIT 5
""")
for r in cur.fetchall():
    print(f"  {r}")

# 9. BP OBJEK - grouped from rapbs
print("\n--- 9. BP OBJEK (grouped by kode_rekening) ---")
cur.execute("""
    SELECT kode_rekening, MAX(uraian) as uraian, SUM(volume) as volume, MAX(satuan) as satuan, SUM(jumlah) as jumlah
    FROM rapbs
    WHERE id_ref_tahun_anggaran = 2026
    GROUP BY kode_rekening
    ORDER BY kode_rekening
    LIMIT 5
""")
for r in cur.fetchall():
    print(f"  {r}")

# 10. BOSP - BOS finance report
print("\n--- 10. BOSP (dari anggaran) ---")
cur.execute("""
    SELECT a.tahun_anggaran, a.jumlah as total_anggaran, 
           (SELECT COALESCE(SUM(k.saldo), 0) FROM kas_umum k WHERE k.tanggal_transaksi LIKE '2026%') as total_realisasi
    FROM anggaran a
    WHERE a.tahun_anggaran = 2026
    GROUP BY a.tahun_anggaran
""")
for r in cur.fetchall():
    print(f"  {r}")

print("\n=== DONE ===")