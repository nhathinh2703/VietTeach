'''
    Duyệt u từ đầu đến cuối danh sách A:
        Duyệt v từ u đến cuối danh sách A:
            Nếu độ dài đoạn con >= k:
                Thêm vào ds giá trị trung bình

    Giá trị lớn nhất trong ds là đáp án bài toán
'''

def ReadDaTa(file:str):
    f = open(file, 'r', encoding='utf-8')
    ds = f.readline().split()
    A = [int(i) for i in f.readline().split()]
    f.close()
    return int(ds[0]), int(ds[1]), A

def WriteDaTa(file:str, content:str):
    f = open(file, 'w', encoding='utf-8')
    f.write(content)
    f.close()

fIn = 'D:\\GitHub\\ezProgramming\\src\\Exams\\Others\\DoanConTheoDieuKien\\Test2.inp'
fOut = 'D:\\GitHub\\ezProgramming\\src\\Exams\\Others\\DoanConTheoDieuKien\\Test2.out'

n, k, A = ReadDaTa(fIn)
kq = []
for l in range(len(A)):
    for r in range(l, len(A)):
        # A[l:r+1]: Day la doan con [l,r]
        if len(A[l:r+1]) >= k:
            kq.append(round(sum(A[l:r+1])/(r-l+1),3))
value = f'{max(kq):.3f}'
WriteDaTa(fOut,value)