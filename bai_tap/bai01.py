from pathlib import Path

import pandas as pd


def _data_path(filename: str) -> Path:
    return Path(__file__).resolve().parent.parent / "du_lieu_mau" / filename


def xep_loai(score: float) -> str:
    if score >= 8.0:
        return "A"
    if score >= 6.5:
        return "B"
    if score >= 5.0:
        return "C"
    return "D"


def bai1_lam_sach_diem_sinhvien(input_csv: str | Path | None = None, output_csv: str | None = None):
    if input_csv is None:
        input_csv = _data_path("diem_sinhvien.csv")
    df = pd.read_csv(input_csv)

    missing_scores = df[["DiemQT", "DiemThi", "DiemTK"]].isna().sum()

    df["DiemQT"] = df["DiemQT"].fillna(df["DiemQT"].mean())
    df["DiemThi"] = df["DiemThi"].fillna(df["DiemThi"].mean())
    df["HoTen"] = df["HoTen"].fillna("ChuaCapNhat")

    df["DiemTK"] = 0.4 * df["DiemQT"] + 0.6 * df["DiemThi"]
    df["XepLoai"] = df["DiemTK"].apply(xep_loai)

    if output_csv:
        df.to_csv(output_csv, index=False, encoding="utf-8-sig")

    return df, missing_scores


if __name__ == "__main__":
    result, missing = bai1_lam_sach_diem_sinhvien()
    print(result)
    print(missing)
