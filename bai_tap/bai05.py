from pathlib import Path

import pandas as pd


def _data_path(filename: str) -> Path:
    return Path(__file__).resolve().parent.parent / "du_lieu_mau" / filename


def bai5_xu_ly_suckhoe(input_csv: str | Path | None = None, output_csv: str | None = None):
    if input_csv is None:
        input_csv = _data_path("suckhoe.csv")
    df = pd.read_csv(input_csv)

    tuoi_bat_thuong = df[(df["Tuoi"] <= 0) | (df["Tuoi"] > 100)].copy()
    missing_cn_cc = df[["CanNang", "ChieuCao"]].isna().sum()

    df["CanNang"] = df["CanNang"].fillna(df["CanNang"].median())
    df["ChieuCao"] = df["ChieuCao"].fillna(df["ChieuCao"].median())

    blood_map = {"a": "A", "b": "B", "ab": "AB", "o": "O"}
    df["NhomMau"] = df["NhomMau"].astype(str).str.strip().str.lower().replace(blood_map).str.upper()

    df["BMI"] = df["CanNang"] / (df["ChieuCao"] / 100) ** 2

    if output_csv:
        df.to_csv(output_csv, index=False, encoding="utf-8-sig")

    return df, tuoi_bat_thuong, missing_cn_cc


if __name__ == "__main__":
    df, invalid_age, missing = bai5_xu_ly_suckhoe()
    print(df)
    print(invalid_age)
    print(missing)
