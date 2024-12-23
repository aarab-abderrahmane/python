from tkinter import *
from tkinter import ttk , messagebox
# from ttkbootstrap import *

class Contacts : 
    def __init__ (self,name,last_name,contry,gender,phone,email):
        self.name=name
        self.last_name=last_name
        self.contry=contry
        self.gender=gender
        self.phone=phone
        self.email=email



    def insert(self):
        tree.insert("","end",values=(self.name,self.last_name,self.contry,self.gender,self.phone,self.email))
    

def delete_item():
    selected=tree.selection()

    if not selected:
        messagebox.showwarning('no selection','please selected item to delete')
        return
    
    for item in selected:
        tree.delete(item)
    
    messagebox.showinfo('success','selected row(s) deleted successfully')



root=Tk()
root.geometry("600x300")

button_delete=Button(root,text="Delete",bg="red",command=delete_item)
button_delete.pack(side="bottom",fill="x")

column=['name','last name','contry','gender','phone','email']
tree=ttk.Treeview(root,column=column,show="headings",height=280,selectmode="extended")

for col in column : 
    tree.heading(col,text=col)
    tree.column(col,width=100)

tree.pack(fill="both",side="top")



# ______________________________

while True : 
  name=input("type your name : ").strip()
  last_name=input("type your last name : ").strip()
  contry=input("type contry name : ").strip()
  gender=input("type type gender : ").strip()
  phone=input('type your number phone : ').strip()
  email=input('type your email : ').strip()

  contact=Contacts(name,last_name,contry,gender,phone,email)
  contact.insert()



root.mainloop()