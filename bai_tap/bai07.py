from pathlib import Path

import pandas as pd


def _data_path(filename: str) -> Path:
    return Path(__file__).resolve().parent.parent / "du_lieu_mau" / filename


def bai7_lam_sach_khaosat(input_csv: str | Path | None = None, output_csv: str | None = None):
    if input_csv is None:
        input_csv = _data_path("khaosat.csv")
    df = pd.read_csv(input_csv)

    map_lam_them = {
        "yes": 1,
        "y": 1,
        "co": 1,
        "có": 1,
        "1": 1,
        "no": 0,
        "n": 0,
        "khong": 0,
        "không": 0,
        "0": 0,
    }
    df["CoLamThem"] = df["CoLamThem"].astype(str).str.strip().str.lower().replace(map_lam_them)

    map_hailong = {
        "rat khong hai long": 1,
        "khong hai long": 2,
        "binh thuong": 3,
        "hai long": 4,
        "rat hai long": 5,
    }
    muc = df["MucDoHaiLong"].astype(str).str.strip().str.lower().replace(map_hailong)
    df["MucDoHaiLong"] = pd.to_numeric(muc, errors="coerce").clip(lower=1, upper=5)

    df = df.rename(
        columns={
            "MaSV": "ma_sv",
            "GioHocMoiNgay": "gio_hoc_moi_ngay",
            "MucDoHaiLong": "muc_do_hai_long",
            "CoLamThem": "co_lam_them",
        }
    )

    df = df[df["gio_hoc_moi_ngay"] >= 0].copy()
    thong_ke = df["co_lam_them"].value_counts(dropna=False)

    if output_csv:
        df.to_csv(output_csv, index=False, encoding="utf-8-sig")

    return df, thong_ke


if __name__ == "__main__":
    df, counts = bai7_lam_sach_khaosat()
    print(df)
    print(counts)
