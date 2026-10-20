def ReadData(path:str):
    f = open(path, 'r')
    ds = f.read().split('\n')
    # ds = f.readlines()
    f.close()
    return ds

fIn = 'D:\\GitHub\\ezProgramming\\src\\Exams\\QuyNhon_THT_2018\\Bai3.inp'
ds = ReadData(fIn)
min, max, average, sum = len(ds[0]), len(ds[0]), 0, 0
for i in ds:
    sum += len(i)
    if len(i) > max:
        max = len(i)
    if len(i) < min:
        min = len(i)
print(min)
print(max)
print(round(sum/len(ds),1))