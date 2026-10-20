# Sơ Đồ Tư Duy - Tin Học 10: Bài 4

> **Bài 4: Hệ nhị phân và dữ liệu số nguyên**  
> *Chương trình GDPT 2018 - Bộ sách Kết nối tri thức với cuộc sống (Chủ đề 1: Máy tính và xã hội tri thức)*

---

## 1. Sơ đồ tư duy dạng Mermaid (Trực quan hóa kiến thức)

```mermaid
mindmap
  root((BÀI 4: HỆ NHỊ PHÂN VÀ DỮ LIỆU SỐ NGUYÊN))

    Hệ đếm nhị phân (Binary)
      Khái niệm
        Hệ đếm cơ số 2, chỉ dùng 2 chữ số: 0 và 1
        Mỗi vị trí tương ứng lũy thừa của 2 (từ phải sang trái: 2^0, 2^1, 2^2...)
      Chuyển đổi Nhị phân sang Thập phân
        Nhân từng chữ số nhị phân với lũy thừa cơ số 2 tương ứng rồi cộng lại
        Ví dụ: 1011_2 = 1*2^3 + 0*2^2 + 1*2^1 + 1*2^0 = 8 + 0 + 2 + 1 = 11_10
      Chuyển đổi Thập phân sang Nhị phân
        Chia liên tiếp cho 2 và lấy phần dư theo thứ tự ngược lại
        Ví dụ: 13 chia 2 dư 1, 6 chia 2 dư 0, 3 chia 2 dư 1, 1 chia 2 dư 1 => 1101_2
    Các phép toán số học nhị phân
      Phép cộng nhị phân
        0 + 0 = 0
        0 + 1 = 1 ; 1 + 0 = 1
        1 + 1 = 10 (viết 0 nhớ 1)
        1 + 1 + 1 = 11 (viết 1 nhớ 1)
      Phép nhân nhị phân
        0 * 0 = 0 ; 0 * 1 = 0 ; 1 * 0 = 0
        1 * 1 = 1
    Biểu diễn số nguyên trong máy tính
      Số nguyên không dấu: Dùng n bit biểu diễn dải giá trị từ 0 đến 2^n - 1
      Số nguyên có dấu: Dùng bit dấu (bit cao nhất: 0 là dương, 1 là âm) hoặc mã bù 2
    
```

---

## 2. Tóm tắt nhanh cốt lõi ghi nhớ (Flashcard dạng bảng)

| Khái niệm cốt lõi | Nội dung trọng tâm cần nhớ |
| :--- | :--- |
| **Hệ nhị phân** | Cơ số 2, dùng hai chữ số 0 và 1. Là ngôn ngữ nền tảng của phần cứng máy tính. |
| **Đổi nhị phân - thập phân** | Nhị phân -> thập phân bằng tổng lũy thừa 2; Thập phân -> nhị phân bằng chia 2 lấy dư ngược. |
| **Cộng nhị phân** | 1 + 1 = 0 nhớ 1 (10). 1 + 1 + 1 = 1 nhớ 1 (11). |

---

## 3. Liên kết bài học trực tuyến
👉 [Mở bài học tương tác trực tuyến](../../lessons/lop-10/bai-04.html)
