'''
Cho một số tiền cần rút từ ATM và danh sách các mệnh giá tiền mà ATM hiện có.
Hãy đổi số tiền đó thành ít tờ nhất.
** Input:
Dòng 1: Số nguyên N — số tiền cần rút.
Dòng 2: Danh sách các mệnh giá tiền mà ATM có (cách nhau bởi khoảng trắng).

** Output
Một số nguyên — số lượng tờ tiền ít nhất cần dùng để đổi ra số tiền N.
'''
# B1. Đọc từ tệp n và danh sách A chứa các mệnh giá
# B2. Sắp xếp A giảm dần (mệnh giá giảm dần)
# B3. 
# - Tạo biến soTo = 0
# - Duyệt i theo danh sách mệnh giá:
#       soTo = n chia lấy phần nguyên cho mệnh giá i
#       n = n % i
# B4. Ghi soTo vào tệp

def ReadData(file:str):
    with open(file, "r", encoding="utf-8") as f:
        n = int(f.readline())
        A = list(map(int,f.readline().split()))
    return n, A

def WriteData(file:str, content:str):
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

fIn = 'D:\\GitHub\\ezProgramming\\src\\Algorithm\\Greedy\\DoiTien\\test2.inp'
n, A = ReadData(fIn)

A.sort(reverse=True)
print(n)
print(A)

soTo, B = 0, []
for i in A:
    soTo += n // i
    B.append(n // i)
    n = n % i

print(soTo)
print(B)