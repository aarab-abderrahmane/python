import os
import subprocess
import customtkinter as ctk
from tkinter import filedialog, messagebox

# إنشاء الواجهة
ctk.set_appearance_mode("Dark")  # الوضع الداكن
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("GitHub Push GUI")
app.geometry("500x300")

# متغير لتخزين مسار المجلد
folder_path = ctk.StringVar()

# دالة لاختيار المجلد
def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)

# دالة لتنفيذ push إلى GitHub
def push_to_github():
    repo_path = folder_path.get().strip()
    commit_message = commit_entry.get().strip()

    if not repo_path:
        messagebox.showerror("خطأ", "يرجى اختيار مجلد المشروع.")
        return
    
    if not commit_message:
        messagebox.showerror("خطأ", "يرجى إدخال رسالة الكوميت.")
        return
    
    try:
        # تنفيذ أوامر Git
        subprocess.run(["git", "-C", repo_path, "add", "."], check=True)
        subprocess.run(["git", "-C", repo_path, "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "-C", repo_path, "push"], check=True)

        messagebox.showinfo("نجاح", "تم إرسال التغييرات إلى GitHub بنجاح!")
    except subprocess.CalledProcessError:
        messagebox.showerror("خطأ", "حدث خطأ أثناء تنفيذ أوامر Git. تأكد من إعداد الريبو بشكل صحيح.")

# واجهة اختيار المجلد
folder_frame = ctk.CTkFrame(app)
folder_frame.pack(pady=10, padx=10, fill="x")

folder_label = ctk.CTkLabel(folder_frame, text="المجلد:")
folder_label.pack(side="left", padx=5)

folder_entry = ctk.CTkEntry(folder_frame, textvariable=folder_path, width=300)
folder_entry.pack(side="left", padx=5, fill="x", expand=True)

folder_button = ctk.CTkButton(folder_frame, text="📂", width=30, command=select_folder)
folder_button.pack(side="right", padx=5)

# إدخال رسالة الكوميت
commit_entry = ctk.CTkEntry(app, placeholder_text="أدخل رسالة الكوميت هنا", width=400)
commit_entry.pack(pady=10)

# زر الإرسال إلى GitHub
push_button = ctk.CTkButton(app, text="Push to GitHub", command=push_to_github)
push_button.pack(pady=10)

app.mainloop()
