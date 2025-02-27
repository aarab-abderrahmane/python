from abc import ABC ,abstractmethod
from tkinter import *
from tkinter import ttk,messagebox

class Vehicule(ABC):
    def __init__(self,nom_client,matricule,capacite):
        self.nom_client = nom_client
        self.matricule = matricule
        self._capacite = capacite
    
    @abstractmethod
    def Calculer_efficiency(self):
        raise NotImplementedError("La méthode calculer_efficiency() doit être redéfinie dans la sous-classe.")


    def ajuster_capacite(self,valeur):
        self._capacite = max(0,self._capacite+valeur)

    def __str__(self):
        return f'Client : {self.nom_client}  | Matricule : {self.matricule}  | Capicite : {self._capacite} kg'


    def __eq__(self,x):
        if isinstance(x , Vehicule):
            if x.matricule == self.matricule : return True
            else: return False
        
        else : return False
    
    #Decorateurs
    @property
    def capacite(self):
        return self._capacite

    @capacite.setter
    def capacite(self,valeur):
        if valeur < 0 : raise CapaciteError()

        self._capacite = valeur


class Voiture(Vehicule):
    def __init__(self,nom_client,matricule,capacite,consomation):
        super().__init__(nom_client,matricule,capacite)
        self.consomation = consomation
    
    def Calculer_efficiency(self):
        return f't l’autonomie du véhicule en fonction du carburant disponible : {100/self.consomation if self.consomation > 0 else float('inf')}'
    
    


class Camion(Vehicule):
        def __init__(self, nom_client, matricule, capacite,charge_max,consomation):
             super().__init__(nom_client, matricule, capacite)
             self.charge_max=charge_max
             self.consomation = consomation
        
        def Calculer_efficiency(self,charge):
            if charge > self.charge_max : return'0'
            return f'e la distance pouvant être parcourue en fonction de la charge transportée : {100/((1+charge/self.charge_max)*self.consomation)}'
        
             
class CapaciteError(Exception):
    def __init__(self, message="La capacite ne peut pas etre negative."):
        super().__init__(message)


v_1 = Voiture("XYZ Logistics", "123-ABC", 500, 6.5)

print(Voiture.__str__(v_1))
print(v_1)


try : 
    v_1.capacite = -100

except CapaciteError as e : 
    print(e)



try:
    v_2 = Vehicule("Test Client", "999-XYZ", 1000)  
    print(v_2.calculer_efficiency())  
except TypeError as e:
    print(f"Erreur détectée : {e}")



class Winodw : 
    def __init__(self,app):
        self.app = app 
        self.app.title('gestion de flotte automobile')
        self.app.geometry('600x400')

        self.app.bind("<Return>",self.update_table)

        #GUI

        self.label_nom = Label(self.app, text="Nom")
        self.entry_nom = Entry(self.app , width = 40)
        self.label_nom.pack(pady=10)
        self.entry_nom.pack(pady=0)

        self.label_matricule = Label(self.app , text="Matricule")
        self.entry_matricule = Entry(self.app,width=40)
        self.label_matricule.pack(pady=10)
        self.entry_matricule.pack(pady=0)

        self.label_capacite = Label(self.app,text="Capacite")
        self.entry_capacite = Entry(self.app , width=40)
        self.label_capacite.pack(pady=10)
        self.entry_capacite.pack(pady=0)

        self.select_type = ttk.Combobox(self.app , values = ('Voiture','Camion'))
        self.select_type.set("Options")
        self.select_type.pack(pady=10)

        # print(self.select_type.get() if self.select_type.get() is not None else "None")

        self.button_add = Button(self.app , text="Ajouter",command=self.update_table)
        self.button_add.pack(pady=10)

        self.tree_view = ttk.Treeview(self.app , columns=('nom',"matricule",'capacite','type','efficacite_estimee'),show="headings")
        self.tree_view.heading("nom",text="nom client")
        self.tree_view.heading('matricule',text="matricule")
        self.tree_view.heading('capacite',text='capacite')
        self.tree_view.heading('type',text="type")
        self.tree_view.heading('efficacite_estimee',text="efficacité estimée")

        for col in ('nom',"matricule",'capacite','type'):
            self.tree_view.column(col,width=50)

       
        self.tree_view.pack(fill='both',side="bottom")
        self.tree_view.bind('<ButtonRelease-1>',self.Delete_row)



    def update_table(self,evnet=None):
        try : 

            type_véhicule = self.select_type.get()
            nom = self.entry_nom.get()
            matricule = self.entry_matricule.get()
            capacite = self.entry_capacite.get()
            if not capacite.isdigit()  or float(capacite) <0:
                messagebox.showerror('Error','You must enter a positive number in the field <Capacite>.')
                return
        
            if type_véhicule =="Options" : 
                messagebox.showwarning('Warning','You must to choose theh option to continue.') 
                return

            elif type_véhicule =="Voiture":
                vehivule = Voiture(nom,matricule,capacite,25)

            else:
                vehivule = Camion(nom,matricule,capacite,100,40)
    
            self.tree_view.insert("","end",values=(nom,matricule,float(capacite),type_véhicule,vehivule.Calculer_efficiency))
    
            for entry in (self.entry_capacite,self.entry_matricule,self.entry_nom):
                if entry.get():
                 entry.delete(0,END)

        except TypeError as e : 
            return e
        
    
    def Delete_row(self,event=None) :
        selection_item = self.tree_view.selection()
        if not selection_item : return
        for item in selection_item : 
            self.tree_view.delete(item)

        



app = Tk()
Winodw(app)
app.mainloop()