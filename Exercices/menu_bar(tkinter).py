# menu_bar
# file_menu = tk.Menu(menu_bar, tearoff=0) 
# file_menu.add_command(label="New", command=new_file)
# menu_bar.add_cascade(label="File", menu=file_menu)
# file_menu.add_separator()


import tkinter as tk
from tkinter import ttk

step=True
def change_color():
    global step
    if step:
     root.config(bg="green")
     step=not step
    else:
       root.config(bg="red")
       step=not step

root=tk.Tk()
root.geometry("200x200")
root.title('menu bar')


menu_bar=tk.Menu(root)

# _____________file
file_menu=tk.Menu(menu_bar,tearoff=0)

file_menu.add_command(label="New",command=change_color)
file_menu.add_command(label="Open",command=change_color)
file_menu.add_command(label="Save",command=change_color)
file_menu.add_separator()

# _____________________Edit
edit_menu=tk.Menu(menu_bar,tearoff=0)

edit_menu.add_command(label="Undo",command=change_color)
edit_menu.add_separator()
edit_menu.add_command(label="Redo",command=change_color)

# ________________help
help_menu=tk.Menu(menu_bar,tearoff=0)

help_menu.add_command(label="About",command=change_color)

# ________________________________________________________

menu_bar.add_cascade(label="File",menu=file_menu)
menu_bar.add_cascade(label="Edit",menu=edit_menu)
menu_bar.add_cascade(label="Help",menu=help_menu)


root.config(menu=menu_bar)
root.mainloop()

