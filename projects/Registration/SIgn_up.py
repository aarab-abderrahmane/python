from customtkinter import *
from PIL import Image
from tkinter import messagebox
import sqlite3


class SignUpPage:
    def __init__(self, app, frame_2,frame_1):
        self.app = app
        self.frame_2 = frame_2
        self.frame_1=frame_1

        self.connect_data()

        self.frame_1.grid_forget()
        self.frame_2.grid_forget()  

        self.frame_3 = CTkFrame(self.app, corner_radius=0, fg_color="white")
        self.frame_3.grid(row=0, column=0, sticky="nsew")

        self.label_3 = CTkLabel(self.frame_3, text="Sign Up", font=('Arial Black', 24, 'bold'), text_color="black")
        self.label_3.place(x=150, y=40)
        self.change_color()


        self.entry_3 =CTkEntry(self.frame_3,placeholder_text="   Your name",width=320,text_color="black",font=("Arial",15),fg_color="#f5ebe0",height=50,border_color="#f5ebe0")
        self.entry_3.place(x=40, y=90)
        self.entry_3.bind("<KeyPress>",lambda event : self.on_focus_in(event,self.entry_3))

        self.entry_4=CTkEntry(self.frame_3,placeholder_text="   Email",width=320,text_color="black",font=("Arial",15),fg_color="#f5ebe0",height=50,border_color="#f5ebe0")
        self.entry_4.place(x=40, y=160)
        self.entry_4.bind('<KeyPress>',lambda event : self.on_focus_in(event,self.entry_4))

        self.entry_5=CTkEntry(self.frame_3,placeholder_text="   Password",width=288,text_color="black",font=("Arial",15),fg_color="#f5ebe0",height=50,border_color="#f5ebe0")
        self.entry_5.place(x=40,y=230)

        self.entry_6=CTkEntry(self.frame_3,placeholder_text="   Confirm Password",width=288,text_color="black",font=("Arial",15),fg_color="#f5ebe0",height=50,border_color="#f5ebe0")
        self.entry_6.place(x=40,y=300)

        self.button_sign_up = CTkButton(self.frame_3, text="Sign Up", text_color="white", fg_color="#007bff", width=210,
                                        height=40, corner_radius=8, font=('Helvetica', 15, 'bold'), command=self.register)
        # self.button_sign_up.place(x=40, y=210)

        self.button_back_to_login = CTkButton(self.frame_3, text="Back to Login", text_color="white", fg_color="#333333", width=100,
                                              height=40, font=('Helvetica', 15, 'bold'),corner_radius=5, command=self.back_to_login)
        # self.button_back_to_login.place(x=260, y=210)


        self.eye_off_icon = Image.open("eye.png") 
        self.eye_icon = Image.open("view.png")  
        
        self.eye_off_icon = CTkImage(self.eye_off_icon, size=(20, 20))
        self.eye_icon = CTkImage(self.eye_icon, size=(20, 20))

        self.eye_button_1 = CTkButton(self.frame_3, image=self.eye_off_icon, text="", width=10, height=50,bg_color="#f5ebe0", fg_color="#f5ebe0",corner_radius=8,hover_color="#f5ebe0",command= lambda : self.toggle_password_visibility(self.entry_5,self.eye_button_1))
        self.eye_button_1.place(x=323, y=230)


        self.eye_button_2 = CTkButton(self.frame_3, image=self.eye_off_icon, text="", width=10, height=50,bg_color="#f5ebe0", fg_color="#f5ebe0",corner_radius=8,hover_color="#f5ebe0",command= lambda : self.toggle_password_visibility(self.entry_6,self.eye_button_2))
        self.eye_button_2.place(x=323, y=300)
            

        # ________frame right
        self.frame_4=CTkFrame(self.app,corner_radius=0,fg_color="white")
        self.frame_4.grid(row=0,column=1,sticky="news")

        self.image = Image.open("image_1.png")

        self.image = self.image.resize((300, 300)) #ext
        self.photo = CTkImage(self.image, size=(380, 380))  #inter
        
        self.image_label = CTkLabel(self.frame_4, image=self.photo, text="")
        self.image_label.grid(row=0, column=0,pady=30)
        



        # ____button__

        self.button_register=CTkButton(self.frame_3,text="REGISTER",font=('Helvetica',14,'bold'),fg_color="black",text_color="white",width=320,height=45,corner_radius=10,command=self.register)
        self.button_register.place(x=40,y=360)
        
        self.label_4=CTkLabel(self.frame_3,text="Login",font=('Arial Black',14,'bold'),text_color="black",cursor="hand2")
        self.label_4.bind("<Button-1>",self.back_to_login)
        self.label_4.place(x=150,y=410)

        self.label_5=CTkLabel(self.frame_3,text="with Others",font=('Arial',14),text_color="black")
        self.label_5.place(x=195,y=410)


    def connect_data(self):
        # _____data_______
        self.connect=sqlite3.connect('useruser.db')
        self.cursor=self.connect.cursor()


    def register(self):
        name=self.entry_3.get()
        email=self.entry_4.get()
        password=self.entry_5.get()
        confirm_password=self.entry_6.get()


        exist=self.cursor.execute('SELECT * FROM user_ur WHERE email = ? OR name = ?',(email,name,)).fetchone()
        if exist : 
            exist_email=self.cursor.execute('SELECT * FROM user_ur WHERE email = ?',(email,)).fetchone()
            if exist_email : 
                exist_name=self.cursor.execute('SELECT * FROM user_ur WHERE name = ?',(name,)).fetchone()
                
                if exist_name: 
                    self.entry_3.configure(border_color="#ef476f")
                    self.entry_4.configure(border_color="#ef476f")
                    messagebox.showwarning('Registration Error','Email and name already exists. Please choose a different one.')
                else:
                    self.entry_4.configure(border_color="#ef476f")
                    messagebox.showwarning('Registration Error','Email already exists. Please choose a different one.')
                 
            else:
                self.entry_3.configure(border_color="#ef476f")
                messagebox.showwarning('Registration Error','Name already exists. Please choose a different one.')

        else:
            self.cursor.execute('INSERT INTO user_ur (email,password,name) VALUES (?,?,?)',(email,password,name))
            self.connect.commit()
            print("success")
        

        
    def on_focus_in(self,event,name_entry):
        name_entry.configure(border_color="#f5ebe0")

    def back_to_login(self,event="none"):
        self.frame_3.grid_forget()
        self.frame_4.grid_forget()

        self.frame_2.grid(row=0, column=1, sticky="nsew")
        self.frame_1.grid(row=0,column=0,sticky="news")
        
    def change_color(self):
        current_color=self.label_3.cget("text_color")
        if current_color == "black":
            new_color = "dodgerblue"  
        elif current_color == "dodgerblue":
            new_color = "darkorange"  
        elif current_color == "darkorange":
            new_color = "forestgreen"  
        elif current_color == "forestgreen":
            new_color = "black" 
        
        self.label_3.configure(text_color=new_color)
        self.app.after(1000,self.change_color)


    def toggle_password_visibility(self,name_entry,name_button):
        if name_entry.cget("show") == "*":
            name_entry.configure(show="")  
            name_button.configure(image=self.eye_off_icon) 
        else:
            name_entry.configure(show="*")  
            name_button.configure(image=self.eye_icon)