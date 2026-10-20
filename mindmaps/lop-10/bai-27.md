# Sơ Đồ Tư Duy - Tin Học 10: Bài 27

> **Bài 27: Tham số của hàm**  
> *Chương trình GDPT 2018 - Bộ sách Kết nối tri thức với cuộc sống (Chủ đề 5: Lập trình Python)*

---

## 1. Sơ đồ tư duy dạng Mermaid (Trực quan hóa kiến thức)

```mermaid
mindmap
  root((BÀI 27: THAM SỐ CỦA HÀM))

    Phân biệt Tham số và Đối số
      Tham số (Parameter): Biến được khai báo trong định nghĩa hàm (def)
      Đối số (Argument): Giá trị thực tế được truyền vào khi gọi hàm
    Truyền đối số theo vị trí (Positional arguments)
      Các đối số được gán tương ứng theo đúng thứ tự xuất hiện
    Truyền đối số theo từ khóa (Keyword arguments)
      Chỉ định rõ tên tham số khi gọi hàm (VD: f(b=2, a=1))
    Tham số có giá trị mặc định (Default parameter)
      Cú pháp: def f(x, step=1):
      Nếu người gọi không truyền giá trị cho step, Python tự lấy giá trị mặc định là 1
      Tham số mặc định phải đặt ở sau các tham số không có mặc định
    
```

---

## 2. Tóm tắt nhanh cốt lõi ghi nhớ (Flashcard dạng bảng)

| Khái niệm cốt lõi | Nội dung trọng tâm cần nhớ |
| :--- | :--- |
| **Tham số vs Đối số** | Tham số ở phần định nghĩa hàm, đối số là dữ liệu cụ thể khi gọi chạy hàm. |
| **Tham số mặc định** | Cung cấp sẵn giá trị dự phòng, giúp gọi hàm linh hoạt hơn. |
| **Đối số từ khóa** | Gọi hàm theo tên biến tham số giúp câu lệnh rõ ràng, không phụ thuộc vị trí. |

---

## 3. Liên kết bài học trực tuyến
👉 [Mở bài học tương tác trực tuyến](../../lessons/lop-10/bai-27.html)
