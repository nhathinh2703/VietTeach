'''
Tìm số có đúng k ước số trong đoạn [a,b].

Thuật toán:
B1. Định nghĩa hàm DemUoc(n:int) -> Số ước của số n
B2. Nhập các số nguyên a, b, k từ bàn phím; tạo danh sách ds = []
B3. Duyệt i từ a đến b:
        Nếu DemUoc(i) == k:
            Số i là số cần tìm -> thêm số i vào ds
B4. In ds
'''