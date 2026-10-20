A = [1,-2,-3.5,4,6,-2.5]
# Câu a
s = 0
for i in range(len(A)):
    if A[i] > 0:
        s = s + A[i]
print(s)

# Câu b
'''
for i in range(len(A)):
    A[i] = A[i] + 3
print(A)
'''

# Câu c
k = 0
for i in range(1,4):
    if A[i] < 0:
        k = k + 1
print(k)
