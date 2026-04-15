import pandas as pd


def main():
    df = pd.read_csv("student_performance_dirty.csv")

    df["full_name"] = (
        df["full_name"].astype("string")
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
        .str.title()
    )

    email_mask = df["email"].astype("string").str.contains(
        r"^[\w\.-]+@[\w\.-]+\.\w+$", regex=True, na=False
    )
    print("===== Invalid email rows =====")
    print(df.loc[~email_mask, ["student_id", "email"]])

    df["phone"] = (
        df["phone"].astype("string")
        .str.replace(r"\D", "", regex=True)
        .replace({"": "Chưa cập nhật"})
    )

    print("\n===== Phone sample after normalization =====")
    print(df[["student_id", "phone"]])


if __name__ == "__main__":
    main()
