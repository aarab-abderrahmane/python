from abc import ABC,abstractmethod
from tkinter import *
from tkinter import ttk ,messagebox

class AdCampaign(ABC) : 
    def __init__(self,nom,budget,canal) :
        self.nom = nom 
        self._budget = budget
        self.canal = canal


    @abstractmethod
    def Calculer_portée(self):
        raise NotImplementedError('error 101.')

    # Decorators
    @property 
    def budget(self): #getter
        return self._budget
    
    @budget.setter 
    def budget(self,value):
        if value <=0 :
            raise InvalidBidgetError()
        
        self._budget = value


    def afficher_details(self):
        return f"Nom : {self.nom} , Budget : {self.budget} ,canal : {self.canal}"
    
    def __str__(self):
        return f'Compagne : {self.nom} | budget : {self.budget} | Canal : {self.canal}'


    def __eq__(self,other):
        if isinstance(other,AdCampaign):
            return self.nom == other.nom and self.budget == other.budget and self.canal == other.canal

        return False
    




class InvalidBidgetError(Exception):
    def __int__(self,message = "le budget ne peut pas etre negatif ou nul."):
        super().__init__(message)


class GoogleAdsCampaign(AdCampaign):
    def __init__(self, nom, budget, canal,cpc):
        super().__init__(nom,budget,canal)
        self.cpc = cpc

    def Calculer_portée(self):
        return self.budget / self.cpc
    
    def afficher_details(self):
        return f"{super().afficher_details()} , nombre par clic : {self.Calculer_portée()}"
    

    
class FacebookAdsCampaign(AdCampaign):
    def __init__(self,nom,budget,canal,cpm):
        super().__init__(nom,budget,canal)
        self.cpm=cpm
    
    def Calculer_portée(self):
        return f"le nombre d'inmpressions : {(self.budget / self.cpm) *1000}"
    
    def afficher_details(self):
        return f"{super().afficher_details()} ,le nombre d'impressions : {self.Calculer_portée()}"
    

class YoutubeAdsCampaign(AdCampaign):
    def __init__(self, nom, budget, canal,cpv):
        super().__init__(nom, budget, canal)
        self.cpv = cpv
    
    def Calculer_portée(self):
        return f'le nombre de vues estimees : {self.budget / self.cpv}'
    
    def afficher_details(self):
        return super().afficher_details() + f" ,le nombre de vues estimees : {self.Calculer_portée()}"
    


class Window:
    def __init__(self,app):
        self.app =app
        self.app.title="Gestion des publication"
        self.app.geometry('600x400')
        self.app.resizable(False,False)

        #GUI
        self.emty_row = Label(self.app,text="")
        self.emty_row.grid(row=0,column=0)

        self.nom_var = StringVar()
        self.label_nom = Label(self.app , text="nom : ")
        self.label_nom.grid(row=1,column=1)
        self.entry_nom = Entry(self.app,width=40,textvariable=self.nom_var)
        self.entry_nom.grid(row=2,column=1)

        self.budget_var = StringVar()
        self.label_budget = Label(self.app,text="budget : ")
        self.label_budget.grid(row=3,column=1,)
        self.entry_budget= Entry(self.app , width=40,textvariable=self.budget_var)
        self.entry_budget.grid(row=4,column=1)

        self.publicite_var = StringVar()
        self.label_publicité = Label(self.app , text="Puclicité : ") 
        self.label_publicité.grid(row=5,column=1)
        self.entry_publicité = Entry(self.app , width=40,textvariable=self.publicite_var)
        self.entry_publicité.grid(row=6,column=1)


        self.button_add = Button(self.app ,command=self.Ajouter, text="Ajouter",background="green" ,foreground="white")
        self.button_add.grid(row=7 ,column=1)

        self.button_delete = Button(self.app, command=self.Delete_row,text="Delete",background="red",foreground="white")
        self.button_delete.grid(row=8,column=1,pady=10)

        #treeview 
        column = ('Nom','Budget','Canal','Type')
        self.tree = ttk.Treeview(self.app,columns=column,show="headings")
        self.tree.bind("<ButtonRelease-1>",lambda  event : self.Delete_row(event))
        for col in column : 
            self.tree.heading(col, text=col)
            self.tree.column(col, width=145,anchor="center")

        self.tree.grid(row=10,column=1)

    
    def Ajouter(self):
        nom = self.entry_nom.get()
        budget = self.entry_budget.get()
        publicite = self.entry_publicité.get()

        if not nom or not budget : 
            messagebox.showerror('Error',"le budget doit etre un nombre positif.")
            return
        
    
        try : 
            budget = float(budget)
            if budget <=0 :
                raise InvalidBidgetError()
                
        except ValueError : 
            messagebox.showerror('Error','le budget doit etre un nombre posifit.')
            return
        
        if publicite.lower() =="google ads":
           campaign = GoogleAdsCampaign(nom,budget,"Digital",cpc=0.5)
        
        elif publicite.lower() == "facebook ads":
           campaign = FacebookAdsCampaign(nom,budget,"Social Media",cpm=6)
        
        else :
           campaign = YoutubeAdsCampaign(nom,budget,"Video",cpv=0.4)

        
        self.tree.insert("","end",values=(campaign.nom,campaign.budget,campaign.canal,publicite))

        self.entry_nom.delete(0,END)
        self.entry_budget.delete(0,END)
        self.entry_publicité.delete(0, END)


    def Delete_row(self,event=None):            
        selection_item = self.tree.selection()
        if not selection_item : 
            return "None"

        if event is not None :
            answer = messagebox.askquestion('Action',"Do you want to delee this row or edit it ?")

            if answer is None:
                return
            
            elif answer=="yes":
                pass

            else : 

                for sel in  selection_item:
                    old_values = self.tree.item(sel,"values")
                    nom,budget,canal,publicite = old_values
                 
                    self.entry_nom.insert(0,nom)
                    self.entry_budget.insert(0,budget)
                    self.entry_publicité.insert(0,publicite)

                    self.button_add.grid_forget()

                    self.save_button = Button(self.app,text="Save",background="blue",foreground="white",command= lambda : self.Update_row(sel,canal))
                    self.save_button.grid(row=9,column=1,pady=10)

                return 

        for sel in selection_item : 
            self.tree.delete(sel)
    

    def Cleaning(self):
        self.entry_nom.delete(0,END)
        self.entry_budget.delete(0,END)
        self.entry_publicité.delete(0,END)

    def Update_row(self,old_item,old_canal):
        selection_row = self.tree.selection()
        if not selection_row : 
            return
        
        new_nom = self.entry_nom.get()
        new_budget = self.entry_budget.get()
        new_publicite = self.entry_publicité.get()

        self.tree.item(old_item,values=(new_nom,new_budget,old_canal,new_publicite))

        self.Cleaning()

        self.save_button.grid_forget()
        self.button_add.grid(row=9,column=1,pady=10)

    
        


app=Tk()
window_1 = Window(app)

app.mainloop()