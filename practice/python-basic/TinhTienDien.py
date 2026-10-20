k = float(input('Nhập số kWh điện tiêu thụ: '))
if k <= 50:
    t = k*1.678
if 50 < k <= 100:
    t = 50*1.678 + (k-50)*1.734
if k > 100:
    t = 50*1.678 + 50*1.734 + (k-100)*2.014
print(f'Số tiền điện phải trả: {t} nghìn đồng')
