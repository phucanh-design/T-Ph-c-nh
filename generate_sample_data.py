import pandas as pd

def main():
    data = [
        ["SV001", "Nguyen Van An", "CNTT 1", "Nam", "2004-01-12",
         "an01@eaut.edu.vn", "0912345678", 8.5, 92, "Da nop"],
        ["SV002", "Tran Thi Binh", "CNTT1", "Nữ", "2004/03/04",
         "binh02@eaut.edu.vn", "0988123456", 7.2, 88, "Chua nop"],
        ["SV003", "Le Van Cuong", "CNTT 2", "nam", "12-07-2004",
         "cuong03@email.com", None, 9.1, 95, "Da nop"],
        ["SV004", "Pham Thi Dung", "CNTT 2", None, "2004-05-21",
         "dung04@email.com", "0912.567.890", 6.8, 79, "Da nop"],
        ["SV005", "Hoang Minh Duc", "CNTT-3", "Nam ", "2004-11-02",
         "duc05@email.com", " 0977555333 ", 11.0, 85, "Da nop"],
        ["SV005", "Hoang Minh Duc", "CNTT-3", "Nam ", "2004-11-02",
         "duc05@email.com", " 0977555333 ", 11.0, 85, "Da nop"],
        ["SV006", "Vu Thi Ha", "CNTT 3", "Nu", None, "ha06@email",
         "0966888777", 5.4, 61, "Chua nop"],
        ["SV007", "Doan Quoc Huy", "CNTT 1", "NAM", "2004-08-16",
         "huy07@email.com", "0933444555", -1.0, 98, "Da nop"],
        ["SV008", "Bui Thu Linh", "CNTT 2", "Nữ", "2004-09-30",
         "linh08@email.com", "0944333222", 8.0, None, "Da nop"],
        ["SV009", "Nguyen Van Nam", "CNTT 1", "Nam", "2004-10-10",
         "nam09@email.com", "0911112222", 7.9, 82, "Tre han"],
    ]
    cols = [
        "student_id", "full_name", "class_name", "gender", "birth_date",
        "email", "phone", "score_python", "attendance_rate", "tuition_status"
    ]
    df = pd.DataFrame(data, columns=cols)
    df.to_csv("student_performance_dirty.csv", index=False, encoding="utf-8-sig")
    print("Created student_performance_dirty.csv")


if __name__ == "__main__":
    main()
