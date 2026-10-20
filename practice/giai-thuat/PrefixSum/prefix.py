def ReadData(file:str):
    with open(file, "r", encoding="utf-8") as f:
        n, q = map(int, f.readline().split())
        A = list(map(int, f.readline().split()))
        Q = []
        for i in range(q):
            Q.append(list(map(int, f.readline().split())))
    return n, q, A, Q

def WriteData(file:str, content:str):
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

fIn = 'D:\\GitHub\\ezProgramming\\src\\Algorithm\\PrefixSum\\Test2.inp'
fOut = 'D:\\GitHub\\ezProgramming\\src\\Algorithm\\PrefixSum\\Test2.out'

n, q, A, Q = ReadData(fIn)

p = [0] * len(A)
p[0] = A[0]
for i in range(1,len(A)):
    p[i] = p[i-1] + A[i]

KQ = []
for l,r in Q:
    if l == 0:
        #print(p[r])
        KQ.append(str(p[r]))
    else:
        #print(p[r]-p[l-1])
        KQ.append(str(p[r]-p[l-1]))

WriteData(fOut, '\n'.join(KQ))