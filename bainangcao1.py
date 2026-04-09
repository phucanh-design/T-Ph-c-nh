from __future__ import annotations

from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).parent


def _full_path(file_name: str) -> Path:
    return BASE_DIR / file_name


def _check_file(path: Path) -> bool:
    if not path.exists():
        print(f"[ERROR] Khong tim thay file: {path.name}")
        return False
    return True


def bai_nang_cao_1() -> pd.DataFrame | None:
    """
    Doc students.csv va scores.xlsx, ghep theo MaSV,
    tao bang tong hop va luu tonghop_diem.xlsx.
    """
    students_path = _full_path("students.csv")
    scores_path = _full_path("scores.xlsx")

    if not (_check_file(students_path) and _check_file(scores_path)):
        return None

    students_df = pd.read_csv(students_path)

    # Thu cac ten sheet pho bien, neu khong co thi doc sheet dau tien.
    score_sheet_candidates = ["Scores", "BangDiem", "Sheet1"]
    score_sheet = None
    excel_file = pd.ExcelFile(scores_path)
    for s in score_sheet_candidates:
        if s in excel_file.sheet_names:
            score_sheet = s
            break

    if score_sheet is None:
        score_sheet = excel_file.sheet_names[0]

    scores_df = pd.read_excel(scores_path, sheet_name=score_sheet)

    if "MaSV" not in students_df.columns or "MaSV" not in scores_df.columns:
        print("[ERROR] Hai bang can cot MaSV de ghep du lieu.")
        return None

    merged = students_df.merge(scores_df, on="MaSV", how="inner")

    required_cols = ["MaSV", "HoTen", "Lop", "DiemQT", "DiemThi"]
    for col in required_cols:
        if col not in merged.columns:
            print(f"[WARN] Thieu cot {col}, gan gia tri rong.")
            merged[col] = pd.NA

    merged["DiemTongKet"] = merged[["DiemQT", "DiemThi"]].mean(axis=1, skipna=True)
    result = merged[["MaSV", "HoTen", "Lop", "DiemQT", "DiemThi", "DiemTongKet"]].copy()

    out_path = _full_path("tonghop_diem.xlsx")
    result.to_excel(out_path, index=False)

    print("Da tao bao cao tong hop diem:", out_path.name)
    print(result.head())
    return result


if __name__ == "__main__":
    bai_nang_cao_1()
