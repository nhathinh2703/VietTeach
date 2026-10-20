# Sơ Đồ Tư Duy - Tin Học 10: Bài 23

> **Bài 23: Một số lệnh làm việc với dữ liệu danh sách**  
> *Chương trình GDPT 2018 - Bộ sách Kết nối tri thức với cuộc sống (Chủ đề 5: Lập trình Python)*

---

## 1. Sơ đồ tư duy dạng Mermaid (Trực quan hóa kiến thức)

```mermaid
mindmap
  root((BÀI 23: MỘT SỐ LỆNH LÀM VIỆC VỚI DỮ LIỆU DANH SÁCH))

    Các phương thức chỉnh sửa danh sách
      Thêm phần tử:
        a.append(x): Thêm x vào cuối danh sách
        a.insert(i, x): Chèn x vào vị trí chỉ số i
      Xóa phần tử:
        a.remove(x): Xóa phần tử đầu tiên có giá trị x
        del a[i]: Xóa phần tử tại vị trí chỉ số i
        a.pop(i): Xóa và trả về phần tử tại vị trí i (mặc định xóa cuối)
        a.clear(): Xóa sạch mọi phần tử
    Các thao tác tìm kiếm & Sắp xếp
      Toán tử in / not in: Kiểm tra phần tử có nằm trong danh sách không
      a.count(x): Đếm số lần x xuất hiện
      a.index(x): Trả về vị trí đầu tiên của x
      a.sort(): Sắp xếp danh sách tăng dần tại chỗ
      a.reverse(): Đảo ngược thứ tự danh sách
    
```

---

## 2. Tóm tắt nhanh cốt lõi ghi nhớ (Flashcard dạng bảng)

| Khái niệm cốt lõi | Nội dung trọng tâm cần nhớ |
| :--- | :--- |
| **append() & insert()** | append thêm vào cuối mảng; insert chèn vào vị trí chỉ định. |
| **remove() & del** | remove xóa theo giá trị tìm thấy; del xóa theo chỉ số vị trí. |
| **sort() & reverse()** | sort sắp xếp danh sách tăng dần; reverse đảo ngược mảng. |

---

## 3. Liên kết bài học trực tuyến
👉 [Mở bài học tương tác trực tuyến](../../lessons/lop-10/bai-23.html)
