n = int(input('Nhập số tự nhiên n: '))
for k in range(1,n+1):
    if n%k == 0:
        print(k, end=' ')

'''
n = 6
range(1,7): 1 2 3 4 5 6
Lần 1 (k = 1): In '1 '
Lần 2 (k = 2): In '2 '
Lần 3 (k = 3): In '3 '
Lần 4 (k = 4):
Lần 5 (k = 5):
Lần 6 (k = 6): In '6 '

'1 2 3 6 '
'''
