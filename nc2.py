import pandas as pd


def compute_age(birth_dates: pd.Series, reference_date: pd.Timestamp = None) -> pd.Series:
    if reference_date is None:
        reference_date = pd.Timestamp.now().normalize()
    birth_dates_dt = pd.to_datetime(birth_dates, errors="coerce", dayfirst=True)
    has_had_birthday = (
        (reference_date.month > birth_dates_dt.dt.month)
        | (
            (reference_date.month == birth_dates_dt.dt.month)
            & (reference_date.day >= birth_dates_dt.dt.day)
        )
    )
    years = reference_date.year - birth_dates_dt.dt.year - (~has_had_birthday).astype(int)
    return years


def main():
    df = pd.read_csv("student_performance_dirty.csv")

    df["birth_date"] = pd.to_datetime(df["birth_date"], errors="coerce", dayfirst=True)
    df["age"] = compute_age(df["birth_date"])

    invalid_age = df["age"].isna() | (df["age"] < 10) | (df["age"] > 120)

    print("===== Age column =====")
    print(df[["student_id", "birth_date", "age"]])
    print("\n===== Invalid or unreasonable ages =====")
    print(df.loc[invalid_age, ["student_id", "age"]])


if __name__ == "__main__":
    main()
