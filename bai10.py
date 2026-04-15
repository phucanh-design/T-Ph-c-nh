import numpy as np
import pandas as pd


def normalize_class_name(series: pd.Series) -> pd.Series:
    return (
        series.astype("string")
        .str.replace("-", " ", regex=False)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
        .str.upper()
        .replace({"CNTT1": "CNTT 1", "CNTT2": "CNTT 2", "CNTT3": "CNTT 3"})
    )


def normalize_gender(series: pd.Series) -> pd.Series:
    return (
        series.astype("string")
        .str.strip()
        .str.lower()
        .replace({"nam": "Nam", "nữ": "Nữ", "nu": "Nữ", "n": "Nữ"})
        .fillna("Không rõ")
    )


def normalize_phone(series: pd.Series) -> pd.Series:
    cleaned = series.astype("string").str.replace(r"\D", "", regex=True)
    return cleaned.replace({"": "Chưa cập nhật"})


def main():
    df = pd.read_csv("student_performance_dirty.csv")

    df["class_name"] = normalize_class_name(df["class_name"])
    df["gender"] = normalize_gender(df["gender"])
    df["attendance_rate"] = df["attendance_rate"].fillna(df["attendance_rate"].median())
    df["phone"] = normalize_phone(df["phone"])

    df = df.drop_duplicates()
    df = df.drop_duplicates(subset=["student_id"], keep="first")

    invalid_score = ~df["score_python"].between(0, 10)
    df.loc[invalid_score, "score_python"] = np.nan
    df["score_python"] = df["score_python"].fillna(df["score_python"].median())

    df["full_name"] = (
        df["full_name"].astype("string")
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
        .str.title()
    )

    df["email"] = df["email"].astype("string").str.strip()
    df["birth_date"] = pd.to_datetime(df["birth_date"], errors="coerce", dayfirst=True)

    bins = [0, 5, 6.5, 8, 10]
    labels = ["Yếu", "Trung bình", "Khá", "Giỏi"]
    df["level"] = pd.cut(df["score_python"], bins=bins, labels=labels, include_lowest=True)

    df.to_csv("student_performance_clean.csv", index=False, encoding="utf-8-sig")
    print("Da luu file student_performance_clean.csv")


if __name__ == "__main__":
    main()
