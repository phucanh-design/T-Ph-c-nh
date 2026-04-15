import pandas as pd


def main():
    df = pd.read_csv("student_performance_dirty.csv")

    total_duplicates = df.duplicated().sum()
    duplicate_ids = df.duplicated(subset=["student_id"]).sum()
    print(f"Total fully duplicate rows: {total_duplicates}")
    print(f"Duplicate student_id rows: {duplicate_ids}")

    df = df.drop_duplicates()
    df = df.drop_duplicates(subset=["student_id"], keep="first")

    print(f"Remaining rows after deduplication: {len(df)}")
    print(df["student_id"])


if __name__ == "__main__":
    main()
