'''
Nhập một số nguyên, cho biết số đó có bao nhiêu chữ số và tính tổng các chữ số đó
'''
n=int(input("n="))
if n<0:
    n = -n
dem = 0
tong = 0         
for i in str(n):
    dem+=1
    tong+=int(i)
print(dem)
print(tong)