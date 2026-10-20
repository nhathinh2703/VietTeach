s = input('Nhập xâu s: ')
dem = 0
for i in range(ord('a'),ord('z')+1):
    if s.count(chr(i)) == 2:
        dem += 1
if dem == 0:
    print(-1)
else:
    print(dem)