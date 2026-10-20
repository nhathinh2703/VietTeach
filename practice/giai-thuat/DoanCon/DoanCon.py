# BT1. In tất cả đoạn con từ danh sách
def InDoanCon(A:list):
    for l in range(len(A)):
        for r in range(l, len(A)):
            print(A[l:r+1], sum(A[l:r+1]))

# BT2. Tổng lớn nhất của đoạn con
def TongDoanLonNhat(A:list):
    i, j, max = 0, 0, sum(A[0:1])
    # Duyệt các đoạn để tìm đoạn có tổng lớn nhất lưu vào max
    for l in range(len(A)):
        for r in range(l, len(A)):
            if sum(A[l:r+1]) > max:
                i, j, max = l, r, sum(A[l:r+1])
    return A[i:j+1], max

# BT3. Đếm số đoạn con có tổng chia hết cho k
def DemSoDoanChiaHetChoK(A:list, k:int):
    dem = 0
    for l in range(len(A)):
        for r in range(l, len(A)):
            if sum(A[l:r+1]) % k == 0:
                dem += 1
    # Duyệt l từ đầu đến cuối danh sách A:
        # Duyệt r từ l đến cuối danh sách A:
            # Nếu tổng đoạn con đang xét chia hết cho k:
                # Tăng dem 1 đơn vị
    return dem

# BT4. Đoạn con dài nhất có tổng ≤ S

# BT5. Tích lớn nhất của đoạn con

A = [3,-9,5,2]
print('BT1-Tất cả đoạn con:')
InDoanCon(A)

AMax, max = TongDoanLonNhat(A)
print('BT2-Tổng đoạn lớn nhất:',AMax,max)

k = int(input('Nhập số nguyên k: '))
print(f'BT3-Số đoạn con có tổng chia hết cho {k} là: {DemSoDoanChiaHetChoK(A,k)}')