def ReadFile(filePath: str):
    with open(file=filePath, mode="r", encoding="utf-8") as f:
        n = int(f.readline())
    return n

def WriteFile(filePath: str, content: str):
    with open(file=filePath, mode="w", encoding="utf-8") as f:
        f.write(content)

fIn = 'D:\\GitHub\\ezProgramming\\src\\Exams\\LaoCai_(25-26)\\Bai1\\test1.inp'
fOut = 'D:\\GitHub\\ezProgramming\\src\\Exams\\LaoCai_(25-26)\\Bai1\\test1.out'
n = ReadFile(fIn)

while len(str(n)) > 1:
    tong = 0
    for i in str(n):
        tong += int(i)
    
    n = tong

print(n)
WriteFile(fOut, str(n))