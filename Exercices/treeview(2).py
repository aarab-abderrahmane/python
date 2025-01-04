from tkinter import *
from tkinter import ttk,messagebox
import sqlite3


class Account:
    def __init__(self, root):
        self.root = root
        self.root.title("Account Manager")
        self.root.geometry('400x300')

        self.connect = sqlite3.connect('account.db')
        self.cursor = self.connect.cursor()
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS account (
                    name TEXT,
                    last_name TEXT
                )
        ''')
        self.connect.commit()


        self.frame_left = Frame(self.root, bg="black", width=600)
        self.frame_right = Frame(self.root, bg="white")

        self.frame_left.pack(side="left", fill="both")
        self.frame_right.pack(side="right",  fill="both")

        self.label_1=Label(self.frame_left,text="your name",fg="white")
        self.label_1.place(x=10,y=10)

        self.entry_1=Entry(self.frame_left,width=100)
        self.entry_1.place(x=10,y=40)


        self.label_2=Label(self.frame_left,text="your name",fg="white")
        self.label_2.place(x=10,y=60)

        self.entry_2=Entry(self.frame_left,width=100)
        self.entry_2.place(x=10,y=90)


        column=('name',"last_name")
        self.tree=ttk.Treeview(self.frame_right,columns=column,show="headings")

        for col in column:
            self.tree.heading(col,text=col)
        
        self.tree.pack(fill='y')

        self.button_add=Button(self.frame_left,text="ADD",command=self.add_button)
        self.button_add.place(x=10,y=140)

        self.button_delete=Button(self.frame_left,text="DELETE",command=self.delete_button)
        self.button_delete.place(x=100,y=140)

        self.button_update=Button(self.frame_left,text="UPDATE",command=self.update_row)
        self.button_update.place(x=200,y=140)


        self.update_table()


    def update_table(self):
            for row in self.tree.get_children():
                self.tree.delete(row)
            
            
            row=self.cursor.execute('SELECT * FROM account').fetchall()
            for item in row:
                self.tree.insert('','end',values=item)

        
    def add_button(self):
            name=self.entry_1.get()
            last_name=self.entry_2.get()

            self.cursor.execute('INSERT INTO account (name,last_name) VALUES (?,?)',(name,last_name,))
            self.connect.commit()

            self.update_table()

    def delete_button(self):

        selection_item=self.tree.selection()

        if not selection_item:
            messagebox.showwarning('no selection',"please select item to delete")
            return
        # messagebox.askyesno

        for item_ in selection_item:

            item_value=self.tree.item(item_,'values')

            if item_value:

                name,last_name=item_value


                self.cursor.execute('DELETE FROM account WHERE name = ? AND last_name = ?',(name,last_name,))
                self.connect.commit()

                self.tree.delete(item_)

    
    def update_row(self):
        selection_item=self.tree.selection

        if len(selection_item)!=1:
            messagebox.showwarning('error','please select one of the table')

            return
        
        selected_item=selection_item[0]
        old_name ,old_last_name=self.tree.item(selected_item,'values')

        name = self.entry_1.get()
        last_name = self.entry_2.get()


        self.tree.item(selected_item,values=(name,last_name))


        #update database

        self.cursor.execute('''
            UPDATE account
            SET name = ? , last_name = ?
            WHERE name = ? AND last_name = ?
        
        ''',(name,last_name,old_name,old_last_name))

        self.connect.commit()

    
    
        





root = Tk()
app = Account(root)
root.mainloop()
