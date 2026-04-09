from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).parent
path = BASE_DIR / "inventory.xlsx"

if not path.exists():
    print(f"[ERROR] Khong tim thay file: {path.name}")
else:
    df_hanghoa = pd.read_excel(path, sheet_name="HangHoa")
    print("=== Bai 6: inventory.xlsx / sheet HangHoa ===")
    print(df_hanghoa.head(10))

    possible_qty_cols = ["TonKho", "SoLuongTon", "SoLuong", "Quantity"]
    qty_col = next((c for c in possible_qty_cols if c in df_hanghoa.columns), None)

    if qty_col is None:
        print("Khong tim thay cot ton kho de loc dieu kien < 20")
    else:
        low_stock_df = df_hanghoa[df_hanghoa[qty_col] < 20].copy()
        print(f"\nMat hang ton kho < 20 theo cot '{qty_col}':")
        print(low_stock_df)
