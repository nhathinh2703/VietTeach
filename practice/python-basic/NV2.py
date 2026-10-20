n = int(input('Nhập số tự nhiên n: '))
count = 0
for k in range(1,n):
    if n%k == 0:
        count = count + 1
print(count)

'''
Bộ nhớ: n = 6
Bộ nhớ: count = 3
range(1,6): 1 2 3 4 5

Lần 1 (k = 1): Đk Đúng -> count = 0 + 1 = 1
Lần 2 (k = 2): Đk Đúng -> count = 1 + 1 = 2
Lần 3 (k = 3): Đk Đúng -> count = 2 + 1 = 3
Lần 4 (k = 4): Đk Sai
Lần 5 (k = 5): Đk Sai

Màn hình:
3
'''
