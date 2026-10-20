def ReadDaTa(file:str):
    f = open(file, 'r')
    n = int(f.readline())
    lst = []
    for i in f.readline().split():
        lst.append(int(i))
    f.close()
    return n, lst

def WriteDaTa(file:str, content:int):
    f = open(file,'w')
    f.write(str(content))
    f.close()

fIn = 'D:\\GitHub\\ezProgramming\\src\\Exams\\KhanhHoa_(23-24)\\CuaSo\\Test1.inp'
fOut = 'D:\\GitHub\\ezProgramming\\src\\Exams\\KhanhHoa_(23-24)\\CuaSo\\Test1.out'

n, lst = ReadDaTa(fIn)

lst.sort(reverse=True)
pair = []
i = 0
while i < len(lst)-1:
    if lst[i] == lst[i+1]:
        pair.append(lst[i])
        i += 2
    else:
        i += 1
        
    if len(pair) == 2:
        break

if len(pair) < 2:
    WriteDaTa(fOut, str(-1))
else:
    WriteDaTa(fOut, str((pair[0]+pair[1])*2))
print('OK!')