# Créer la classe Entreprise avec l'attribut : listEmploye=[]
# et les methodes : 
# ****** AddEmploye
# ***** RemoveEmploye 
# *****FindEmploye by matricule
# *****getOldestEmp
# *****getYoungestEmp
# ****serialize in json file

from tkinter import *
import sqlite3
from tkinter import ttk

class Entreprise : 

    def __init__(self,root):
        
        #list
        list_Employe=[]

        #window

        self.root=root
        self.root.title('List Employes')
        self.root.geometry('700x400')
        self.root.resizable(False,False)

        #left frame
        self.frame_left=Frame(root,bg="#e5e5e5",width=300,height="400")
        self.frame_left.pack(side="left",fill="both",expand=True)

        self.matricule=Entry(self.frame_left,width=50,state="readonly")
        self.matricule.place(x=10,y=10)
        

        #right frame
        self.frame_right=Frame(root,width=300,bg="white",height=400)
        self.frame_right.pack(side="right",fill="both",expand=True)


        #data 

        self.connect=sqlite3.connect('listemploye.db')
        self.cursor=self.connect.cursor()
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS emplyes(
                    matricule INTEGER PRIMARY KEY,
                    nom TEXT,
                    datenaissance TEXT
                            )
        ''')

        self.connect.commit()

        #treeview 
        self.tree=ttk.Treeview(self.frame_right,columns=('matricule','nom','date naissance'),show='headings',height=20)
        for col in ('matricule','nom','date naissance'):
            self.tree.heading(col,text=col)
            self.tree.column(col,width=100)
        
        self.tree.pack(fill="both")


    def AddEmploye(self):
        pass


        


root=Tk()

window=Entreprise(root)
root.mainloop()