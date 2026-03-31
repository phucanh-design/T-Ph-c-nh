import numpy as np

print("=" * 70)
print("BÀI 3: PHÂN TÍCH DOANH THU BÁN HÀNG THEO MIỀN KINH DOANH")
print("=" * 70)

# 1. TẠO MA TRẬN DOANH THU VÀ TỔNG THEO NGÀY
sales = np.array([
    [120, 150, 130, 140, 160],
    [125, 145, 128, 142, 158],
    [130, 155, 135, 150, 162],
    [135, 160, 140, 152, 168],
    [140, 165, 145, 155, 170],
    [138, 162, 142, 153, 169],
    [145, 170, 150, 160, 175]
])

daily_total = sales.sum(axis=1)
print("\n1. Tổng doanh thu theo từng ngày:")
for i, total in enumerate(daily_total, 1):
    print(f"  Ngày {i}: {total}")

# 2. TỔNG VÀ TRUNG BÌNH THEO SẢN PHẨM
product_total = sales.sum(axis=0)
product_mean = sales.mean(axis=0)
print("\n2. Tổng và doanh thu trung bình theo sản phẩm:")
for j in range(sales.shape[1]):
    print(f"  Sản phẩm {j + 1}: tổng={product_total[j]}, trung bình={product_mean[j]:.2f}")

# 3. NGÀY DOANH THU CAO NHẤT VÀ SẢN PHẨM BÁN TỐT NHẤT
best_day = np.argmax(daily_total) + 1
best_product = np.argmax(product_total) + 1
print("\n3. Ngày có doanh thu cao nhất và sản phẩm bán tốt nhất:")
print(f"  Ngày cao nhất: Ngày {best_day} với {daily_total[best_day - 1]}")
print(f"  Sản phẩm tốt nhất: Sản phẩm {best_product} với tổng {product_total[best_product - 1]}")

# 4. TĂNG DOANH SỐ SẢN PHẨM 2 VÀ 5 8%
new_sales = sales.astype(float).copy()
new_sales[:, [1, 4]] *= 1.08
print("\n4. Doanh thu sau điều chỉnh (sản phẩm 2 và 5 +8%):")
print(new_sales)

# 5. SO SÁNH TỔNG TOÀN TUẦN TRƯỚC VÀ SAU ĐIỀU CHỈNH
before_total = sales.sum()
after_total = new_sales.sum()
print("\n5. Tổng doanh thu toàn tuần trước và sau điều chỉnh:")
print(f"  Trước điều chỉnh: {before_total:.2f}")
print(f"  Sau điều chỉnh: {after_total:.2f}")

# 6. NGÀY CÓ TỔNG DOANH THU > TRUNG BÌNH TOÀN TUẦN
mean_week = daily_total.mean()
high_days = np.where(daily_total > mean_week)[0] + 1
print("\n6. Ngày có tổng doanh thu lớn hơn trung bình toàn tuần:")
if high_days.size == 0:
    print("  Không có ngày nào cao hơn trung bình.")
else:
    print(f"  Ngày: {high_days.tolist()}")

# 7. SẢN PHẨM ỔN ĐỊNH NHẤT (ĐỘ LỆCH CHUẨN NHỎ NHẤT)
stable_product = np.argmin(sales.std(axis=0)) + 1
print("\n7. Sản phẩm có độ ổn định cao nhất:")
print(f"  Sản phẩm {stable_product} với độ lệch chuẩn {sales.std(axis=0)[stable_product - 1]:.2f}")

# 8. NHẬN XÉT CHUNG
print("\n8. Nhận xét:")
print("  - Doanh thu được duy trì tốt qua 7 ngày; ngày 7 là cao nhất nên cần đảm bảo hàng tồn để tận dụng.")
print("  - Sản phẩm bán tốt nhất là sản phẩm", best_product, "không chỉ có tổng doanh thu cao mà còn độ ổn định tốt.")
print("  - Ưu tiên gia tăng quảng bá sản phẩm 2 và 5 do mức tăng 8% có ảnh hưởng rõ rệt lên tổng doanh thu.")

print("\n" + "=" * 70)
