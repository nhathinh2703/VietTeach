# Sơ Đồ Tư Duy - Tin Học 11: Bài 18

> **Thực hành xác định cấu trúc bảng và các trường khoá**  
> *Chương trình GDPT 2018 - Bộ sách Kết nối tri thức với cuộc sống (Chủ đề 6: Thực hành CSDL)*

---

## 1. Sơ đồ tư duy dạng Mermaid (Trực quan hóa kiến thức)

```mermaid
mindmap
  root((BÀI 18: THỰC HÀNH XÁC ĐỊNH CẤU TRÚC BẢNG VÀ CÁC TRƯỜNG KHOÁ))

    Thiết kế cấu trúc bảng
      Phân tích thực thể
        Ví dụ bài toán Quản lí thư viện: Bảng DOC_GIA, Bảng SACH, Bảng MUON_TRA
      Xác định các trường (Field) & Kiểu dữ liệu
        INT: Số nguyên (mã định danh, số lượng)
        VARCHAR(n): Xâu kí tự độ dài thay đổi (họ tên, tên sách)
        DATE: Ngày tháng năm
      Lựa chọn trường khóa
        Chọn MaDG làm khóa chính cho DOC_GIA
        Chọn MaSach làm khóa chính cho SACH
    
```

---

## 2. Flashcards - Thuật ngữ & Kiến thức cốt lõi

### 🏷️ Kiểu dữ liệu VARCHAR
> **Khái niệm cốt lõi:**  
> Kiểu dữ liệu chuỗi kí tự có độ dài biến thiên giúp tối ưu hóa dung lượng bộ nhớ lưu trữ.

---
### 🏷️ Xác định khóa chính
> **Khái niệm cốt lõi:**  
> Bước then chốt trong thiết kế CSDL nhằm bảo đảm không có 2 bản ghi trùng lặp mã định danh.

---
### 🏷️ Phân tích thực thể
> **Khái niệm cốt lõi:**  
> Quá trình chuyển đổi các đối tượng ngoài đời thực thành các bảng dữ liệu trong máy tính.

---


## 3. Hướng dẫn ôn tập & Tư duy tự học

1. **Quan sát tổng quan**: Đọc từ nhánh gốc ở tâm sơ đồ tư duy Mermaid ra các nhánh cấp 1 và cấp 2.
2. **Đối chiếu thực tế**: Tự liên hệ các khái niệm với thao tác thực hành trên máy tính và tình huống thực tiễn.
3. **Tự kiểm tra**: Che phần định nghĩa trong các thẻ Flashcards và tự diễn đạt lại bằng ngôn từ của mình.

---
*Tài liệu thuộc Hệ sinh thái giải pháp giáo dục VietApps (VietMix, VietTest, VietBook, VietTeach).*
