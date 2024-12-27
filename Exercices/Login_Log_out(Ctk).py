from customtkinter import * 
import customtkinter as ck
from PIL import Image 

class Sign: 
    def __init__(self, app):
        self.app = app
        self.app.geometry("700x400")
        self.app.title('Sign In')

        # إعداد تخطيط الشبكة
        # self.app.grid_columnconfigure(0, weight=1, uniform="equal")
        # self.app.grid_columnconfigure(1, weight=2, uniform="equal")
        self.app.grid_columnconfigure(0,weight=1)
        self.app.grid_columnconfigure(1,weight=100,uniform="equal")
        self.app.grid_rowconfigure(0, weight=1)

        # الإطار الأيسر (frame_1)
        self.frame_1 = CTkFrame(app, corner_radius=0, fg_color="#e9edc9")
        self.frame_1.grid(row=0, column=0, sticky="news")

        # تحميل الصورة وضبط الحجم لتناسب الإطار
        self.image = Image.open("/home/abdulrahman/Desktop/python/images/login.png")
 
        # تعيين الحجم الديناميكي للإطار
        self.image = self.image.resize((400, 400))  # يمكنك ضبط الأبعاد هنا لتتوافق مع الإطار
        self.photo = CTkImage(self.image, size=(400, 400))  # تأكد من ضبط الحجم هنا أيضًا
        
        # إضافة الصورة إلى الإطار الأيسر
        self.image_label = CTkLabel(self.frame_1, image=self.photo, text="")
        self.image_label.place(x=-1,y=10)  # تمدد الصورة لتناسب الإطار

        # الإطار الأيمن (frame_2)
        self.frame_2 = CTkFrame(app, corner_radius=0, fg_color="#ccd5ae")
        self.frame_2.grid(row=0, column=1, sticky="news")

app = CTk()
window = Sign(app)
app.mainloop()
