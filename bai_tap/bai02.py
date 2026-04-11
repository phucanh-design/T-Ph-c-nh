from pathlib import Path

import pandas as pd


def _data_path(filename: str) -> Path:
    return Path(__file__).resolve().parent.parent / "du_lieu_mau" / filename


def bai2_xoa_trung_donhang(input_csv: str | Path | None = None, output_csv: str | None = None):
    if input_csv is None:
        input_csv = _data_path("donhang.csv")
    df = pd.read_csv(input_csv)

    trung_toan_bo = df[df.duplicated(keep=False)].copy()
    trung_ma_don = df[df.duplicated(subset=["MaDon"], keep=False)].copy()

    clean = df.drop_duplicates(subset=["MaDon"], keep="first").copy()
    clean["ThanhTien"] = clean["SoLuong"] * clean["DonGia"]
    clean["NgayDat"] = pd.to_datetime(clean["NgayDat"], errors="coerce")
    clean = clean.sort_values("NgayDat", ascending=True).reset_index(drop=True)

    if output_csv:
        clean.to_csv(output_csv, index=False, encoding="utf-8-sig")

    return clean, trung_toan_bo, trung_ma_don


if __name__ == "__main__":
    clean, dup_all, dup_order = bai2_xoa_trung_donhang()
    print(clean)
    print(dup_all)
    print(dup_order)
