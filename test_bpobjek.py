import sys, os, json
sys.path.append('C:/Users/USER/Documents/ARKASu Data')
import app

print("=== Testing BP Objek for 2026 ===\n")

bp = app.get_buku_pembantu_objek(tahun=2026)
print(f"BP Objek: {len(bp)} rows")

print("\n=== Sample (first 5) ===")
for row in bp[:5]:
    print(row)

print("\n=== Unique kode_rekening count ===")
codes = set(r[0] for r in bp)
print(f"Unique codes: {len(codes)}")