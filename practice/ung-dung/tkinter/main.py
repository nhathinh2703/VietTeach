import tkinter as tk
from tkinter import ttk, messagebox

def reset_info():
    entry_name.delete(0, tk.END)
    entry_grade.delete(0, tk.END)
    gender_var.set("Nam")
    hobby_read.set(False)
    hobby_music.set(False)
    hobby_sport.set(False)
    combo_day.set("")
    combo_month.set("")
    combo_year.set("")
    combo_country.set("")
    text_bio.delete("1.0", tk.END)


def show_info():
    name = entry_name.get()
    grade = entry_grade.get()
    gender = gender_var.get()
    birthday = f'{combo_day.get()}/{combo_month.get()}/{combo_year.get()}'
    hobbies = []
    if hobby_read.get(): hobbies.append("Đọc sách")
    if hobby_music.get(): hobbies.append("Nghe nhạc")
    if hobby_sport.get(): hobbies.append("Thể thao")
    country = combo_country.get()
    bio = text_bio.get("1.0", tk.END).strip()

    msg = f"Họ tên: {name}\nNgày sinh: {birthday}\nLớp: {grade}\nGiới tính: {gender}\nSở thích: {', '.join(hobbies)}\nQuốc gia: {country}\nGiới thiệu: {bio}"
    messagebox.showinfo("Thông tin học sinh", msg)

root = tk.Tk()
root.title("Form thông tin học sinh")
root.geometry("500x500")

# Họ tên
tk.Label(root, text="Họ tên:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
entry_name = tk.Entry(root, width=40)
entry_name.pack(padx=10)

# Ngày sinh
tk.Label(root, text="Ngày sinh:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
frame_dob = tk.Frame(root)
frame_dob.pack(anchor="w", padx=20)

combo_day = ttk.Combobox(frame_dob, values=[str(i) for i in range(1,32)], width=5)
combo_day.set("1")
combo_day.pack(side="left", padx=5)

combo_month = ttk.Combobox(frame_dob, values=[str(i) for i in range(1,13)], width=5)
combo_month.set("1")
combo_month.pack(side="left", padx=5)

combo_year = ttk.Combobox(frame_dob, values=[str(i) for i in range(1900, 2099)], width=7)
combo_year.set("2005")
combo_year.pack(side="left", padx=5)

# Lớp
tk.Label(root, text="Lớp:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
entry_grade = tk.Entry(root, width=20)
entry_grade.pack(padx=10)

# Giới tính
tk.Label(root, text="Giới tính:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
gender_var = tk.StringVar(value="Nam")
frame_gender = tk.Frame(root)
frame_gender.pack(anchor="w", padx=20)

tk.Radiobutton(frame_gender, text="Nam", variable=gender_var, value="Nam").pack(side="left", padx=10)

tk.Radiobutton(frame_gender, text="Nữ", variable=gender_var, value="Nữ").pack(side="left", padx=10)

# Sở thích
tk.Label(root, text="Sở thích:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
hobby_read = tk.BooleanVar()
hobby_music = tk.BooleanVar()
hobby_sport = tk.BooleanVar()
frame_hobby = tk.Frame(root)
frame_hobby.pack(anchor="w", padx=20)
tk.Checkbutton(frame_hobby, text="Đọc sách", variable=hobby_read).pack(side="left", padx=10)
tk.Checkbutton(frame_hobby, text="Nghe nhạc", variable=hobby_music).pack(side="left", padx=10)
tk.Checkbutton(frame_hobby, text="Thể thao", variable=hobby_sport).pack(side="left", padx=10)

# Quốc gia
tk.Label(root, text="Quốc gia:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
combo_country = ttk.Combobox(root, values=["Việt Nam", "Mỹ", "Nhật Bản", "Hàn Quốc", "Brazil"])
combo_country.pack(padx=10)

# Giới thiệu bản thân
tk.Label(root, text="Giới thiệu:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
text_bio = tk.Text(root, width=50, height=5)
text_bio.pack(padx=10, pady=5)

# Nút xác nhận
tk.Button(root, text="Xác nhận", command=show_info).pack(pady=20)

tk.Button(root, text="Nhập lại", command=reset_info).pack(pady=20)

root.mainloop()
