from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).parent
path = BASE_DIR / "products.json"

if not path.exists():
    print(f"[ERROR] Khong tim thay file: {path.name}")
else:
    df_raw = pd.read_json(path)

    if df_raw.shape[1] == 1 and isinstance(df_raw.iloc[0, 0], (dict, list)):
        df = pd.json_normalize(df_raw.iloc[:, 0])
    else:
        df = df_raw.copy()

    print("=== Bai 9: products.json ===")
    basic_cols = ["MaSP", "TenSP", "NhomHang", "Gia"]
    show_cols = [c for c in basic_cols if c in df.columns]

    if show_cols:
        print(df[show_cols].head())
    else:
        print(df.head())

    print("\nNhan xet:")
    print("- JSON linh hoat, co the long nhau (nested)")
    print("- CSV la dang bang phang, de xem nhanh tren bang tinh")
