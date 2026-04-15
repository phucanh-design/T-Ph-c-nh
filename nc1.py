import pandas as pd


def clean_gender(series: pd.Series) -> pd.Series:
    return (
        series.astype("string")
        .str.strip()
        .str.lower()
        .replace({"nam": "Nam", "nữ": "Nữ", "nu": "Nữ", "n": "Nữ"})
        .fillna("Không rõ")
    )


def clean_phone(series: pd.Series) -> pd.Series:
    cleaned = series.astype("string").str.replace(r"\D", "", regex=True)
    return cleaned.replace({"": "Chưa cập nhật"})


def main():
    df = pd.read_csv("student_performance_dirty.csv")

    df["gender"] = clean_gender(df["gender"])
    df["phone"] = clean_phone(df["phone"])

    print("===== Cleaned gender and phone =====")
    print(df[["student_id", "gender", "phone"]])


if __name__ == "__main__":
    main()
