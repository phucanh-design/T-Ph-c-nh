from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).parent
path = BASE_DIR / "customers.csv"

if not path.exists():
    print(f"[ERROR] Khong tim thay file: {path.name}")
else:
    df = pd.read_csv(path, dtype={"MaKH": "string"})

    print("=== Bai 4: customers.csv ===")
    print(df.head())
    print("\nKieu du lieu tung cot:")
    print(df.dtypes)

    print(
        "\nGiai thich: MaKH nen la chuoi de giu so 0 o dau, "
        "va tranh bi xem nhu so dung de tinh toan."
    )
