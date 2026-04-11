from pathlib import Path

import numpy as np
import pandas as pd


def _data_path(filename: str) -> Path:
    return Path(__file__).resolve().parent.parent / "du_lieu_mau" / filename


def _normalize_spaces(text: str) -> str:
    return " ".join(str(text).split())


def bai3_chuan_hoa_nhansu(input_csv: str | Path | None = None, output_csv: str | None = None):
    if input_csv is None:
        input_csv = _data_path("nhansu.csv")
    df = pd.read_csv(input_csv)

    gender_map = {
        "nam": "Nam",
        "male": "Nam",
        "m": "Nam",
        "nu": "Nu",
        "nữ": "Nu",
        "female": "Nu",
        "f": "Nu",
    }

    df["GioiTinh"] = (
        df["GioiTinh"].astype(str).str.strip().str.lower().replace(gender_map).replace({"nan": np.nan})
    )
    df["PhongBan"] = df["PhongBan"].astype(str).str.strip().str.title()
    df["HoTen"] = df["HoTen"].astype(str).map(_normalize_spaces)

    df = df.rename(
        columns={
            "MaNV": "ma_nv",
            "HoTen": "ho_ten",
            "GioiTinh": "gioi_tinh",
            "PhongBan": "phong_ban",
            "Luong": "luong",
        }
    )

    if output_csv:
        df.to_csv(output_csv, index=False, encoding="utf-8-sig")

    return df


if __name__ == "__main__":
    print(bai3_chuan_hoa_nhansu())
