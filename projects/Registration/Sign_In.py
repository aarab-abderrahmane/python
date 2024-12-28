from customtkinter import *
import customtkinter as ck
from PIL import Image,ImageTk
import sqlite3
from tkinter import messagebox

from SIgn_up import SignUpPage
from forget_password import reset_password

class Sign: 
    def __init__(self, app):
        self.app = app
        self.app.geometry("800x450")
        self.app.title('Sign In')
        self.app.resizable(False,False)
        self.app.iconbitmap("C:\\Users\\group2\\Desktop\\python\\projects\\Registration\\icon_app.ico")

        self.creat_data()


        self.app.grid_columnconfigure(0, weight=1, uniform="equal")
        self.app.grid_columnconfigure(1, weight=1, uniform="equal")
        self.app.grid_rowconfigure(0, weight=1)

        self.frame_1 = CTkFrame(app, corner_radius=0, fg_color="#e9edc9")
        self.frame_1.grid(row=0, column=0, sticky="nsew")

        self.image = Image.open("C:\\Users\\group2\\Desktop\\python\\projects\\Registration\\photo-multicultural-community-concept-collage.jpg")
        # C:\\Users\\group2\\Desktop\\python\\images\\photo-multicultural-community-concept-collage.jpg

        self.image = self.image.resize((400, 500)) 
        self.photo = CTkImage(self.image, size=(400, 500))
        
        self.image_label = CTkLabel(self.frame_1, image=self.photo, text="")
        self.image_label.grid(row=0, column=0, sticky="nsew") 

        self.frame_1.grid_rowconfigure(0, weight=1)
        self.frame_1.grid_columnconfigure(0, weight=1)

# _____________________________________________________________________________________________________________________________________


        self.frame_2 = CTkFrame(app, corner_radius=0, fg_color="white")# #ffedd9
        self.frame_2.grid(row=0, column=1, sticky="nsew")

        self.image_1 = Image.open("C:\\Users\\group2\\Desktop\\python\\projects\\Registration\\icon_.ico")
        self.image_1 = self.image_1.resize((40, 40))  
        self.icon = CTkImage(self.image_1, size=(40, 40))

        self.icon_label = CTkLabel(self.frame_2, image=self.icon, text="")
        self.icon_label.grid(row=0, column=0, sticky="n", pady=40,padx=40) 
        

        self.label_1=CTkLabel(self.frame_2,text="UI Unicon",font=('Arial Black',25,'bold'),text_color="#1c1c1c")
        self.label_1.place(x=90,y=45)

        self.label_2=CTkLabel(self.frame_2,text="Nice to see you again",font=('Helvetica',18,'bold'),text_color="black")
        self.label_2.place(x=40,y=120)


        self.label_3=CTkLabel(self.frame_2,text="Login",font=('Arial',14),text_color="black")
        self.label_3.place(x=50,y=160)

        self.entry_1=CTkEntry(self.frame_2,placeholder_text="   Email or phone number",width=320,text_color="black",font=("Arial",15),fg_color="#f5ebe0",height=50,border_color="#f5ebe0")
        self.entry_1.place(x=40,y=190)

        self.label_4=CTkLabel(self.frame_2,text="Password",font=('Arial',14),text_color="black")
        self.label_4.place(x=50,y=250)

        self.entry_2=CTkEntry(self.frame_2,placeholder_text="   Enter password",width=320,text_color="black",font=("Arial",15),fg_color="#f5ebe0",height=50,border_color="#f5ebe0")
        self.entry_2.place(x=40,y=280)

        self.check=CTkSwitch(self.frame_2,text="show passwrod",text_color="black",fg_color="#f2f2f2",command=lambda : self.show_password(self.check,self.entry_2))
        self.check.place(x=40,y=340)

        self.label_5=CTkLabel(self.frame_2,text="Forget password ?",cursor="hand2",text_color="#0f83ff")
        self.label_5.place(x=257,y=340)
        self.label_5.bind("<Button-1>",  lambda event: self.open_reset_password())

        self.button_sign_in=CTkButton(self.frame_2,text="Sign in",text_color="white",fg_color="#007bff",width=210,height=40,corner_radius=8,font=('Helvetica',15,'bold'),command=self.sign_in)
        self.button_sign_in.place(x=40,y=385)

        self.button_sign_up=CTkButton(self.frame_2,text="Sign up",text_color="white",fg_color="#333333",width=100,height=40,corner_radius=8,font=('Helvetica',15,'bold'),command=self.open_signup)
        self.button_sign_up.place(x=260,y=385)

        
# ________________algorithme________________________________________________

    def creat_data(self):
        # _____data_______
        self.connect=sqlite3.connect('useruser.db')
        self.cursor=self.connect.cursor()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_ur (
            email TEXT PRIMARY KEY,
            password TEXT,
            name TEXT
        )
        ''')
        self.connect.commit()

    
    def sign_in(self):
            email=self.entry_1.get()
            password=self.entry_2.get()

            user=self.cursor.execute('SELECT * FROM user_ur WHERE email = ?',(email,)).fetchone()

            
            if user : 

                if user[1] == password:
                    self.entry_1.delete(0,"end")
                    self.entry_2.delete(0,'end')
                    messagebox.showinfo("Success","You have successfully sign in!")
                
                else: 
                    messagebox.showwarning('Invalid Credentials', 'The password you entered is incorrect. Please try again.')

            else : 
                 messagebox.showwarning('Invalid Credentials', 'The email you entered does not exist. Please check your email.')



    def show_password(self,name_check,entry_name):
        if name_check.get():
            entry_name.configure(show="*")
        else:
            entry_name.configure(show="")

    def open_signup(self):
        SignUpPage(self.app, self.frame_2,self.frame_1)
    
    def open_reset_password(self):
        reset_password(self.app,self.frame_1,self.frame_2)


app = CTk()
window = Sign(app)
app.mainloop()
