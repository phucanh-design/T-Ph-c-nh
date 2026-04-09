from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).parent
path = BASE_DIR / "inventory.xlsx"

if not path.exists():
    print(f"[ERROR] Khong tim thay file: {path.name}")
else:
    sheet_names = ["HangHoa", "NhapKho", "XuatKho"]
    sheets = pd.read_excel(path, sheet_name=sheet_names)

    print("=== Bai 7: inventory.xlsx / nhieu sheet ===")
    for name, df in sheets.items():
        print(f"\nSheet: {name}")
        print(f"Shape: {df.shape}")
        print("Columns:", list(df.columns))

    print("\nMo ta chuc nang tung sheet:")
    print("- HangHoa: Danh muc hang hoa va ton kho hien tai")
    print("- NhapKho: Cac giao dich nhap hang vao kho")
    print("- XuatKho: Cac giao dich xuat hang khoi kho")
