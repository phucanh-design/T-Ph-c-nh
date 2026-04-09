from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).parent
path = BASE_DIR / "sales.csv"
threshold = 10_000_000

if not path.exists():
    print(f"[ERROR] Khong tim thay file: {path.name}")
else:
    df = pd.read_csv(path)

    possible_rev_cols = ["DoanhThu", "Revenue", "ThanhTien", "TongTien"]
    rev_col = next((c for c in possible_rev_cols if c in df.columns), None)

    if rev_col is None:
        print("Khong tim thay cot doanh thu")
    else:
        high_sales = df[df[rev_col] > threshold].copy()

        out_csv = BASE_DIR / "high_sales.csv"
        out_xlsx = BASE_DIR / "high_sales.xlsx"

        high_sales.to_csv(out_csv, index=False, encoding="utf-8-sig")
        high_sales.to_excel(out_xlsx, index=False)

        print("=== Bai 8: Xuat du lieu ===")
        print(f"Nguong doanh thu: {threshold}")
        print(f"So don hang dat dieu kien: {len(high_sales)}")
        print(f"Da luu: {out_csv.name}, {out_xlsx.name}")
