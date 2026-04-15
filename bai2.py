import pandas as pd


def main():
    df = pd.read_csv("student_performance_dirty.csv")

    df["class_name"] = (
        df["class_name"].astype("string")
        .str.replace("-", " ", regex=False)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
        .str.upper()
        .replace({"CNTT1": "CNTT 1", "CNTT2": "CNTT 2", "CNTT3": "CNTT 3"})
    )

    df["gender"] = (
        df["gender"].astype("string")
        .str.strip()
        .str.lower()
        .replace({"nam": "Nam", "nữ": "Nữ", "nu": "Nữ", "n": "Nữ"})
    )

    print(df[["student_id", "class_name", "gender"]])


if __name__ == "__main__":
    main()
