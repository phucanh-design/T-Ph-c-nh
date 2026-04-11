from pathlib import Path

import pandas as pd


def _data_path(filename: str) -> Path:
    return Path(__file__).resolve().parent.parent / "du_lieu_mau" / filename


def bai4_lam_sach_muonsach(
    input_csv: str | Path | None = None, output_csv: str | None = None, current_date: str | None = None
):
    if input_csv is None:
        input_csv = _data_path("muonsach.csv")
    df = pd.read_csv(input_csv)

    df["NgayMuon"] = pd.to_datetime(df["NgayMuon"], errors="coerce")
    df["NgayTra"] = pd.to_datetime(df["NgayTra"], errors="coerce")

    status_map = {
        "datra": "DaTra",
        "da tra": "DaTra",
        "chuatra": "ChuaTra",
        "chua tra": "ChuaTra",
    }

    df["TrangThai"] = df["TrangThai"].astype(str).str.strip().str.lower().replace(status_map)
    df.loc[df["NgayTra"].isna(), "TrangThai"] = "ChuaTra"
    df.loc[df["NgayTra"].notna() & df["TrangThai"].isna(), "TrangThai"] = "DaTra"

    if current_date is None:
        current = pd.Timestamp.today().normalize()
    else:
        current = pd.to_datetime(current_date)

    df["SoNgayMuon"] = (df["NgayTra"].fillna(current) - df["NgayMuon"]).dt.days
    qua_han = df[(df["TrangThai"] == "ChuaTra") & (df["SoNgayMuon"] > 30)].copy()

    if output_csv:
        df.to_csv(output_csv, index=False, encoding="utf-8-sig")

    return df, qua_han


if __name__ == "__main__":
    df, overdue = bai4_lam_sach_muonsach()
    print(df)
    print(overdue)
