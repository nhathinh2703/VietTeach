A = [3,7,5,9,0,-6,20,-15]
print('Duyệt và in tiến:')
i = 0
while i <= len(A)-1:
    print(A[i], end = ' ')
    i += 1

print('\nDuyệt và in lùi:')
i = len(A)-1
while i >= 0:
    print(A[i], end = ' ')
    i -= 1
