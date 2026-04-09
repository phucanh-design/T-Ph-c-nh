from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).parent


def read_with_fallback(path: Path, encodings: list[str]) -> pd.DataFrame | None:
    for enc in encodings:
        try:
            df = pd.read_csv(path, encoding=enc)
            print(f"Doc thanh cong {path.name} voi encoding='{enc}'")
            return df
        except UnicodeDecodeError as exc:
            print(f"Thu encoding='{enc}' that bai: {exc}")
    return None


utf8_path = BASE_DIR / "sinhvien_utf8.csv"
ansi_path = BASE_DIR / "sinhvien_ansi.csv"

print("=== Bai 5: Loi ma hoa tieng Viet ===")

if utf8_path.exists():
    df_utf8 = read_with_fallback(utf8_path, ["utf-8", "utf-8-sig", "cp1258", "latin1"])
    if df_utf8 is not None:
        print(df_utf8.head())
else:
    print(f"[ERROR] Khong tim thay file: {utf8_path.name}")

if ansi_path.exists():
    df_ansi = read_with_fallback(ansi_path, ["cp1258", "latin1", "utf-8", "utf-8-sig"])
    if df_ansi is not None:
        print(df_ansi.head())
else:
    print(f"[ERROR] Khong tim thay file: {ansi_path.name}")

print(
    "Nhan xet: UTF-8 pho bien tren web/API, con ANSI (Windows-1258) thuong gap o file cu tren Windows."
)
