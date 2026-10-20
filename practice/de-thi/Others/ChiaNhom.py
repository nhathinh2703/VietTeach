import random

# Danh sách học sinh từ 1 đến 35
students = list(range(1, 36))

# Xáo trộn ngẫu nhiên danh sách
random.shuffle(students)

groups = []

# Tạo 16 nhóm, mỗi nhóm 2 học sinh
for i in range(16):
    group = students[i*2:(i+1)*2]
    groups.append(group)

# Nhóm cuối cùng (nhóm 17) gồm 3 học sinh còn lại
groups.append(students[32:])

# In kết quả
for idx, group in enumerate(groups, start=1):
    print(f"Nhóm {idx}: {group}")
