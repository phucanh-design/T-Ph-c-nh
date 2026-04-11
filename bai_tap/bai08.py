from pathlib import Path

import numpy as np
import pandas as pd


def _data_path(filename: str) -> Path:
    return Path(__file__).resolve().parent.parent / "du_lieu_mau" / filename


def bai8_phan_nhom_chitieu(input_csv: str | Path | None = None, output_csv: str | None = None):
    if input_csv is None:
        input_csv = _data_path("chitieu.csv")
    df = pd.read_csv(input_csv)

    giao_dich_loi = df[df["SoTien"] <= 0].copy()
    df = df[df["SoTien"] > 0].copy()

    if df["SoTien"].nunique() >= 3:
        bins = np.linspace(df["SoTien"].min(), df["SoTien"].max(), 4)
        bins[0] = bins[0] - 1e-9
        df["MucChiTieu"] = pd.cut(df["SoTien"], bins=bins, labels=["thap", "trung binh", "cao"])
    else:
        df["MucChiTieu"] = "trung binh"

    thong_ke_muc = df.groupby("MucChiTieu", dropna=False).size().reset_index(name="SoGiaoDich")
    tong_theo_nhom = df.groupby("NhomChiTieu", dropna=False)["SoTien"].agg(TongChiTieu="sum").reset_index()

    if output_csv:
        df.to_csv(output_csv, index=False, encoding="utf-8-sig")

    return df, giao_dich_loi, thong_ke_muc, tong_theo_nhom


if __name__ == "__main__":
    df, invalid, stats, agg = bai8_phan_nhom_chitieu()
    print(df)
    print(invalid)
    print(stats)
    print(agg)
