import pandas as pd


def main():
    df = pd.read_csv("student_performance_dirty.csv")

    q1 = df["attendance_rate"].quantile(0.25)
    q3 = df["attendance_rate"].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    outlier_df = df[(df["attendance_rate"] < lower) | (df["attendance_rate"] > upper)]
    print("===== Attendance rate outliers =====")
    print(outlier_df[["student_id", "attendance_rate"]])


if __name__ == "__main__":
    main()
