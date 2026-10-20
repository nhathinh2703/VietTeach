'''
Viết chương trình đọc từ tệp STRING.INP một xâu ký tự (chỉ gồm chữ cái và khoảng trắng).
Hãy tìm từ dài nhất trong xâu và ghi ra tệp STRING.OUT từ đó cùng với độ dài của nó.
Nếu có nhiều từ dài nhất bằng nhau, ghi ra từ xuất hiện đầu tiên.
'''

def ReadFile(filePath:str):
    with open(file=filePath, mode='r', encoding='utf-8') as f:
        s = f.readline()
    return s

def WriteFile(filePath:str, content: str):
    with open(file=filePath, mode='w', encoding='utf-8') as f:
        f.write(content)

def FindIndexWord(A:list):
    first = 0
    last = 0
    for i in range(1,len(A)):
        if len(A[i]) > len(A[first]):
            first = i

        if len(A[i]) >= len(A[last]):
            last = i
    return first, last

f = 'D:\\GitHub\\ezProgramming\\src\\Exams\\Others\\String1\\test1'

s = ReadFile(f + '.inp')
A = s.split()
first, last = FindIndexWord(A)
WriteFile(f + '.out', A[first] + ' ' + str(len(A[last])))