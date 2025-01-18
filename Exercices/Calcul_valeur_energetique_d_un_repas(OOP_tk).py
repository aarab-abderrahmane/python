from tkinter import * 
from tkinter import messagebox

class Aliment : 
     def __init__(self,nom,valeur_energetique):
          self.nom= nom 
          self.energetique=valeur_energetique
        
     def calculer_valeur(self,qunatite):
          return self.energetique * qunatite

class Pain(Aliment):
    def __init__(self) :
          super().__init__('Pain',2.75)

class Viande(Aliment):
     def __init__(self):
          super().__init__('Viande',1.80)


class Application(Tk):
    def __init__(self):
        super().__init__()
        self.title("Calcul de la valeur energetique d'un repas")
        self.geometry('500x500')

        #Initianlisation des aliments 
        self.pain=Pain()
        self.viande=Viande()


        #Interface 

        self.label=Label(self,text="Choisir les aliments qui composent votre repas",font=('Arial',14,'bold'))
        self.label.place(x=20,y=30)

        #Pain
        self.pain_var=IntVar(value=1)

        self.pain_chek=Checkbutton(self,text="Pain",variable=self.pain_var,font=('Arial',15),command= lambda : self.Active_button(self.pain_input,self.pain_var))
        self.pain_chek.place(x=10,y=100)

        self.pain_input=Entry(self,width=40)
        self.pain_input.place(x=120,y=120)

        #viande 
        self.viande_var=IntVar(value=0)

        self.viande_chek=Checkbutton(self,text="viande",variable=self.viande_var,font=('Arial',15),command=lambda : self.Active_button(self.viande_input,self.viande_var))
        self.viande_chek.place(x=10,y=200)

        self.viande_input=Entry(self,width=40)
        self.viande_input.place(x=120,y=220)

        self.Active_button(self.viande_input,self.viande_var)


        #Legumes
        self.legumes_var=IntVar(value=0)

        self.legumes_chek=Checkbutton(self,text="legumes",variable=self.legumes_var,font=('Arial',15),command=lambda : self.Active_button(self.legumes_input,self.legumes_var))
        self.legumes_chek.place(x=10,y=300)

        self.legumes_input=Entry(self,width=40)
        self.legumes_input.place(x=120,y=320)

        self.Active_button(self.legumes_input,self.legumes_var)

        #Banane 
        self.banane_var=IntVar(value=0)

        self.banane_chek=Checkbutton(self,text="banane",variable=self.banane_var,font=('Arial',15),command=lambda : self.Active_button(self.banane_input,self.banane_var))
        self.banane_chek.place(x=10,y=400)

        self.banane_input=Entry(self,width=40)
        self.banane_input.place(x=120,y=420)

        self.Active_button(self.banane_input,self.banane_var)


    def Active_button(self,name_entry,name_var):
            if name_var.get()==1:
                name_entry.config(state="normal")
            else: 
                name_entry.config(state='disabled')



if __name__ == "__main__":
    app=Application()
    app.mainloop()