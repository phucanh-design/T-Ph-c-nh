from pathlib import Path

import pandas as pd


def _data_path(filename: str) -> Path:
    return Path(__file__).resolve().parent.parent / "du_lieu_mau" / filename


def _normalize_spaces(text: str) -> str:
    return " ".join(str(text).split())


def bai_nc1_tuyen_sinh(
    input_csv: str | Path | None = None,
    output_clean_csv: str | None = None,
    output_summary_csv: str | None = None,
):
    if input_csv is None:
        input_csv = _data_path("tuyensinh.csv")
    df = pd.read_csv(input_csv)

    df["HoTen"] = df["HoTen"].astype(str).map(_normalize_spaces).str.title()

    gender_map = {
        "nam": "Nam",
        "male": "Nam",
        "m": "Nam",
        "nu": "Nu",
        "nữ": "Nu",
        "female": "Nu",
        "f": "Nu",
    }
    df["GioiTinh"] = df["GioiTinh"].astype(str).str.strip().str.lower().replace(gender_map)
    df["NgaySinh"] = pd.to_datetime(df["NgaySinh"], errors="coerce", dayfirst=True)

    for col in ["DiemToan", "DiemVan", "DiemAnh"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(df[col].median())

    if df["KhuVuc"].notna().any():
        df["KhuVuc"] = df["KhuVuc"].fillna(df["KhuVuc"].mode().iloc[0])
    df["HoTen"] = df["HoTen"].replace("Nan", "ChuaCapNhat")
    df["GioiTinh"] = df["GioiTinh"].fillna("Khac")

    diem_loi = df[
        (~df["DiemToan"].between(0, 10))
        | (~df["DiemVan"].between(0, 10))
        | (~df["DiemAnh"].between(0, 10))
    ].copy()

    df["TongDiem"] = df[["DiemToan", "DiemVan", "DiemAnh"]].sum(axis=1)
    df["NhomDiem"] = pd.qcut(
        df["TongDiem"], q=4, labels=["thap", "trung binh", "kha", "cao"], duplicates="drop"
    )

    thong_ke_khu_vuc = (
        df.groupby("KhuVuc", dropna=False)
        .agg(SoThiSinh=("MaHS", "count"), TongDiemTB=("TongDiem", "mean"))
        .reset_index()
    )

    if output_clean_csv:
        df.to_csv(output_clean_csv, index=False, encoding="utf-8-sig")
    if output_summary_csv:
        thong_ke_khu_vuc.to_csv(output_summary_csv, index=False, encoding="utf-8-sig")

    return df, diem_loi, thong_ke_khu_vuc


if __name__ == "__main__":
    df, bad_scores, summary = bai_nc1_tuyen_sinh()
    print(df)
    print(bad_scores)
    print(summary)
