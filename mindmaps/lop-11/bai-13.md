# Sơ Đồ Tư Duy - Tin Học 11: Bài 13

> **Cơ sở dữ liệu quan hệ**  
> *Chương trình GDPT 2018 - Bộ sách Kết nối tri thức với cuộc sống (Chủ đề 4: Giới thiệu các hệ cơ sở dữ liệu)*

---

## 1. Sơ đồ tư duy dạng Mermaid (Trực quan hóa kiến thức)

```mermaid
mindmap
  root((BÀI 13: CƠ SỞ DỮ LIỆU QUAN HỆ))

    CSDL Quan hệ (RDBMS)
      Mô hình quan hệ
        Bảng (Table / Relation): Cấu trúc 2 chiều gồm các hàng và cột
        Bản ghi (Record / Row / Tuple): Thể hiện một đối tượng cụ thể
        Trường (Field / Column / Attribute): Thể hiện một thuộc tính
      Khoá của bảng
        Khoá chính (Primary Key): Nhận diện duy nhất mỗi bản ghi, không được rỗng
        Khoá ngoài (Foreign Key): Tham chiếu đến khoá chính của bảng khác
      Mối quan hệ giữa các bảng
        Quan hệ 1 - 1: Một chồng - một vợ
        Quan hệ 1 - n: Một lớp - nhiều học sinh
        Quan hệ n - n: Nhiều học sinh - nhiều môn học
    
```

---

## 2. Flashcards - Thuật ngữ & Kiến thức cốt lõi

### 🏷️ Khóa chính (Primary Key)
> **Khái niệm cốt lõi:**  
> Một hoặc tập hợp các trường dùng để định danh duy nhất mỗi bản ghi trong bảng.

---
### 🏷️ Khóa ngoài (Foreign Key)
> **Khái niệm cốt lõi:**  
> Trường trong bảng này dùng để liên kết và tham chiếu đến khóa chính của bảng khác.

---
### 🏷️ Ràng buộc toàn vẹn thực thể
> **Khái niệm cốt lõi:**  
> Quy tắc bắt buộc trường khóa chính không được phép mang giá trị rỗng (NOT NULL).

---


## 3. Hướng dẫn ôn tập & Tư duy tự học

1. **Quan sát tổng quan**: Đọc từ nhánh gốc ở tâm sơ đồ tư duy Mermaid ra các nhánh cấp 1 và cấp 2.
2. **Đối chiếu thực tế**: Tự liên hệ các khái niệm với thao tác thực hành trên máy tính và tình huống thực tiễn.
3. **Tự kiểm tra**: Che phần định nghĩa trong các thẻ Flashcards và tự diễn đạt lại bằng ngôn từ của mình.

---
*Tài liệu thuộc Hệ sinh thái giải pháp giáo dục VietApps (VietMix, VietTest, VietBook, VietTeach).*
