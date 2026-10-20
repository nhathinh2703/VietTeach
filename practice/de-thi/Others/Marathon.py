'''
B1. Nhập n
B2. Nhập n số nguyên a(i) viết cách nhau bỏi dấu cách
    Tách n số nguyên a(i) theo dấu cách, lưu vào A
B3. Xử lý:
    - Khởi tạo danh sách KQ rỗng
    - Duyệt i theo danh sách thành tích A:
        + Gán dem bằng 0
        + Duyệt k theo A:
            Nếu thành tích k <= i:
                Tăng đếm 1 đơn vị
        Lưu dem vào danh sách KQ
B4. In kết quả KQ theo yêu cầu
'''

n, KQ = input('Nhập n: '), []
A = list(map(int, input('Nhập n số nguyên: ').split()))
for i in A:
    dem = 0
    for k in A:
        if k <= i:
            dem += 1
    KQ.append(str(dem))
print('\n'.join(KQ))


# n = int(input())
# a = list(map(int, input().split()))

# A = max(a)
# dem = [0] * (A + 1)

# for x in a:
#     dem[x] += 1

# for i in range(1, A + 1):
#     dem[i] += dem[i-1]

# for x in a:
#     print(dem[x])