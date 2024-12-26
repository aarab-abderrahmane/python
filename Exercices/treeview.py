import tkinter as tk
from tkinter import ttk

class AccountCreationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Creation Compte")
        self.root.geometry("1000x600")
        self.root.resizable(False,False)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        self.current_numero = 0

        self.form_frame = tk.Frame(self.root)
        self.form_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        self.create_form()

        self.create_table()

    def create_form(self):
        self.numero_label = tk.Label(self.form_frame, text="Numéro:")
        self.numero_label.grid(row=0, column=0, sticky="w", pady=10)

        self.numero_entry = tk.Entry(self.form_frame, state="disabled")
        self.numero_entry.grid(row=0, column=1, sticky="ew", pady=10)
        self.numero_entry.insert(0, str(self.current_numero))  

        self.proprietaire_label = tk.Label(self.form_frame, text="Propriétaire:")
        self.proprietaire_label.grid(row=1, column=0, sticky="w", pady=10)

        self.proprietaire_entry = tk.Entry(self.form_frame)
        self.proprietaire_entry.grid(row=1, column=1, sticky="ew", pady=10)

        self.solde_initial_label = tk.Label(self.form_frame, text="Solde Initial:")
        self.solde_initial_label.grid(row=2, column=0, sticky="w", pady=10)

        self.solde_initial_entry = tk.Entry(self.form_frame)
        self.solde_initial_entry.grid(row=2, column=1, sticky="ew", pady=10)

        self.euro_label=tk.Label(self.form_frame,text="Euro")
        self.euro_label.grid(row=2,column=2,pady=10,padx=10)

        self.type_label = tk.Label(self.form_frame, text="Type:")
        self.type_label.grid(row=3, column=0, sticky="w", pady=10)

        self.type_var = tk.StringVar(value="Courant")
        self.courant_radio = tk.Radiobutton(self.form_frame, text="Courant", variable=self.type_var, value="Courant")
        self.courant_radio.grid(row=3, column=1, sticky="w", pady=10)

        self.epagne_radio = tk.Radiobutton(self.form_frame, text="Epargne", variable=self.type_var, value="Epargne")
        self.epagne_radio.grid(row=3, column=2, sticky="w", pady=10)

        self.taux_interet_label = tk.Label(self.form_frame, text="Taux Intérêt:")
        self.taux_interet_label.grid(row=4, column=0, sticky="w", pady=10)

        self.taux_interet_entry = tk.Entry(self.form_frame)
        self.taux_interet_entry.grid(row=4, column=1, sticky="ew", pady=10)

        self.m_decouvert_label = tk.Label(self.form_frame, text="M. Découvert:")
        self.m_decouvert_label.grid(row=5, column=0, sticky="w", pady=10)

        self.m_decouvert_entry = tk.Entry(self.form_frame)
        self.m_decouvert_entry.grid(row=5, column=1, sticky="ew", pady=10)

        self.submit_button = tk.Button(self.form_frame, text="Création Compte", command=self.insert_account)
        self.submit_button.grid(row=6, column=0, columnspan=3, pady=20)

    def create_table(self):
        self.table_frame = tk.Frame(self.root)
        self.table_frame.grid(row=1, column=0, sticky="e", padx=20, pady=20)
        column=("#","Numero","Proprietaire",'solde lnitial','type','taux interet','montant decouvert')

        self.treeview = ttk.Treeview(self.table_frame, columns=column, show="headings")
        self.treeview.grid(row=0, column=0, sticky="nsew")
        
        for col in column:
            self.treeview.heading(col,text=col)
            self.treeview.column(col,width=100)
            if col=="montant decouvert" : 
             self.treeview.column(col,width=200)

                



    def insert_account(self):

        self.current_numero += 1
        self.numero_entry.config(state="normal")  
        self.numero_entry.delete(0, tk.END)  
        self.numero_entry.insert(0, str(self.current_numero))
        self.numero_entry.config(state="disabled")  
    

        nothing=""
        numero = self.numero_entry.get()
        proprietaire = self.proprietaire_entry.get()
        solde_initial = self.solde_initial_entry.get()
        type_compte = self.type_var.get()
        taux_interet = self.taux_interet_entry.get()
        m_decouvert = self.m_decouvert_entry.get()


        self.treeview.insert("", "end", values=(nothing,numero, proprietaire, solde_initial, type_compte, taux_interet, m_decouvert))



root = tk.Tk()
app = AccountCreationApp(root)
root.mainloop()
