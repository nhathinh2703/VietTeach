dsLop = []
n = int(input("Nhập số học sinh trong lớp: "))
for i in range(n):
    name = input("Nhập họ tên học sinh thứ " + str(i+1)+":")
    dsLop.append(name)
print("Danh sách học sinh đã nhập:")
for i in range(len(dsLop)):
    print(dsLop[i], end = " ")