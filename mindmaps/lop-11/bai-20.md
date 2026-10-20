# Sơ Đồ Tư Duy - Tin Học 11: Bài 20

> **Thực hành tạo lập các bảng có khoá ngoài**  
> *Chương trình GDPT 2018 - Bộ sách Kết nối tri thức với cuộc sống (Chủ đề 6: Thực hành CSDL)*

---

## 1. Sơ đồ tư duy dạng Mermaid (Trực quan hóa kiến thức)

```mermaid
mindmap
  root((BÀI 20: THỰC HÀNH TẠO LẬP CÁC BẢNG CÓ KHOÁ NGOÀI))

    Thiết lập Khóa ngoài
      Khái niệm liên kết bảng
        Bảng tham chiếu (Bảng con) trỏ về Bảng được tham chiếu (Bảng cha)
      Tạo khóa ngoài trong HeidiSQL
        Tab Foreign Keys: Chọn trường làm khóa ngoài và chọn bảng tham chiếu
      Cú pháp SQL
        FOREIGN KEY (MaLop) REFERENCES Lop(MaLop)
      Nguyên tắc toàn vẹn tham chiếu
        Không thể thêm bản ghi vào bảng con nếu mã tham chiếu chưa có ở bảng cha
    
```

---

## 2. Flashcards - Thuật ngữ & Kiến thức cốt lõi

### 🏷️ Khóa ngoài (Foreign Key)
> **Khái niệm cốt lõi:**  
> Cầu nối liên kết dữ liệu giữa hai bảng, bảo đảm tính toàn vẹn tham chiếu hệ thống.

---
### 🏷️ Bảng cha & Bảng con
> **Khái niệm cốt lõi:**  
> Bảng cha chứa khóa chính, bảng con chứa khóa ngoài trỏ đến khóa chính của bảng cha.

---
### 🏷️ Toàn vẹn tham chiếu
> **Khái niệm cốt lõi:**  
> Nguyên tắc ngăn chặn dữ liệu "mồ côi" không xác định được xuất xứ nguồn gốc.

---


## 3. Hướng dẫn ôn tập & Tư duy tự học

1. **Quan sát tổng quan**: Đọc từ nhánh gốc ở tâm sơ đồ tư duy Mermaid ra các nhánh cấp 1 và cấp 2.
2. **Đối chiếu thực tế**: Tự liên hệ các khái niệm với thao tác thực hành trên máy tính và tình huống thực tiễn.
3. **Tự kiểm tra**: Che phần định nghĩa trong các thẻ Flashcards và tự diễn đạt lại bằng ngôn từ của mình.

---
*Tài liệu thuộc Hệ sinh thái giải pháp giáo dục VietApps (VietMix, VietTest, VietBook, VietTeach).*
