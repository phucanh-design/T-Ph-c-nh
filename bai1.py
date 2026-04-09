from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).parent
path = BASE_DIR / "students.csv"

if not path.exists():
	print(f"[ERROR] Khong tim thay file: {path.name}")
else:
	df = pd.read_csv(path)
	print("=== Bai 1: students.csv ===")
	print("5 dong dau:")
	print(df.head())
	print(f"So dong: {df.shape[0]}")
	print(f"So cot: {df.shape[1]}")
	print("Ten cac cot:", list(df.columns))
