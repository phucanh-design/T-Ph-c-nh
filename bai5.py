import numpy as np
import pandas as pd


def main():
    df = pd.read_csv("student_performance_dirty.csv")

    invalid_score = ~df["score_python"].between(0, 10)
    print("===== Invalid scores =====")
    print(df.loc[invalid_score, ["student_id", "score_python"]])

    df.loc[invalid_score, "score_python"] = np.nan
    df["score_python"] = df["score_python"].fillna(df["score_python"].median())

    print("\n===== Score sample after correction =====")
    print(df[["student_id", "score_python"]])


if __name__ == "__main__":
    main()
