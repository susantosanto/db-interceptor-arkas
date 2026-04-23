import sys, os, json
sys.path.append('C:/Users/USER/Documents/ARKASu Data')
import app

print("=== Comparing BHP vs Modal for 2026 ===\n")

bhp = app.get_realisasi_barang_habis(tahun=2026)
modal = app.get_realisasi_barang_modal(tahun=2026)

print(f"BHP (Barang Habis Pakai): {len(bhp)} rows")
print(f"Modal (Barang Modal/Aset): {len(modal)} rows")

print("\n=== BHP Sample (first 3) ===")
for row in bhp[:3]:
    print(f"  {row[0]}: {row[1]}")

print("\n=== Modal Sample (first 3) ===")
for row in modal[:3]:
    print(f"  {row[0]}: {row[1]}")

print("\n=== Check overlap (should be 0) ===")
bhp_codes = set(r[0] for r in bhp)
modal_codes = set(r[0] for r in modal)
overlap = bhp_codes & modal_codes
print(f"Overlapping codes: {len(overlap)}")