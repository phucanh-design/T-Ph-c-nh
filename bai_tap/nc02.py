from pathlib import Path
from typing import Iterable

import pandas as pd


def _data_path(filename: str) -> Path:
    return Path(__file__).resolve().parent.parent / "du_lieu_mau" / filename


def _normalize_sales_columns(df: pd.DataFrame) -> pd.DataFrame:
    col_map = {}
    for col in df.columns:
        key = col.strip().lower().replace(" ", "").replace("_", "")
        if key in {"madon", "mahoadon", "orderid"}:
            col_map[col] = "MaDon"
        elif key in {"makh", "makhachhang", "customerid"}:
            col_map[col] = "MaKH"
        elif key in {"ngaydat", "ngaydon", "orderdate"}:
            col_map[col] = "NgayDat"
        elif key in {"sanpham", "tensp", "product", "productname"}:
            col_map[col] = "SanPham"
        elif key in {"soluong", "qty", "quantity"}:
            col_map[col] = "SoLuong"
        elif key in {"dongia", "gia", "price", "unitprice"}:
            col_map[col] = "DonGia"
    return df.rename(columns=col_map)


def bai_nc2_ban_hang_nhieu_nguon(file_paths: Iterable[str | Path] | None = None):
    if file_paths is None:
        file_paths = [
            _data_path("banhang_thang1.csv"),
            _data_path("banhang_thang2.csv"),
            _data_path("banhang_thang3.csv"),
        ]
    frames = []
    for path in file_paths:
        tmp = pd.read_csv(path)
        frames.append(_normalize_sales_columns(tmp))

    df = pd.concat(frames, ignore_index=True)

    df["SoLuong"] = pd.to_numeric(df["SoLuong"], errors="coerce")
    df["DonGia"] = df["DonGia"].astype(str).str.replace(r"[^\d\.-]", "", regex=True)
    df["DonGia"] = pd.to_numeric(df["DonGia"], errors="coerce")
    df["NgayDat"] = pd.to_datetime(df["NgayDat"], errors="coerce")

    invalid_mask = (
        df["MaDon"].isna()
        | df["NgayDat"].isna()
        | df["SoLuong"].isna()
        | df["DonGia"].isna()
        | (df["SoLuong"] <= 0)
        | (df["DonGia"] <= 0)
    )

    so_don_loi = int(invalid_mask.sum())

    clean = df[~invalid_mask].copy()
    clean = clean.drop_duplicates(subset=["MaDon"], keep="first")
    clean["ThanhTien"] = clean["SoLuong"] * clean["DonGia"]

    doanh_thu_thang = (
        clean.assign(Thang=clean["NgayDat"].dt.to_period("M").astype(str))
        .groupby("Thang", as_index=False)["ThanhTien"]
        .sum()
        .rename(columns={"ThanhTien": "DoanhThu"})
    )

    top_5_san_pham = (
        clean.groupby("SanPham", as_index=False)["ThanhTien"]
        .sum()
        .sort_values("ThanhTien", ascending=False)
        .head(5)
    )

    return clean, doanh_thu_thang, top_5_san_pham, so_don_loi


if __name__ == "__main__":
    clean, doanh_thu, top5, loi = bai_nc2_ban_hang_nhieu_nguon()
    print(clean)
    print(doanh_thu)
    print(top5)
    print(loi)
