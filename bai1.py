import numpy as np

print("=" * 70)
print("BÀI 1: PHÂN TÍCH ĐIỂM HỌC PHẦN THEO MIỀN GIÁO DỤC")
print("=" * 70)

# Dữ liệu đầu vào
scores = np.array([
    [8.0, 7.5, 8.5, 7.0],
    [6.5, 6.0, 7.0, 6.5],
    [9.0, 8.5, 9.0, 8.5],
    [5.0, 5.5, 6.0, 5.5],
    [7.5, 7.0, 8.0, 7.5],
    [4.5, 5.0, 5.5, 5.0],
    [8.5, 9.0, 8.0, 9.0],
    [6.0, 6.5, 6.0, 6.5],
    [7.0, 7.5, 7.0, 8.0],
    [9.5, 9.0, 9.5, 9.0]
])

weights = np.array([0.1, 0.2, 0.3, 0.4])  # Chuyên cần, Giữa kỳ, Thực hành, Cuối kỳ

print("\n1. MA TRẬN ĐIỂM VÀ THÔNG TIN CÂU TRÚC")
print("-" * 70)
print("Dữ liệu đầu vào (Ma trận điểm 10 sinh viên x 4 cột):")
print("Cột 0: Chuyên cần | Cột 1: Giữa kỳ | Cột 2: Thực hành | Cột 3: Cuối kỳ")
print(scores)
print(f"\nShape: {scores.shape}")
print(f"Ndim: {scores.ndim}")
print(f"Dtype: {scores.dtype}")
print("\nNhận xét: Ma trận có 10 hàng (sinh viên) và 4 cột (thành phần điểm).")
print("Dữ liệu là số thực (float64), cho phép các phép tính toán học chính xác.")

# ====================================================================================
print("\n2. ĐIỂM TỔNG KẾT THEO TRỌNG SỐ")
print("-" * 70)
print(f"Trọng số: Chuyên cần=10%, Giữa kỳ=20%, Thực hành=30%, Cuối kỳ=40%")
final_score = scores @ weights
print("\nĐiểm tổng kết cho mỗi sinh viên:")
for i, score in enumerate(final_score):
    print(f"Sinh viên {i+1}: {score:.2f}")

# ====================================================================================
print("\n3. XẾP LOẠI SINH VIÊN")
print("-" * 70)
# A: >= 8.5, B: 7.0-8.5, C: 5.0-7.0, D: < 5.0
def classify_grade(score):
    if score >= 8.5:
        return 'A'
    elif score >= 7.0:
        return 'B'
    elif score >= 5.0:
        return 'C'
    else:
        return 'D'

grades = np.array([classify_grade(s) for s in final_score])
print("Xếp loại (A >= 8.5, B: 7.0-8.5, C: 5.0-7.0, D < 5.0):")
for i, (score, grade) in enumerate(zip(final_score, grades)):
    print(f"Sinh viên {i+1}: {score:.2f} ({grade})")

# ====================================================================================
print("\n4. TÌM SINH VIÊN CÓ ĐIỂM TỔNG KẾT CAO NHẤT VÀ THẤP NHẤT")
print("-" * 70)
max_idx = np.argmax(final_score)
min_idx = np.argmin(final_score)
print(f"Sinh viên có điểm cao nhất: Sinh viên {max_idx+1} với điểm {final_score[max_idx]:.2f}")
print(f"Sinh viên có điểm thấp nhất: Sinh viên {min_idx+1} với điểm {final_score[min_idx]:.2f}")
print(f"\nNhận xét: Độ chênh lệch điểm tổng kết là {final_score[max_idx] - final_score[min_idx]:.2f}.")
print(f"Điều này cho thấy có sự phân hóa giữa các sinh viên trong lớp.")

# ====================================================================================
print("\n5. LỌC SINH VIÊN CÓ ĐIỂM TỔNG KẾT TỪ 7.0 TRỞ LÊN")
print("-" * 70)
pass_filter = final_score >= 7.0
passed_students = np.where(pass_filter)[0]
print(f"Sinh viên đạt loại >= 7.0: {passed_students + 1}")
print(f"Danh sách chi tiết:")
for idx in passed_students:
    print(f"  Sinh viên {idx+1}: {final_score[idx]:.2f}")
print(f"\nNhận xét: Có {len(passed_students)} sinh viên đạt điểm từ 7.0 trở lên, ")
print(f"chiếm {len(passed_students)/len(final_score)*100:.1f}% lớp.")

# ====================================================================================
print("\n6. PHÁT HIỆN SINH VIÊN CÓ ÍT NHẤT MỘT THÀNH PHẦN ĐIỂM DƯỚI 5.0")
print("-" * 70)
low_component = np.any(scores < 5.0, axis=1)
low_students = np.where(low_component)[0]
print(f"Sinh viên có thành phần điểm dưới 5.0: {low_students + 1}")
print(f"Danh sách chi tiết:")
for idx in low_students:
    problem_cols = np.where(scores[idx] < 5.0)[0]
    col_names = ['Chuyên cần', 'Giữa kỳ', 'Thực hành', 'Cuối kỳ']
    print(f"  Sinh viên {idx+1}: Thành phần yếu - {', '.join([col_names[c] + f' ({scores[idx, c]:.1f})' for c in problem_cols])}")
print(f"\nNhận xét: {len(low_students)} sinh viên có thành phần điểm dưới 5.0 và cần")
print(f"được hỗ trợ bổ sung kiến thức.")

# ====================================================================================
print("\n7. SẮP XẾP VÀ TÌM 3 SINH VIÊN ĐỨNG ĐẦU")
print("-" * 70)
rank_idx = np.argsort(final_score)[::-1]
top3 = rank_idx[:3]
print("Xếp hạng sinh viên theo điểm tổng kết (cao đến thấp):")
for rank, idx in enumerate(rank_idx, 1):
    print(f"  {rank}. Sinh viên {idx+1}: {final_score[idx]:.2f}")

print(f"\n3 sinh viên đứng đầu:")
for rank, idx in enumerate(top3, 1):
    print(f"  {rank}. Sinh viên {idx+1} - {final_score[idx]:.2f}")
print(f"\nNhận xét: 3 sinh viên đứng đầu đều có điểm từ 8.5 trở lên, ")
print(f"thể hiện khả năng học tập xuất sắc.")

# ====================================================================================
print("\n8. CHUẨN HÓA ĐIỂM CUỐI KỲ THEO Z-SCORE")
print("-" * 70)
final_exam = scores[:, 3]
mean_final = final_exam.mean()
std_final = final_exam.std()
z_final_exam = (final_exam - mean_final) / std_final

print(f"Thống kê điểm cuối kỳ (cột 3):")
print(f"  Trung bình: {mean_final:.2f}")
print(f"  Độ lệch chuẩn: {std_final:.2f}")
print(f"\nDiểm cuối kỳ Z-score cho mỗi sinh viên:")
for i, (score, z) in enumerate(zip(final_exam, z_final_exam)):
    print(f"  Sinh viên {i+1}: Điểm gốc={score:.1f}, Z-score={z:+.3f}")

print(f"\nNhận xét: Độ lệch chuẩn (~1.05) cho thấy mức độ phân hóa vừa phải,")
print(f"các sinh viên có điểm cuối kỳ tương đối cân bằng nhưng có sự khác biệt rõ ràng.")

print("\n" + "=" * 70)
