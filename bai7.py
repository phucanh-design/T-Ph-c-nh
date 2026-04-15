import pandas as pd


def main():
    df = pd.read_csv("student_performance_dirty.csv")

    df["birth_date"] = pd.to_datetime(df["birth_date"], errors="coerce", dayfirst=True)
    invalid_count = df["birth_date"].isna().sum()

    print(f"Invalid or unparseable birth_date values: {invalid_count}")
    print(df.loc[df["birth_date"].isna(), ["student_id", "birth_date"]])


if __name__ == "__main__":
    main()
