from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def _data_path(filename: str) -> Path:
    return Path(__file__).resolve().parent.parent / "du_lieu_mau" / filename


def bai9_xu_ly_ngoai_le(input_csv: str | Path | None = None, output_csv: str | None = None, method: str = "iqr"):
    if input_csv is None:
        input_csv = _data_path("moitruong.csv")
    df = pd.read_csv(input_csv)
    nhiet_do = pd.to_numeric(df["NhietDo"], errors="coerce")

    if method.lower() == "zscore":
        mean = nhiet_do.mean()
        std = nhiet_do.std(ddof=0)
        z = (nhiet_do - mean) / std if std else pd.Series(0, index=nhiet_do.index)
        mask = z.abs() > 3
    else:
        q1 = nhiet_do.quantile(0.25)
        q3 = nhiet_do.quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        mask = (nhiet_do < lower) | (nhiet_do > upper)

    before = nhiet_do.describe().to_dict()
    df["Outlier"] = mask
    df.loc[mask, "NhietDo"] = nhiet_do.median()
    after = pd.to_numeric(df["NhietDo"], errors="coerce").describe().to_dict()

    if output_csv:
        df.to_csv(output_csv, index=False, encoding="utf-8-sig")

    thong_ke = {
        "outlier_count": int(mask.sum()),
        "before_mean": float(before.get("mean", np.nan)),
        "after_mean": float(after.get("mean", np.nan)),
    }
    return df, thong_ke


def bai9_ve_boxplot(input_csv: str | Path | None = None, image_path: str = "boxplot_nhietdo.png"):
    if input_csv is None:
        input_csv = _data_path("moitruong.csv")
    df = pd.read_csv(input_csv)
    vals = pd.to_numeric(df["NhietDo"], errors="coerce").dropna()
    plt.figure(figsize=(6, 4))
    plt.boxplot(vals)
    plt.title("Boxplot NhietDo")
    plt.ylabel("NhietDo")
    plt.savefig(image_path, dpi=120, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    df, stats = bai9_xu_ly_ngoai_le()
    bai9_ve_boxplot(None)
    print(df)
    print(stats)
