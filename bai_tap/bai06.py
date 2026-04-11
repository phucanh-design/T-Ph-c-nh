from pathlib import Path

import pandas as pd


def _data_path(filename: str) -> Path:
    return Path(__file__).resolve().parent.parent / "du_lieu_mau" / filename


def bai6_chuan_hoa_sanpham(input_csv: str | Path | None = None, output_csv: str | None = None):
    if input_csv is None:
        input_csv = _data_path("sanpham.csv")
    df = pd.read_csv(input_csv)

    df["Gia"] = df["Gia"].astype(str).str.replace(r"[^\d\.-]", "", regex=True)
    df["Gia"] = pd.to_numeric(df["Gia"], errors="coerce")

    df["DanhMuc"] = df["DanhMuc"].astype(str).str.strip().str.lower()
    df = df[df["SoLuongTon"] >= 0].copy()
    df = df.sort_values("Gia", ascending=False).reset_index(drop=True)

    if output_csv:
        df.to_csv(output_csv, index=False, encoding="utf-8-sig")

    return df


if __name__ == "__main__":
    print(bai6_chuan_hoa_sanpham())
