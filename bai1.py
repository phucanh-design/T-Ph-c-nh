import pandas as pd


def main():
    df = pd.read_csv("student_performance_dirty.csv")
    print("===== 5 rows =====")
    print(df.head())
    print("\n===== DataFrame info =====")
    print(df.info())
    print("\n===== Missing values per column =====")
    print(df.isna().sum())


if __name__ == "__main__":
    main()
