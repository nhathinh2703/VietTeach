s = input('Nhập các số nguyên cách nhau bởi dấu cách: ')
sline = s.split()
n = len(sline)
nline = []
for x in sline:
    nline.append(int(x))
print("Bạn đã nhập",n,"số.")
for k in nline:
    print(k, end = " ")