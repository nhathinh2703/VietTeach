def TachSo(s:str):
    kq = ''
    for i in s:
        if i >= '0' and i <= '9':
            kq += i
    return kq

def TimSoMax(s:str):
    max = s[0:3]    # max = s[0] + s[1] + s[2]    
    for i in range(1,len(s)-2):
        if s[i:i+3] > max:
            max = s[i:i+3]
    return max

s = '18HSG093dgtre90sd536'
print(TimSoMax(TachSo(s)))