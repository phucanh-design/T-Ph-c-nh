import pandas as pd


def main():
    df = pd.read_csv("student_performance_dirty.csv")

    df["gender"] = (
        df["gender"].astype("string")
        .str.strip()
        .str.lower()
        .replace({"nam": "Nam", "nữ": "Nữ", "nu": "Nữ", "n": "Nữ"})
    )
    df["gender"] = df["gender"].fillna("Không rõ")

    df["attendance_rate"] = df["attendance_rate"].fillna(df["attendance_rate"].median())
    df["phone"] = df["phone"].fillna("Chưa cập nhật")

    print("===== Missing values after filling =====")
    print(df.isna().sum())
    print("\n===== Sample rows =====")
    print(df[["student_id", "gender", "attendance_rate", "phone"]])


if __name__ == "__main__":
    main()
