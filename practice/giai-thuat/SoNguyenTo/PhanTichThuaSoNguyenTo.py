'''
Phân tích thừa số nguyên tố. (Một số nguyên có thể được biểu diễn dưới dạng tích của các số nguyên tố. 
Ví dụ: 60 = 2 × 2 × 3 × 5).

Ý tưởng: Chia liên tục các ước nguyên tố từ nhỏ tới lớn

B1. Nhập n từ bàn phím, khởi tạo i giá trị 2, ds rỗng
B2. Trong khi (while) i <= n đúng:
        Trong khi (while) n vẫn chia hết cho i đúng:
            Thêm số i vào ds
            Cập nhật n thành n//i
        Tăng i thêm 1 đơn vị
B3. In ds ra theo yêu cầu
'''

n, i, ds = int(input('Nhập số nguyên n: ')), 2, []
number = n
while i <= n:
    while n%i == 0:
        ds.append(str(i))
        n = n//i
    i += 1
print(f'{number} = {' x '.join(ds)}')