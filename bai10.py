import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).parent
db_path = BASE_DIR / "shop.db"

if not db_path.exists():
    print(f"[ERROR] Khong tim thay file: {db_path.name}")
else:
    with sqlite3.connect(db_path) as conn:
        orders = pd.read_sql("SELECT * FROM orders", conn)

    print("=== Bai 10: SQLite + pandas.read_sql ===")
    print("5 ban ghi dau:")
    print(orders.head())

    total_orders = len(orders)
    print(f"Tong so don hang: {total_orders}")

    possible_rev_cols = ["DoanhThu", "Revenue", "TotalAmount", "TongTien"]
    rev_col = next((c for c in possible_rev_cols if c in orders.columns), None)

    if rev_col is None:
        print("Khong tim thay cot doanh thu de tinh tong")
    else:
        total_revenue = orders[rev_col].sum()
        print(f"Tong doanh thu ({rev_col}): {total_revenue}")
