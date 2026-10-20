def SortAscending(A:list):
    n = len(A)
    for i in range(n-1):
        for j in range(n-1-i):
            if A[j][1] > A[j+1][1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

def ReadData(file:str):
    with open(file, "r", encoding="utf-8") as f:
        n = int(f.readline())
        A = []
        for i in range(n):
            A.append(list(map(int, f.readline().split())))
    return n, A

def WriteData(file:str, content:str):
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

fIn = 'D:\\GitHub\\ezProgramming\\src\\Algorithm\\Greedy\\test2.inp'
fOut = 'D:\\GitHub\\ezProgramming\\src\\Algorithm\\Greedy\\test2.out'
n, A = ReadData(fIn)

SortAscending(A)
last_end = 0
count = 0
ds = []
for s,e in A:
    if s >= last_end:
        count += 1
        ds.append((s,e))
        last_end = e

print(count)
print(ds)
WriteData(fOut, str(count))