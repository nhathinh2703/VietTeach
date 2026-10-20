def TongUoc(n:int):
    tong = 0
    for i in range(1,(n//2)+1):
        if n%i==0:
            tong += i
    return tong

n = int(input())

# while TongUoc(n) <= n:
#     n += 1

while True:
    if TongUoc(n) > n:
        break
    n += 1
    
print(n)