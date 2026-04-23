import sys, os, json
sys.path.append('C:/Users/USER/Documents/ARKASu Data')
import app
import sqlcipher3 as sqlite3
cfg = json.load(open('C:/Users/USER/Documents/ARKASu Data/config.json'))
conn = sqlite3.connect(cfg['db_path'])
conn.execute(f"PRAGMA key = '{cfg['db_key']}'")
cur = conn.cursor()
cur.execute("SELECT DISTINCT CAST(strftime('%Y', tanggal_transaksi) AS INTEGER) as yr FROM kas_umum ORDER BY yr")
years = [row[0] for row in cur.fetchall()]
print('Years in kas_umum:', years)
