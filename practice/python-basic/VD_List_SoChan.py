# # 1a)
# A =[3,2,1,5,6,10,7,12,18]
# S = 0
# for i in range(len(A)):
#     if A[i] > 0:
#         S = S + A[i]
# print(S)
# # 1b)
# A =[3,2,1,5,6,10,7,12,18]
# C = 0
# for i in range(len(A)):
#     if A[i] > 0:
#         C = C + 1
# print(C)
# 2
import random

# print(random.randint(10,100))

A = []
for i in range(10):
    A.append(random.randint(10,100))
print(A)

for i in range(len(A)):
    if A[i] % 2 == 0:
        print(A[i])
