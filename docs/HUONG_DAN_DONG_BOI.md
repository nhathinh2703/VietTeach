# Hướng Dẫn Biên Soạn & Quản Lý Dự Án VietTeach

Tài liệu này hướng dẫn cách tổ chức học liệu, biên soạn sơ đồ tư duy, tạo trang web bài học tương tác và cấu hình xuất bản lên **GitHub Pages**.

---

## 1. Cấu trúc thư mục chuẩn của VietTeach

```text
VietTeach/
├── index.html                   # Trang chủ điều hướng (Cổng Portal xem trực tuyến trên GitHub Pages)
├── README.md                    # Giới thiệu dự án, quy chuẩn kỹ thuật
├── docs/                        # Tài liệu hướng dẫn & quy chuẩn biên soạn
│   └── HUONG_DAN_DONG_BOI.md
│
├── lessons/                     # CÁC BÀI HỌC TƯƠNG TÁC (Tự học & trực tuyến)
│   ├── lop-06/
│   ├── lop-07/
│   ├── lop-08/
│   ├── lop-09/
│   │   ├── bai-02-thong-tin-trong-giai-quyet-van-de.html
│   │   └── bai-04-mot-so-van-de-phap-li-ve-su-dung-dich-vu-internet.html
│   ├── lop-10/
│   ├── lop-11/
│   └── lop-12/
│
├── mindmaps/                    # SƠ ĐỒ TƯ DUY (Mermaid, Markdown, SVG/PNG)
│   ├── lop-06/ ... lop-12/
│   │   ├── bai-02.md
│   │   └── bai-04.md
│
├── materials/                   # HỌC LIỆU GỐC & TÀI LIỆU SƯ PHẠM (PDF/DOCX)
│   ├── lop-06/ ... lop-12/
│   │   ├── sgk/                 # Sách giáo khoa (nguồn chính)
│   │   ├── sgv/                 # Sách giáo viên (hỗ trợ cách tổ chức dạy học)
│   │   └── sbt/                 # Sách bài tập
│   └── tham-khao/               # Tài liệu chuyên tin, thuật toán nâng cao
│
└── practice/                    # KHO BÀI TẬP LẬP TRÌNH & THỰC HÀNH
    ├── python-basic/            # Bài tập Python cơ bản theo chương trình SGK
    ├── giai-thuat/              # Cấu trúc dữ liệu & Thuật toán
    ├── de-thi/                  # Đề thi HSG, Tin học trẻ các cấp
    ├── ung-dung/                # Các dự án nhỏ, minigame
    └── web-co-ban/              # Thực hành HTML/CSS
```

---

## 2. Quy chuẩn 7 bước thiết kế bài học tương tác (Interactive Web)

Mỗi trang bài học (như `bai-02` và `bai-04`) được thiết kế theo quy trình sư phạm chuẩn GDPT 2018 gồm 7 phần:

1. **Mục tiêu bài học (Yêu cầu cần đạt):** Nêu rõ kiến thức, năng lực và phẩm chất theo chuẩn chương trình môn Tin học.
2. **Khởi động:** Đưa ra tình huống thực tế, câu hỏi gợi mở để kích thích học sinh tư duy.
3. **Khám phá kiến thức:** Chia thành các tiểu mục nhỏ kèm ví dụ minh họa, câu hỏi tương tác ngắn, có nút "Đánh dấu đã xem".
4. **Luyện tập:** Bài tập củng cố ngay sau lý thuyết.
5. **Vận dụng:** Tình huống thực tiễn mở rộng giúp học sinh áp dụng kiến thức vào đời sống hoặc học tập.
6. **Tóm tắt cốt lõi:** Bảng tổng hợp hoặc sơ đồ tóm tắt ngắn gọn.
7. **Hệ thống đánh giá ma trận (3 Dạng):**
   - **Dạng 1:** Trắc nghiệm nhiều lựa chọn (chọn 1 đáp án đúng).
   - **Dạng 2:** Trắc nghiệm Đúng/Sai đa ý (mỗi ý chọn Đúng hoặc Sai).
   - **Dạng 3:** Tự luận ngắn có gợi ý đáp án và biểu điểm.

---

## 3. Quy chuẩn tạo Sơ đồ tư duy (Mindmaps)

- Đặt tên file theo cấu trúc: `mindmaps/lop-{xx}/bai-{yy}.md`.
- Sử dụng cú pháp **Mermaid Mindmap** để hiển thị dạng cây trực quan, kết hợp bảng Flashcard tóm tắt nhanh.
- Học sinh hoặc giáo viên có thể mở trực tiếp trên GitHub hoặc render bằng các công cụ như Markmap/VSCode Mermaid Preview.

---

## 4. Hướng dẫn xuất bản lên GitHub Pages

Để học sinh có thể truy cập trực tuyến mọi lúc mọi nơi từ điện thoại và máy tính:

1. Đẩy mã nguồn lên kho chứa GitHub của bạn:
   ```bash
   git add .
   git commit -m "To chuc lai cau truc VietTeach va them cong hoc tap"
   git push origin main
   ```
2. Mở trình duyệt vào trang quản trị repo trên GitHub:
   - Vào **Settings** (Cài đặt) -> Chọn tab **Pages** (bên menu trái).
   - Tại mục **Build and deployment** -> **Source**: Chọn `Deploy from a branch`.
   - Tại mục **Branch**: Chọn nhánh `main` và thư mục `/ (root)`.
   - Bấm **Save**.
3. Sau khoảng 1-2 phút, GitHub sẽ cung cấp đường link truy cập công khai:
   `https://<username>.github.io/VietTeach/`
   - Bất kỳ học sinh nào cũng có thể truy cập để học tập, làm bài kiểm tra và theo dõi tiến độ.
