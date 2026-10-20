# Sơ Đồ Tư Duy - Tin Học 10: Bài 22

> **Bài 22: Kiểu dữ liệu danh sách**  
> *Chương trình GDPT 2018 - Bộ sách Kết nối tri thức với cuộc sống (Chủ đề 5: Lập trình Python)*

---

## 1. Sơ đồ tư duy dạng Mermaid (Trực quan hóa kiến thức)

```mermaid
mindmap
  root((BÀI 22: KIỂU DỮ LIỆU DANH SÁCH))

    Khái niệm List (Danh sách)
      Tập hợp các phần tử có thứ tự, đặt trong cặp ngoặc vuông [ ]
      Các phần tử phân cách bằng dấu phẩy, có thể có kiểu dữ liệu khác nhau
      Ví dụ: a = [10, 20, 30, "Tin học", True]
    Chỉ số (Index) của danh sách
      Chỉ số dương: Đánh số từ trái sang phải, bắt đầu từ 0 đến len-1
      Chỉ số âm: Đánh số từ phải sang trái, phần tử cuối cùng là -1
      Truy cập phần tử: a[0], a[-1]
    Các thao tác cơ bản
      Hàm len(a): Trả về số lượng phần tử
      Duyệt danh sách bằng for:
        for x in a: (duyệt theo giá trị)
        for i in range(len(a)): (duyệt theo chỉ số)
      Toán tử ghép nối + và nhân bản *
    
```

---

## 2. Tóm tắt nhanh cốt lõi ghi nhớ (Flashcard dạng bảng)

| Khái niệm cốt lõi | Nội dung trọng tâm cần nhớ |
| :--- | :--- |
| **Cấu trúc List** | Khai báo bằng ngoặc vuông []. Cho phép thay đổi giá trị và chứa nhiều kiểu dữ liệu. |
| **Chỉ số bắt đầu từ 0** | Phần tử đầu tiên là a[0], phần tử cuối cùng là a[-1] hoặc a[len-1]. |
| **Duyệt danh sách** | Dùng vòng lặp for duyệt trực tiếp từng phần tử hoặc thông qua hàm range(len()). |

---

## 3. Liên kết bài học trực tuyến
👉 [Mở bài học tương tác trực tuyến](../../lessons/lop-10/bai-22.html)
