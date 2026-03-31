import numpy as np

print("=" * 70)
print("BÀI 4: QUẢN LÝ TỒN KHO VÀ ĐỀ XUẤT NHẬP HÀNG")
print("=" * 70)

# Dữ liệu đầu vào
stock = np.array([35, 8, 12, 5, 40, 18, 7, 22, 9, 15])
min_stock = np.array([20, 15, 15, 10, 25, 20, 12, 18, 12, 15])
price = np.array([30, 25, 28, 22, 35, 20, 18, 24, 19, 21])

print("\nDỮ LIỆU ĐẦU VÀO:")
print("-" * 70)
print("Tồn kho hiện tại:", stock)
print("Mức tồn tối thiểu:", min_stock)
print("Giá nhập dự kiến:", price)

# 1. Xác định các mặt hàng đang thiếu so với mức tối thiểu
print("\n1. CÁC MẶT HÀNG ĐANG THIẾU:")
print("-" * 70)
need_import = np.maximum(min_stock - stock, 0)
print("Số lượng cần nhập thêm:", need_import)
deficient_items = np.where(need_import > 0)[0]
print("Mặt hàng thiếu (chỉ số):", deficient_items + 1)  # +1 để hiển thị từ 1

# 2. Tính số lượng cần nhập thêm cho từng mặt hàng (đã tính ở trên)

# 3. Chỉ tính chi phí nhập thêm cho các mặt hàng thiếu
print("\n3. CHI PHÍ NHẬP THÊM CHO MẶT HÀNG THIẾU:")
print("-" * 70)
cost = need_import * price
print("Chi phí nhập cho từng mặt hàng:", cost)

# 4. Tính tổng chi phí nhập hàng
print("\n4. TỔNG CHI PHÍ NHẬP HÀNG:")
print("-" * 70)
total_cost = cost.sum()
print(f"Tổng chi phí: {total_cost}")

# 5. Phân loại trạng thái mỗi mặt hàng
print("\n5. TRẠNG THÁI MỖI MẶT HÀNG:")
print("-" * 70)
status = np.where(stock < min_stock, "Thiếu hàng", "Đủ hàng")
for i, stat in enumerate(status):
    print(f"Mặt hàng {i+1}: {stat}")

# 6. Tìm 3 mặt hàng thiếu nhiều nhất
print("\n6. 3 MẶT HÀNG THIẾU NHIỀU NHẤT:")
print("-" * 70)
top3_shortage = np.argsort(need_import)[::-1][:3]
print("Chỉ số mặt hàng thiếu nhiều nhất:", top3_shortage + 1)
print("Số lượng thiếu tương ứng:", need_import[top3_shortage])

# 7. Giới hạn số lượng nhập tối đa mỗi mặt hàng là 20 đơn vị
print("\n7. GIỚI HẠN SỐ LƯỢNG NHẬP TỐI ĐA 20 ĐƠN VỊ:")
print("-" * 70)
limited_need = np.clip(need_import, 0, 20)
print("Số lượng cần nhập sau giới hạn:", limited_need)

# 8. Tính lại tổng chi phí sau khi giới hạn lượng nhập
print("\n8. TỔNG CHI PHÍ SAU KHI GIỚI HẠN:")
print("-" * 70)
limited_total_cost = (limited_need * price).sum()
print(f"Tổng chi phí sau giới hạn: {limited_total_cost}")

# 9. Nhận xét ngắn về mức độ thiếu hụt của kho
print("\n9. NHẬN XÉT VỀ MỨC ĐỘ THIẾU HỤT:")
print("-" * 70)
total_shortage = need_import.sum()
num_deficient = len(deficient_items)
print(f"Tổng số mặt hàng thiếu: {num_deficient}/10")
print(f"Tổng số lượng thiếu: {total_shortage} đơn vị")
print(f"Tổng chi phí nhập ban đầu: {total_cost}")
print(f"Tổng chi phí sau giới hạn: {limited_total_cost}")
if num_deficient > 5:
    print("Nhận xét: Kho hàng đang trong tình trạng thiếu hụt nghiêm trọng, cần nhập hàng khẩn cấp.")
elif num_deficient > 2:
    print("Nhận xét: Kho hàng thiếu một số mặt hàng, cần bổ sung kịp thời.")
else:
    print("Nhận xét: Kho hàng tương đối ổn định, chỉ thiếu một vài mặt hàng.")