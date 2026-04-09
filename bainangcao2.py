from __future__ import annotations

from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).parent


def _full_path(file_name: str) -> Path:
    return BASE_DIR / file_name


def _normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    # Chuan hoa ten cot ve snake_case don gian.
    mapping = {}
    for col in df.columns:
        normalized = (
            str(col)
            .strip()
            .replace(" ", "_")
            .replace("-", "_")
            .replace("__", "_")
            .lower()
        )
        mapping[col] = normalized
    df = df.rename(columns=mapping)

    # Hop nhat cac bien the ten cot ve cung mot schema.
    canonical_map = {
        "orderid": "order_id",
        "order_id": "order_id",
        "order-id": "order_id",
        "doanhthu": "doanh_thu",
        "doanh_thu": "doanh_thu",
        "doanh-thu": "doanh_thu",
    }

    rename_map = {}
    for col in df.columns:
        key = col.replace("-", "_").replace(" ", "").lower()
        if key in canonical_map:
            rename_map[col] = canonical_map[key]

    return df.rename(columns=rename_map)


def bai_nang_cao_2() -> pd.DataFrame | None:
    """
    Doc 3 file sales_jan.csv, sales_feb.csv, sales_mar.csv,
    chuan hoa ten cot, ghep thanh 1 DataFrame va luu sales_q1.csv.
    """
    file_names = ["sales_jan.csv", "sales_feb.csv", "sales_mar.csv"]
    dataframes = []

    for name in file_names:
        path = _full_path(name)
        if not path.exists():
            print(f"[ERROR] Khong tim thay file: {name}")
            return None

        df = pd.read_csv(path)
        df = _normalize_columns(df)
        df["source_month"] = name.replace("sales_", "").replace(".csv", "")
        dataframes.append(df)

    # Hop schema: concat theo ten cot sau khi da chuan hoa.
    q1_df = pd.concat(dataframes, ignore_index=True, sort=False)

    out_path = _full_path("sales_q1.csv")
    q1_df.to_csv(out_path, index=False, encoding="utf-8-sig")

    print("Da tao file tong hop quy 1:", out_path.name)
    print("Kich thuoc du lieu:", q1_df.shape)
    print(q1_df.head())
    return q1_df


if __name__ == "__main__":
    bai_nang_cao_2()
