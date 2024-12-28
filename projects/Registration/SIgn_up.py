from customtkinter import *
from PIL import Image

class SignUpPage:
    def __init__(self, app, frame_2):
        self.app = app
        self.frame_2 = frame_2
        self.frame_2.grid_forget()  

        self.frame_3 = CTkFrame(self.app, corner_radius=0, fg_color="white")
        self.frame_3.grid(row=0, column=0, sticky="nsew")

        self.label_3 = CTkLabel(self.frame_3, text="Sign Up", font=('Helvetica', 24, 'bold'), text_color="black")
        self.label_3.place(x=45, y=20)
        self.change_color()


        self.entry_3 =CTkEntry(self.frame_3,placeholder_text="   Your name",width=320,text_color="black",font=("Arial",15),fg_color="#f2f2f2",height=50,border_color="#f2f2f2")
        self.entry_3.place(x=40, y=70)

        self.entry_4=CTkEntry(self.frame_3,placeholder_text="   Email",width=320,text_color="black",font=("Arial",15),fg_color="#f2f2f2",height=50,border_color="#f2f2f2")
        self.entry_4.place(x=40, y=140)

        self.entry_5=CTkEntry(self.frame_3,placeholder_text="   Password",width=288,text_color="black",font=("Arial",15),fg_color="#f2f2f2",height=50,border_color="#f2f2f2")
        self.entry_5.place(x=40,y=210)

        self.entry_6=CTkEntry(self.frame_3,placeholder_text="   Confirm Password",width=288,text_color="black",font=("Arial",15),fg_color="#f2f2f2",height=50,border_color="#f2f2f2")
        self.entry_6.place(x=40,y=280)

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

        self.eye_button_1 = CTkButton(self.frame_3, image=self.eye_off_icon, text="", width=10, height=50,bg_color="#f2f2f2", fg_color="#f2f2f2",corner_radius=8,hover_color="#f2f2f2",command= lambda : self.toggle_password_visibility(self.entry_5,self.eye_button_1))
        self.eye_button_1.place(x=323, y=210)


        self.eye_button_2 = CTkButton(self.frame_3, image=self.eye_off_icon, text="", width=10, height=50,bg_color="#f2f2f2", fg_color="#f2f2f2",corner_radius=8,hover_color="#f2f2f2",command= lambda : self.toggle_password_visibility(self.entry_6,self.eye_button_2))
        self.eye_button_2.place(x=323, y=280)
        

        # ________frame right


    def register(self):
        email = self.entry_3.get()
        password = self.entry_4.get()

        if email and password:
            messagebox.showinfo("Success", "Successfully signed up!")
        else:
            messagebox.showwarning("Error", "Please fill in all fields")

    def back_to_login(self):
        self.frame_3.grid_forget()

        self.frame_2.grid(row=0, column=1, sticky="nsew")

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