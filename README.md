# VietTeach (Quản Lý Nội Dung Dạy Học Tin Học 6 - 12)

> Nền tảng tổ chức học liệu, biên soạn sơ đồ tư duy và xây dựng bài học tương tác trực tuyến môn Tin học từ Khối 6 đến Khối 12 theo Chương trình GDPT 2018.

---

## 🌟 Mục tiêu dự án

1. **Quản lý học liệu tập trung:** Lưu trữ và đối chiếu Sách giáo khoa (nguồn chính), Sách giáo viên (hỗ trợ sư phạm), Sách bài tập cho các khối lớp 6, 7, 8, 9, 10, 11, 12.
2. **Sơ đồ tư duy trực quan (Mindmaps):** Mỗi khối có các bài học, mỗi bài tái hiện lần lượt nội dung cô đọng theo cấu trúc nhánh cây để học sinh dễ nhớ và xem lại nhanh chóng.
3. **Trang web dạy học tương tác (GitHub Pages):** Thiết kế bài học 7 bước chuẩn sư phạm (Mục tiêu, Khởi động, Khám phá, Luyện tập, Vận dụng, Tóm tắt, Đánh giá trắc nghiệm 3 dạng ma trận mới) chạy trực tuyến trên GitHub Pages không cần máy chủ riêng.

---

## 📂 Cấu trúc thư mục dự án

```text
VietTeach/
├── index.html                   # Cổng điều hướng trực tuyến (Landing Page cho GitHub Pages)
├── README.md                    # Tài liệu giới thiệu dự án
├── docs/                        # Tài liệu hướng dẫn & quy chuẩn
│   └── HUONG_DAN_DONG_BOI.md
│
├── lessons/                     # CÁC BÀI HỌC TƯƠNG TÁC (Tự học & trực tuyến)
│   ├── lop-06/ ... lop-12/
│   │   ├── bai-02-thong-tin-trong-giai-quyet-van-de.html
│   │   └── bai-04-mot-so-van-de-phap-li-ve-su-dung-dich-vu-internet.html
│
├── mindmaps/                    # SƠ ĐỒ TƯ DUY TỪNG BÀI (Mermaid / Markdown)
│   ├── lop-06/ ... lop-12/
│   │   ├── bai-02.md
│   │   └── bai-04.md
│
├── materials/                   # HỌC LIỆU GỐC & TÀI LIỆU SƯ PHẠM (PDF/DOCX)
│   ├── lop-06/ ... lop-12/
│   │   ├── sgk/                 # Sách giáo khoa
│   │   ├── sgv/                 # Sách giáo viên
│   │   └── sbt/                 # Sách bài tập
│   └── tham-khao/               # Sách chuyên tin, tài liệu giải thuật
│
└── practice/                    # KHO BÀI TẬP LẬP TRÌNH & THỰC HÀNH
    ├── python-basic/            # Lập trình Python căn bản
    ├── giai-thuat/              # Cấu trúc dữ liệu và giải thuật
    ├── de-thi/                  # Đề thi HSG, Olympic, Tin học trẻ
    ├── ung-dung/                # Ứng dụng nhỏ & minigame
    └── web-co-ban/              # Thiết kế web HTML/CSS căn bản
```

---

## 🚀 Hướng dẫn kích hoạt GitHub Pages

1. Đẩy mã nguồn lên repository:
   ```bash
   git add .
   git commit -m "To chuc lai cau truc VietTeach"
   git push origin main
   ```
2. Trên GitHub, vào **Settings** > **Pages**.
3. Tại **Branch**, chọn `main` và thư mục `/ (root)`, sau đó nhấn **Save**.
4. Website sẽ tự động xuất bản tại: `https://<ten-tai-khoan>.github.io/VietTeach/`.

---

## 📝 Quy chuẩn bài học 7 bước
Xem chi tiết quy chuẩn sư phạm và kỹ thuật tại [docs/HUONG_DAN_DONG_BOI.md](docs/HUONG_DAN_DONG_BOI.md).
