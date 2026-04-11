from pathlib import Path

import pandas as pd


def _data_path(filename: str) -> Path:
    return Path(__file__).resolve().parent.parent / "du_lieu_mau" / filename


def _normalize_spaces(text: str) -> str:
    return " ".join(str(text).split())


def bai10_lam_sach_lienhe(input_csv: str | Path | None = None, output_csv: str | None = None):
    if input_csv is None:
        input_csv = _data_path("lienhe.csv")
    df = pd.read_csv(input_csv)

    df["Email"] = df["Email"].astype(str).str.strip().str.lower()
    pattern = r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"
    df["EmailHopLe"] = df["Email"].str.contains(pattern, regex=True, na=False)

    so = df["SoDienThoai"].astype(str).str.replace(r"\D", "", regex=True)
    df["DauSo"] = so.str.extract(r"^(\d{2,4})")

    df["DiaChi"] = df["DiaChi"].astype(str).map(_normalize_spaces)
    df["Domain"] = df["Email"].str.extract(r"@(.+)$")

    if output_csv:
        df.to_csv(output_csv, index=False, encoding="utf-8-sig")

    return df


if __name__ == "__main__":
    print(bai10_lam_sach_lienhe())
