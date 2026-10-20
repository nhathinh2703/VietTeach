A = [5,9,1,-7,4]
S = 0
for i in range(len(A)):
    if A[i] > 0:
        S = S + A[i]

print(S)