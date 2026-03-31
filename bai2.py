import numpy as np

print("=" * 70)
print("BÀI 2: PHÂN TÍCH CHUYÊN CẦN VÀ CẢNH BÁO HỌC VỤ")
print("=" * 70)

# 1. TẠO MA TRẬN CHUYÊN CẦN
attendance = np.array([
    [1,1,1,1,1,1,1,1],
    [1,1,0,1,1,0,1,1],
    [1,0,0,1,1,1,0,1],
    [1,1,1,1,0,1,1,1],
    [0,1,1,0,1,1,1,0],
    [1,1,1,1,1,1,0,1],
    [1,0,1,0,1,0,1,0],
    [1,1,1,1,1,1,1,0],
    [0,0,1,1,0,1,1,1],
    [1,1,1,0,1,1,1,1],
    [1,1,0,0,1,0,1,1],
    [1,1,1,1,1,0,1,1]
])

present_count = attendance.sum(axis=1)
print("\n1. Tổng số buổi đi học của từng sinh viên:")
for i, c in enumerate(present_count, 1):
    print(f"  Sinh viên {i}: {c}/8")

# 2. TỈ LỆ CHUYÊN CẦN
rate = present_count / attendance.shape[1] * 100
print("\n2. Tỉ lệ chuyên cần (%):")
for i, r in enumerate(rate, 1):
    print(f"  Sinh viên {i}: {r:.1f}%")

# 3. CẢNH BÁO HỌC VỤ
warning_idx = np.where(rate < 75)[0]
print("\n3. Danh sách sinh viên cảnh báo (dưới 75%):")
if warning_idx.size == 0:
    print("  Không có sinh viên nào bị cảnh báo.")
else:
    print(f"  Sinh viên: {warning_idx + 1}")

# 4. BUỔI HỌC VẮNG NHIỀU NHẤT
absent_count_by_session = (attendance == 0).sum(axis=0)
worst_session = np.argmax(absent_count_by_session)
print("\n4. Buổi học có số lượng vắng nhiều nhất:")
print(f"  Buổi {worst_session + 1} với {absent_count_by_session[worst_session]} sinh viên vắng.")
print(f"  Chi tiết vắng mỗi buổi: {absent_count_by_session.tolist()}")

# 5. ĐI HỌC ĐẦY ĐỦ 8 BUỔI
full_attendance = np.where(np.all(attendance == 1, axis=1))[0]
print("\n5. Sinh viên đi học đầy đủ cả 8 buổi:")
if full_attendance.size == 0:
    print("  Không có học sinh nào đi học đầy đủ 8 buổi.")
else:
    print(f"  Sinh viên: {full_attendance + 1}")

# 6. TỪ 2 BUỔI VẮNG LIÊN TIẾP TRỞ LÊN
two_absent_in_row = np.where(np.any((attendance[:, :-1] == 0) & (attendance[:, 1:] == 0), axis=1))[0]
print("\n6. Sinh viên có từ 2 buổi vắng liên tiếp trở lên:")
if two_absent_in_row.size == 0:
    print("  Không có sinh viên nào vắng >= 2 buổi liên tiếp.")
else:
    print(f"  Sinh viên: {two_absent_in_row + 1}")

# 7. NHẬN XÉT CHUNG
print("\n7. Nhận xét chung:")
print("  - Lớp có thái độ học tập tốt nhìn chung, nhiều sinh viên duy trì tỉ lệ chuyên cần cao.")
print("  - Tuy nhiên vẫn còn một số sinh viên cần theo dõi và cảnh báo vì chuyên cần thấp (<75%).")
print("  - Điều này cho thấy cần giải pháp hỗ trợ kịp thời để giữ ổn định chất lượng lớp.")

print("\n" + "=" * 70)
