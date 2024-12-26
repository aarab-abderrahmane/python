from customtkinter import *
import customtkinter as ck
from for_customtkinter import on_hover,on_leave
import math
from rich.console import Console

root=CTk()
ck.set_appearance_mode("light")



class Area : 
    def __init__ (obj,root):
        obj.root=root
        obj.root.geometry("400x250")
        obj.root.title('Area calculation')
        obj.root.resizable(False,False)

        obj.radio_var=IntVar(value=1)

        obj.radio_1=CTkRadioButton(master=root,text="circle",command=obj.change_color,variable=obj.radio_var,value=1,fg_color="green",hover_color="green",text_color="green")
        obj.radio_2=CTkRadioButton(master=root,text="rectangle",command=obj.change_color,variable=obj.radio_var,value=2,fg_color="red",hover_color="green",text_color="black")


        obj.radio_1.place(x=100,y=30)
        obj.radio_2.place(x=250,y=30)

        obj.label_1=CTkLabel(master=root,text="length",font=('Arial',20))
        obj.label_1.place(x=40,y=100)
        
        obj.entry_1=CTkEntry(master=root,placeholder_text="302",border_color="black",width=200)
        obj.entry_1.place(x=160,y=100)


        obj.label_2=CTkLabel(master=root,text="width",font=('Arial',20))
        obj.label_2.place(x=40,y=150)
        
        obj.entry_2=CTkEntry(master=root,border_color="black",width=200,state="readonly",fg_color="gray")
        obj.entry_2.place(x=160,y=150)


        obj.button_calcul=CTkButton(master=root,text="Calculate",hover_color="green",corner_radius=0,command=obj.calcultae_area)
        obj.button_calcul.pack(side="bottom",fill="x")


    def change_color(obj):
        if obj.radio_var.get()==1:
            obj.radio_1.configure(fg_color="green",text_color="green")
            obj.radio_2.configure(fg_color="red",text_color="black")

            obj.entry_2.configure(state="readonly",placeholder_text="",fg_color="gray")
        else:
            obj.radio_1.configure(fg_color="red",text_color="black")
            obj.radio_2.configure(fg_color="green",text_color="green")

            obj.entry_2.configure(state="normal",placeholder_text="302",fg_color="white")
        


    def calcultae_area(obj):
        try: 
            if obj.radio_var.get()==1:
                radius=float(obj.entry_1.get())
                area=math.pi * (radius**2)

                result=f"Area of Circle : {area:.2f}"
            else:
                lenght=float(obj.entry_1.get())
                width=float(obj.entry_2.get())
                area=lenght * width

                result=f"Area of Rectangle : {area:.2f}"
            
            obj.show_result(result)       
        
        except: 
            obj.show_result("Please enter valid number")
            

    def show_result(obj,result):

        result_window = CTkToplevel(obj.root)
        result_window.geometry("300x100")
        result_window.title("Result")

        result_label=CTkLabel(master=result_window,text=result,font=('Arial',20,'bold'),text_color="red")
        result_label.pack(pady=50)



app=Area(root)
root.mainloop()