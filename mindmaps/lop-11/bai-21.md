# Sơ Đồ Tư Duy - Tin Học 11: Bài 21

> **Thực hành cập nhật và truy xuất dữ liệu các bảng**  
> *Chương trình GDPT 2018 - Bộ sách Kết nối tri thức với cuộc sống (Chủ đề 6: Thực hành CSDL)*

---

## 1. Sơ đồ tư duy dạng Mermaid (Trực quan hóa kiến thức)

```mermaid
mindmap
  root((BÀI 21: THỰC HÀNH CẬP NHẬT VÀ TRUY XUẤT DỮ LIỆU CÁC BẢNG))

    Cập nhật & Truy vấn dữ liệu
      Nhập dữ liệu
        Tab Data trong HeidiSQL hoặc lệnh INSERT INTO
        INSERT INTO Lop VALUES (1, '11A1', 40);
      Truy vấn lọc dữ liệu
        SELECT HoTen, NgaySinh FROM HocSinh WHERE GioiTinh = 'Nữ';
      Chỉnh sửa dữ liệu
        UPDATE HocSinh SET DiaChi = 'Hà Nội' WHERE MaHS = 101;
      Xóa dữ liệu
        DELETE FROM HocSinh WHERE MaHS = 999;
    
```

---

## 2. Flashcards - Thuật ngữ & Kiến thức cốt lõi

### 🏷️ INSERT INTO
> **Khái niệm cốt lõi:**  
> Câu lệnh SQL dùng để chèn thêm một hoặc nhiều bản ghi mới vào trong bảng dữ liệu.

---
### 🏷️ Mệnh đề WHERE
> **Khái niệm cốt lõi:**  
> Bộ lọc điều kiện giúp câu lệnh SQL chỉ tác động lên đúng các bản ghi thỏa mãn tiêu chí.

---
### 🏷️ Truy vấn dữ liệu
> **Khái niệm cốt lõi:**  
> Thao tác trích xuất thông tin theo mong muốn của người dùng từ kho dữ liệu có sẵn.

---


## 3. Hướng dẫn ôn tập & Tư duy tự học

1. **Quan sát tổng quan**: Đọc từ nhánh gốc ở tâm sơ đồ tư duy Mermaid ra các nhánh cấp 1 và cấp 2.
2. **Đối chiếu thực tế**: Tự liên hệ các khái niệm với thao tác thực hành trên máy tính và tình huống thực tiễn.
3. **Tự kiểm tra**: Che phần định nghĩa trong các thẻ Flashcards và tự diễn đạt lại bằng ngôn từ của mình.

---
*Tài liệu thuộc Hệ sinh thái giải pháp giáo dục VietApps (VietMix, VietTest, VietBook, VietTeach).*
