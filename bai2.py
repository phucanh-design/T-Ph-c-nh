from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).parent
path = BASE_DIR / "sales_semicolon.csv"

if not path.exists():
    print(f"[ERROR] Khong tim thay file: {path.name}")
else:
    print("=== Bai 2: sales_semicolon.csv ===")

    df_wrong = pd.read_csv(path)
    print("\nDoc sai sep (mac dinh dau phay):")
    print(df_wrong.head())
    print("Cot doc sai:", list(df_wrong.columns))

    df_right = pd.read_csv(path, sep=";")
    print("\nDoc dung sep=';':")
    print(df_right.head())
    print("Cot doc dung:", list(df_right.columns))

    print("\nGiai thich: khi sep sai, pandas khong tach duoc cac truong nen ca dong bi don vao 1 cot.")
