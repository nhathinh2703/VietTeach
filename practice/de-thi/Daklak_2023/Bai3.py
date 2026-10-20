def ReadData(file:str):
    f = open(file, 'r')
    lst = f.readline().split()
    N, Q = int(lst[0]), int(lst[1])
    dsN = [int(i) for i in f.readline().split()]
    dsQ = []
    for i in range(Q):
        dsQ.append(f.readline())
    f.close()
    return N, Q, dsN, dsQ

def WriteData(file:str, content:str):
    f = open(file, 'w')
    f.write(content)
    f.close()

fIn = 'D:\\GitHub\\ezProgramming\\src\\Exams\\Daklak_2023\\B3.inp'
fOut = 'D:\\GitHub\\ezProgramming\\src\\Exams\\Daklak_2023\\B3.out'
N, Q, dsN, dsQ = ReadData(fIn)
dsKQ = []
for i in dsQ:
    A = str(i).split()
    L, R, S = int(A[0]), int(A[1]), int(A[2])
    # Tìm số theo yêu cầu
    soCanTim = '-1'
    for i in range(L-1,R):
        if dsN[i] >= S:
            soCanTim = str(dsN[i])
            break
    dsKQ.append(soCanTim)

WriteData(fOut, '\n'.join(dsKQ))
print('OK')