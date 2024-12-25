from customtkinter import * 
import customtkinter as ck
from tkinter import messagebox
from for_customtkinter import on_hover ,on_leave



def calculer():
    revenus=entry_1.get()
    electricite=entry_2.get()
    eau=entry_3.get()
    telephone=entry_4.get()


    for i in [revenus,electricite,eau,telephone]:
        if not i.isdigit():
            messagebox.showwarning('Error',"All fields must be filled out and type a correct number")
            return
    
    

    revenus=int(revenus)
    electricite=int(electricite)
    eau=int(eau)
    telephone=int(telephone)
    
    total_des_charges=(electricite+eau+telephone)
    result_=(revenus)-(total_des_charges)
    total_des_revenus=revenus

    result.set(result_)
    t_charges.set(total_des_charges)
    t_revenus.set(total_des_revenus)


def ajouter_charge():

    y_n=30
    
    if not hasattr(ajouter_charge,"add") :
        ajouter_charge.add=""

        entry_autres.place(y=310,x=20)
        
        button_calcule.place_forget()
        button_calcule.place(x=20,y=430+y_n-5)

        button_ajouter.place_forget()
        button_ajouter.configure(text="return")
        button_ajouter.bind('<Enter>',lambda event : on_hover(event,button_ajouter,"white","red"))
        button_ajouter.bind("<Leave>",lambda event : on_leave(event,button_ajouter,"white","gray"))
        button_ajouter.place(x=20,y=310+y_n+10)

        label_5.place_forget()
        entry_5.place_forget()
        label_5.place(x=20,y=350+y_n)
        entry_5.place(x=20,y=380+y_n)

        label_6.place_forget()
        entry_6.place_forget()
        label_6.place(x=180,y=350+y_n)
        entry_6.place(x=180,y=380+y_n)

        label_7.place_forget()
        entry_7.place_forget()
        label_7.place(x=340,y=350+y_n)
        entry_7.place(x=340,y=380+y_n)

    else: 
        del ajouter_charge.add


        entry_autres.place_forget()
        button_calcule.place_forget()
        button_calcule.place(x=20,y=430)

        button_ajouter.place_forget()
        button_ajouter.place(x=20,y=310)
        button_ajouter.configure(text="Ajouter charge")
        button_ajouter.bind('<Enter>',lambda event : on_hover(event,button_ajouter,"white","#f77f00"))
        button_ajouter.bind("<Leave>",lambda event : on_leave(event,button_ajouter,"white","gray"))


        label_5.place_forget()
        entry_5.place_forget()
        label_5.place(x=20,y=350)
        entry_5.place(x=20,y=380)

        label_6.place_forget()
        entry_6.place_forget()
        label_6.place(x=180,y=350)
        entry_6.place(x=180,y=380)

        label_7.place_forget()
        entry_7.place_forget()
        label_7.place(x=340,y=350)
        entry_7.place(x=340,y=380)


        
    




app=CTk()
app.geometry('500x490')
app.title('activite calcul')
ck.set_appearance_mode("darck")

label_1=CTkLabel(app,text="Revenus")
label_1.place(x=20,y=20)

entry_1=CTkEntry(app,width=460,corner_radius=5,placeholder_text="100",placeholder_text_color="yellow",text_color="white")
entry_1.place(x=20,y=50)


label_2=CTkLabel(app,text="Electricite")
label_2.place(y=90,x=20)

entry_2=CTkEntry(app,width=460,corner_radius=5,placeholder_text="300",placeholder_text_color="yellow",text_color="white")
entry_2.place(y=120,x=20)


label_3=CTkLabel(app,text="Eau")
label_3.place(y=160,x=20)

entry_3=CTkEntry(app,width=460,corner_radius=5,placeholder_text="198",placeholder_text_color="yellow",text_color="white")
entry_3.place(y=190,x=20)


label_4=CTkLabel(app,text="Telephone")
label_4.place(y=230,x=20)

entry_4=CTkEntry(app,width=460,corner_radius=5,placeholder_text="299",placeholder_text_color="yellow",text_color="white")
entry_4.place(y=260,x=20)

# _________________ajouter charge
button_ajouter=CTkButton(app,width=460,text="Ajouter Charge",fg_color="gray",command=ajouter_charge)
button_ajouter.place(y=310,x=20)

button_ajouter.bind('<Enter>',lambda event : on_hover(event,button_ajouter,"white","#f77f00"))
button_ajouter.bind("<Leave>",lambda event : on_leave(event,button_ajouter,"white","gray"))

# _________________________________________
label_5=CTkLabel(app,text="Resultat")
label_5.place(x=20,y=350)

result=StringVar()
result.set('    - - - - - - -')
entry_5=CTkEntry(app,textvariable=result,state="readonly")
entry_5.place(x=20,y=380)



label_6=CTkLabel(app,text="Totale des charges")
label_6.place(x=180,y=350)

t_charges=StringVar()
t_charges.set('    - - - - - - -')
entry_6=CTkEntry(app,textvariable=t_charges,state="readonly")
entry_6.place(x=180,y=380)



label_7=CTkLabel(app,text="Total des revenus")
label_7.place(x=340,y=350)

t_revenus=StringVar()
t_revenus.set('    - - - - - - -')
entry_7=CTkEntry(app,textvariable=t_revenus,state="readonly")
entry_7.place(x=340,y=380 )
# __________________________

button_calcule=CTkButton(app,text="Calculer",fg_color="#020203",command=calculer,width=460)
button_calcule.place(x=20,y=430 )



# _____anouther entry
entry_autres=CTkEntry(app,width=460,placeholder_text="text")




app.mainloop()