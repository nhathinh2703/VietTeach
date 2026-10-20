# Sơ Đồ Tư Duy - Tin Học 10: Bài 29

> **Bài 29: Nhận biết lỗi chương trình**  
> *Chương trình GDPT 2018 - Bộ sách Kết nối tri thức với cuộc sống (Chủ đề 5: Lập trình Python)*

---

## 1. Sơ đồ tư duy dạng Mermaid (Trực quan hóa kiến thức)

```mermaid
mindmap
  root((BÀI 29: NHẬN BIẾT LỖI CHƯƠNG TRÌNH))

    Lỗi cú pháp (Syntax Error)
      Do viết sai quy tắc ngữ pháp của Python
      Xảy ra trước khi chương trình chạy
      Ví dụ: Quên dấu hai chấm :, thiếu dấu ngoặc, thụt lề sai (IndentationError)
    Lỗi ngoại lệ khi chạy (Runtime Error / Exception)
      Cú pháp đúng nhưng phát sinh lỗi trong quá trình thực thi
      Ví dụ:
        ZeroDivisionError: Chia cho số 0
        ValueError: Ép kiểu dữ liệu không hợp lệ (int("abc"))
        IndexError: Truy cập chỉ số vượt quá độ dài mảng
        NameError: Dùng biến chưa được khai báo
    Lỗi ngữ nghĩa / Lỗi logic (Semantic / Logic Error)
      Chương trình vẫn chạy hoàn chỉnh không báo lỗi nhưng cho kết quả SAI
      Là loại lỗi khó phát hiện nhất
    
```

---

## 2. Tóm tắt nhanh cốt lõi ghi nhớ (Flashcard dạng bảng)

| Khái niệm cốt lõi | Nội dung trọng tâm cần nhớ |
| :--- | :--- |
| **Lỗi cú pháp** | Sai quy tắc viết code (quên dấu :, thụt dòng sai), Python chặn ngay từ đầu. |
| **Lỗi Runtime** | Lỗi xảy ra lúc chạy: chia cho 0, truy cập mảng quá giới hạn, ép kiểu sai. |
| **Lỗi Logic** | Chương trình chạy trơn tru nhưng kết quả tính toán bị sai do giải thuật nhầm lẫn. |

---

## 3. Liên kết bài học trực tuyến
👉 [Mở bài học tương tác trực tuyến](../../lessons/lop-10/bai-29.html)
