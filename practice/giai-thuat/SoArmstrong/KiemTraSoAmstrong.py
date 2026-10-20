'''
Kiểm tra số N có phải là số Armstrong hay không?

B1: Nhập số nguyên N từ bàn phím.
B2: Tính biến x bằng độ dài xâu N, biến tổng (sum) bằng 0
B3: Duyệt i trong xâu N:
        Cộng thêm int(i)**x vào sum
B4: In kết quả biểu thức (tong == int(N))
'''
def SoArmstrong(n:int):
    x, sum = len(str(n)), 0
    for i in str(n):
        sum += (int(i))**x
    return sum == n

n = int(input('Nhập n = '))
print(SoArmstrong(n))