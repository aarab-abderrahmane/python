from customtkinter import *
from PIL import Image
from tkinter import messagebox
import sqlite3



class reset_password:

    def __init__ (self,app,frame_1,frame_2):
        self.app=app
        self.frame_1=frame_1
        self.frame_2=frame_2

        self.frame_1.grid_forget()
        self.frame_2.grid_forget()

        self.connect_data()

        self.frame_3=CTkFrame(self.app,corner_radius=0,fg_color="#fefae0")
        self.frame_3.grid(row=0,column=0,sticky="news")


        self.frame_4=CTkFrame(self.app,corner_radius=0,fg_color="#fefae0")
        self.frame_4.grid(row=0,column=1,sticky="news")


        self.image=Image.open("computer-security-with-login-password-padlock.png")
        self.image=self.image.resize((410,330)) #ext
        self.image=CTkImage(self.image,size=(410,330)) #inter

        self.image_label=CTkLabel(self.frame_3,text="",image=self.image)
        self.image_label.grid(row=0,column=0,pady=50)

        
        self.frame_5=CTkFrame(self.frame_4,corner_radius=10,fg_color="#e9edc9",border_color="black",border_width=2,width=350,height=350)
        self.frame_5.pack(pady=40)

        self.return_icon=Image.open("back-arrow.png")
        self.return_icon=CTkImage(self.return_icon,size=(30,30))

        self.button_return=CTkButton(self.frame_3,text="",image=self.return_icon,fg_color="#f1fbbc",hover_color="#97ccfb",width=5,height=10,corner_radius=40,text_color="white",command=self.back_to_login,font=('Arial Black',18,'bold'))
        self.button_return.place(x=10,y=10)

        

        self.label_1=CTkLabel(self.frame_5,text="Reset password",font=('Arial Black',20,'bold'),text_color="black")
        self.label_1.place(x=100,y=30)

        self.entry_email=CTkEntry(self.frame_5,width=300,height=50,fg_color="#ccd5ae",border_color="#ccd5ae",text_color="black",placeholder_text="email")
        self.entry_name=CTkEntry(self.frame_5,width=300,height=50,fg_color="#ccd5ae",border_color="#ccd5ae",text_color="black",placeholder_text="name")
        self.entry_new_password=CTkEntry(self.frame_5,width=300,height=50,fg_color="#ccd5ae",border_color="black",text_color="black",placeholder_text="new password")
        self.entry_new_password_confirm=CTkEntry(self.frame_5,width=300,height=50,fg_color="#ccd5ae",border_color="black",text_color="black",placeholder_text="confirm password")


        self.entry_email.bind('<KeyPress>',lambda event : self.on_focus_in(event,self.entry_email))
        self.entry_name.bind('<KeyPress>',lambda event : self.on_focus_in(event,self.entry_name))

        self.entry_email.place(x=20,y=110)
        self.entry_name.place(x=20,y=180)

        self.button_confirm=CTkButton(self.frame_5,text="Confirm",font=('Arial Black',20,'bold'),fg_color="black",text_color="white",corner_radius=9,command=lambda : self.add_confirm())
        self.button_confirm.place(x=100,y=290)

        self.button_change_pass=CTkButton(self.frame_5,text="Change password",font=('Arial Black',20,'bold'),fg_color="#4e9501",text_color="black",corner_radius=7,command=self.change_password)



    def add_confirm(self):


            email=self.entry_email.get()
            name=self.entry_name.get()

            exist_email=self.cursor.execute('SELECT * FROM user_ur WHERE email = ?',(email,)).fetchone()

            if exist_email:
                name_org=exist_email[2]
                if name_org==name:

                    self.entry_email.configure(state="readonly",fg_color="#90a955")
                    self.entry_name.configure(state="readonly",fg_color="#90a955")
                    self.entry_email.place_forget()
                    self.entry_name.place_forget()
                    self.label_1.place_forget()
                    self.button_confirm.place_forget()

                    self.label_1.place(x=100,y=20)
                    self.entry_email.place(x=20,y=60)
                    self.entry_name.place(x=20,y=120)
                    self.entry_new_password.place(x=20,y=180)
                    self.entry_new_password_confirm.place(x=20,y=240)

                    self.button_change_pass.place(x=80,y=305)


                else:
                    messagebox.showwarning('mistake','Name error')
                    self.entry_name.configure(border_color="red")
            else:
                messagebox.showwarning('mistake','Email not found')
                self.entry_email.configure(border_color='red')
    
    def change_password(self):
            password=self.entry_new_password.get()
            password_confirm=self.entry_new_password_confirm.get()

            if password == password_confirm:
                self.cursor.execute('UPDATE user_ur SET password = ? WHERE email = ?',(password,self.entry_email.get()))
                self.connect.commit()
                self.connect.close()
                
                self.entry_new_password.configure(state="readonly")
                self.entry_new_password_confirm.configure(state="readonly")

                messagebox.showinfo('success','Password changed successfully')
                self.app.after(2000,lambda : self.back_to_login())
            else:
                messagebox.showwarning('error','password is not the same')


          
    def connect_data(self):
        self.connect=sqlite3.connect('useruser.db')
        self.cursor=self.connect.cursor()

    def back_to_login(self,event="none"):
        self.frame_3.grid_forget()
        self.frame_4.grid_forget()
        self.frame_5.grid_forget()

        self.frame_2.grid(row=0, column=1, sticky="nsew")
        self.frame_1.grid(row=0,column=0,sticky="news")

    def on_focus_in(self,event,name_entry):
        name_entry.configure(border_color="#ccd5ae")
    
    