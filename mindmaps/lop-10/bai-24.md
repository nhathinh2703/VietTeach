# Sơ Đồ Tư Duy - Tin Học 10: Bài 24

> **Bài 24: Xâu kí tự**  
> *Chương trình GDPT 2018 - Bộ sách Kết nối tri thức với cuộc sống (Chủ đề 5: Lập trình Python)*

---

## 1. Sơ đồ tư duy dạng Mermaid (Trực quan hóa kiến thức)

```mermaid
mindmap
  root((BÀI 24: XÂU KÍ TỰ))

    Đặc điểm xâu kí tự (String)
      Dãy các kí tự đặt trong cặp dấu nháy đơn '...' hoặc nháy kép "..."
      Tính chất bất biến (Immutable): Không thể gán trực tiếp thay đổi từng kí tự s[0] = 'a'
    Chỉ số và Cắt xâu (Slicing)
      Đánh số chỉ số từ 0 đến len(s)-1 (và chỉ số âm từ -1)
      Cú pháp cắt xâu: s[start:stop:step]
        s[1:4]: Lấy từ chỉ số 1 đến 3
        s[::-1]: Kĩ thuật đảo ngược toàn bộ xâu kí tự
    Duyệt xâu kí tự
      for ch in s: Duyệt từng kí tự
    Toán tử xâu
      Ghép xâu (+), lặp xâu (*)
      Kiểm tra tồn tại: in, not in
    
```

---

## 2. Tóm tắt nhanh cốt lõi ghi nhớ (Flashcard dạng bảng)

| Khái niệm cốt lõi | Nội dung trọng tâm cần nhớ |
| :--- | :--- |
| **Tính bất biến** | Xâu không cho phép gán đè trực tiếp từng kí tự như danh sách. |
| **Cắt xâu s[start:stop]** | Lấy chuỗi con từ vị trí start đến sát stop-1. |
| **Đảo xâu s[::-1]** | Mẹo kinh điển trong Python để lật ngược một xâu kí tự. |

---

## 3. Liên kết bài học trực tuyến
👉 [Mở bài học tương tác trực tuyến](../../lessons/lop-10/bai-24.html)
