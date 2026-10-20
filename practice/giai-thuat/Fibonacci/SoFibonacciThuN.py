'''
Dãy Fibonacci được định nghĩa bởi công thức truy hồi: 
F(0)=0, F(1)=1, và F(n)=F(n−1)+F(n−2) với n≥2.

B1. Tìm số Fibonacci thứ N → Viết hàm trả về số Fibonacci tại vị trí N.

B2. Tổng N số Fibonacci đầu tiên → Tính tổng của N số đầu tiên trong dãy Fibonacci.

Gợi ý:
1. Nhập vào số nguyên N từ bàn phím
2. Tìm dãy Fibonacci N số (lưu trong danh sách)
Khởi tạo F = [0,1]
Lặp i từ 2 đến n-1:
    Thêm (F[i-1] + F[i-2]) vào danh sách F
3. In ra phần tử thứ (N-1) của danh sách.
'''
# Hàm trả về dãy N số Fibonacci
def Fibonacci(N:int):
    F = [0,1]
    for i in range(2,N):
        F.append(F[i-1] + F[i-2])
    return F

N = int(input('Nhập số nguyên N: '))
F = Fibonacci(N)
print(F)
print('Bài 1:', F[len(F)-1])
print('Bài 2:', sum(F))