from customtkinter import * 
import customtkinter as ck

class Sign : 

    def __init__ (self,app):

        self.app=app
        self.app.geometry("600x400")
        self.app.title('Sign In')

        self.app.grid_columnconfigure(0,weight=1,uniform="equal")
        self.app.grid_columnconfigure(1,weight=1,uniform="equal")
        self.app.grid_rowconfigure(0,weight=1)


        self.frame_1=CTkFrame(app,corner_radius=0,fg_color="red")
        self.frame_1.grid(row=0,column=0,sticky="news")

        self.frame_2=CTkFrame(app,corner_radius=0,fg_color="blue")
        self.frame_2.grid(row=0,column=1,sticky="news")

        




app=CTk()

window=Sign(app)
app.mainloop()