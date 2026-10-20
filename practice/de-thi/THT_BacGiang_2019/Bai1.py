def WriteData(file:str, content:str):
    f = open(file, 'w')
    f.write(content)
    f.close()
    print('OK!')

ds = []
for i in range(1000,10000):
    num = str(i)
    a = i//100
    b = i%100
    if i == (a + b)**2:
        ds.append(num)

print(ds)
fOut = 'D:\\GitHub\\ezProgramming\\src\\Exams\\THT_BacGiang_2019\\Bai1.out'
WriteData(fOut, '\n'.join(ds))