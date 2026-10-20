# Sơ Đồ Tư Duy - Tin Học 10: Bài 28

> **Bài 28: Phạm vi của biến**  
> *Chương trình GDPT 2018 - Bộ sách Kết nối tri thức với cuộc sống (Chủ đề 5: Lập trình Python)*

---

## 1. Sơ đồ tư duy dạng Mermaid (Trực quan hóa kiến thức)

```mermaid
mindmap
  root((BÀI 28: PHẠM VI CỦA BIẾN))

    Biến cục bộ (Local variable)
      Được khai báo bên trong một hàm
      Chỉ có hiệu lực và sử dụng được trong nội bộ hàm đó
      Bị xóa khỏi bộ nhớ khi hàm kết thúc thực thi
    Biến toàn cục (Global variable)
      Được khai báo bên ngoài tất cả các hàm
      Có thể được đọc từ bất kì đâu trong chương trình
    Từ khóa global
      Mặc định hàm chỉ được đọc biến toàn cục, không được gán đổi giá trị
      Muốn sửa đổi giá trị biến toàn cục bên trong hàm, phải khai báo: global <tên_biến>
    Nguyên tắc lập trình tốt
      Hạn chế lạm dụng biến toàn cục để tránh các lỗi logic khó kiểm soát
    
```

---

## 2. Tóm tắt nhanh cốt lõi ghi nhớ (Flashcard dạng bảng)

| Khái niệm cốt lõi | Nội dung trọng tâm cần nhớ |
| :--- | :--- |
| **Biến cục bộ** | Khai báo trong hàm, chỉ sống và dùng được bên trong hàm đó. |
| **Biến toàn cục** | Khai báo ngoài hàm, có phạm vi nhìn thấy trên toàn bộ chương trình. |
| **Từ khóa global** | Bắt buộc dùng khi muốn gán lại giá trị cho biến toàn cục từ trong hàm. |

---

## 3. Liên kết bài học trực tuyến
👉 [Mở bài học tương tác trực tuyến](../../lessons/lop-10/bai-28.html)
