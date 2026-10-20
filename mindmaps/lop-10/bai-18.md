# Sơ Đồ Tư Duy - Tin Học 10: Bài 18

> **Bài 18: Các lệnh vào ra đơn giản**  
> *Chương trình GDPT 2018 - Bộ sách Kết nối tri thức với cuộc sống (Chủ đề 5: Lập trình Python)*

---

## 1. Sơ đồ tư duy dạng Mermaid (Trực quan hóa kiến thức)

```mermaid
mindmap
  root((BÀI 18: CÁC LỆNH VÀO RA ĐƠN GIẢN))

    Lệnh xuất dữ liệu (print)
      Cú pháp: print(giá_trị_1, giá_trị_2, ...)
      Tham số sep: Kí tự ngăn cách giữa các giá trị (mặc định là dấu cách)
      Tham số end: Kí tự kết thúc dòng (mặc định là xuống dòng \n)
    Lệnh nhập dữ liệu (input)
      Cú pháp: biến = input("Dòng thông báo: ")
      Lưu ý quan trọng: Dữ liệu nhập từ input() LUÔN CÓ KIỂU XÂU (str)
    Chuyển đổi kiểu dữ liệu (Ép kiểu)
      int(): Chuyển xâu thành số nguyên (VD: int(input()))
      float(): Chuyển xâu thành số thực
      str(): Chuyển số thành xâu
    Toán tử số học
      Cộng +, Trừ -, Nhân *, Chia thực /
      Chia lấy phần nguyên //
      Chia lấy phần dư %
      Lũy thừa **
    
```

---

## 2. Tóm tắt nhanh cốt lõi ghi nhớ (Flashcard dạng bảng)

| Khái niệm cốt lõi | Nội dung trọng tâm cần nhớ |
| :--- | :--- |
| **Lệnh print()** | In dữ liệu ra màn hình; có thể dùng sep để đổi dấu ngăn cách, end để không xuống dòng. |
| **Lệnh input()** | Nhận dữ liệu người dùng nhập từ bàn phím; mặc định luôn trả về kiểu chuỗi (str). |
| **Ép kiểu bắt buộc** | Phải dùng int() hoặc float() khi muốn tính toán số học từ input(). |

---

## 3. Liên kết bài học trực tuyến
👉 [Mở bài học tương tác trực tuyến](../../lessons/lop-10/bai-18.html)
