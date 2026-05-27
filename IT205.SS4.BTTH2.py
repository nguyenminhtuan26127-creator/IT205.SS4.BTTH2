target = 0
total_revenue = 0
avg_revenue = total_revenue / 7
for i in range(8):
    revenue = int(input(f"Nhập doanh thu ngày {i}: "))
    total_revenue += revenue
    if revenue >= 5000000:
        target += 1

print("--- BÁO CÁO DOANH THU TUẦN RIKKEI STORE ---")
print(f"Tổng doanh thu cả tuần: {total_revenue} VND")
avg_revenue = total_revenue / 7
print(f"Doanh thu trung bình mỗi ngày: {avg_revenue} VND")
print(f"Số ngày đạt dôanh thu mục tiêu (>= 5.000.000 VND): {target} Ngày")