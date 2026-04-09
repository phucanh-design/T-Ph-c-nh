from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).parent
path = BASE_DIR / "scores_no_header.csv"

if not path.exists():
    print(f"[ERROR] Khong tim thay file: {path.name}")
else:
    columns = ["MaSV", "HoTen", "Lop", "DiemQT", "DiemThi"]
    df = pd.read_csv(path, header=None, names=columns)

    print("=== Bai 3: scores_no_header.csv ===")
    print(df.head())
    print("\nThong tin du lieu:")
    df.info()
