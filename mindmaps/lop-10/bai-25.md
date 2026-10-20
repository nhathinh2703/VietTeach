# Sơ Đồ Tư Duy - Tin Học 10: Bài 25

> **Bài 25: Một số lệnh làm việc với xâu kí tự**  
> *Chương trình GDPT 2018 - Bộ sách Kết nối tri thức với cuộc sống (Chủ đề 5: Lập trình Python)*

---

## 1. Sơ đồ tư duy dạng Mermaid (Trực quan hóa kiến thức)

```mermaid
mindmap
  root((BÀI 25: MỘT SỐ LỆNH LÀM VIỆC VỚI XÂU KÍ TỰ))

    Tách và Nối xâu
      s.split(sep): Tách xâu thành danh sách các từ (mặc định phân cách theo khoảng trắng)
      sep.join(list): Nối các phần tử của danh sách thành một xâu duy nhất
    Chuyển đổi kiểu chữ
      s.lower(): Chuyển toàn bộ thành chữ thường
      s.upper(): Chuyển toàn bộ thành chữ hoa
      s.title(): Viết hoa chữ cái đầu mỗi từ
    Tìm kiếm và Thay thế
      s.find(sub): Trả về vị trí xuất hiện đầu tiên của xâu con sub (trả về -1 nếu không có)
      s.count(sub): Đếm số lần xâu con xuất hiện
      s.replace(old, new): Thay thế xâu cũ bằng xâu mới
    Xóa khoảng trắng thừa
      s.strip(): Cắt bỏ khoảng trắng ở đầu và cuối xâu
    
```

---

## 2. Tóm tắt nhanh cốt lõi ghi nhớ (Flashcard dạng bảng)

| Khái niệm cốt lõi | Nội dung trọng tâm cần nhớ |
| :--- | :--- |
| **split() & join()** | split chia xâu thành mảng các từ; join gộp mảng từ thành xâu dài. |
| **lower() & upper()** | Chuẩn hóa định dạng chữ hoa/chữ thường khi so sánh xâu. |
| **find() & replace()** | find dò tìm vị trí kí tự; replace thay thế từ khóa linh hoạt. |

---

## 3. Liên kết bài học trực tuyến
👉 [Mở bài học tương tác trực tuyến](../../lessons/lop-10/bai-25.html)
