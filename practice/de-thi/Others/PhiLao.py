# def PhiLao(m,lst):
#     du = lst[0] - 2*m
#     i = 1
#     while i < len(lst):
#         tinh = lst[i] - m
#         if tinh > m:
#             tinh = tinh - m
#         if du >= tinh:
#             du = tinh
#         i += 1
#     du = du + 2*m
#     return du

# A = [20,15,10,18]
# m = 4
# print(PhiLao(m,A))

n, m = 4, 7
A = [20,15,10,18]

thap = 0
cao = max(A)
KQ = -1

while thap <= cao:
    h = (thap + cao) // 2  
    tong = 0
    for i in A:
        if i > h:
            tong += (i - h)
    if tong >= m:
        KQ = h      
        thap = h + 1
    else:
        cao = h - 1      

print(KQ)