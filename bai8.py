import pandas as pd


def main():
    df = pd.read_csv("student_performance_dirty.csv")

    bins = [0, 5, 6.5, 8, 10]
    labels = ["Yếu", "Trung bình", "Khá", "Giỏi"]
    df["level"] = pd.cut(df["score_python"], bins=bins, labels=labels, include_lowest=True)

    print(df[["student_id", "score_python", "level"]])


if __name__ == "__main__":
    main()
