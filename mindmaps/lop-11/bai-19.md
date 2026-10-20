# Sơ Đồ Tư Duy - Tin Học 11: Bài 19

> **Thực hành tạo lập cơ sở dữ liệu và các bảng**  
> *Chương trình GDPT 2018 - Bộ sách Kết nối tri thức với cuộc sống (Chủ đề 6: Thực hành CSDL)*

---

## 1. Sơ đồ tư duy dạng Mermaid (Trực quan hóa kiến thức)

```mermaid
mindmap
  root((BÀI 19: THỰC HÀNH TẠO LẬP CƠ SỞ DỮ LIỆU VÀ CÁC BẢNG))

    Tạo bảng trong HeidiSQL
      Thao tác bằng giao diện đồ họa (GUI)
        Bấm chuột phải chọn Create new -> Table
        Thêm cột: Tên cột, kiểu dữ liệu, chiều dài, thuộc tính Not Null
      Thao tác bằng câu lệnh SQL
        CREATE TABLE HocSinh (MaHS INT PRIMARY KEY, HoTen VARCHAR(50), NgaySinh DATE);
      Chỉnh sửa cấu trúc bảng
        ALTER TABLE để thêm hoặc sửa đổi cột
    
```

---

## 2. Flashcards - Thuật ngữ & Kiến thức cốt lõi

### 🏷️ CREATE TABLE
> **Khái niệm cốt lõi:**  
> Câu lệnh SQL dùng để tạo mới một bảng dữ liệu kèm theo định nghĩa chi tiết các cột.

---
### 🏷️ NOT NULL
> **Khái niệm cốt lõi:**  
> Thuộc tính ràng buộc bắt buộc người dùng phải nhập giá trị cho trường, không được để trống.

---
### 🏷️ ALTER TABLE
> **Khái niệm cốt lõi:**  
> Câu lệnh SQL cho phép chỉnh sửa, thêm mới hoặc xóa bớt cột trong một bảng đã tồn tại.

---


## 3. Hướng dẫn ôn tập & Tư duy tự học

1. **Quan sát tổng quan**: Đọc từ nhánh gốc ở tâm sơ đồ tư duy Mermaid ra các nhánh cấp 1 và cấp 2.
2. **Đối chiếu thực tế**: Tự liên hệ các khái niệm với thao tác thực hành trên máy tính và tình huống thực tiễn.
3. **Tự kiểm tra**: Che phần định nghĩa trong các thẻ Flashcards và tự diễn đạt lại bằng ngôn từ của mình.

---
*Tài liệu thuộc Hệ sinh thái giải pháp giáo dục VietApps (VietMix, VietTest, VietBook, VietTeach).*
