import os
import subprocess
import customtkinter as ctk
from tkinter import filedialog, messagebox
import sqlite3



ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("GitHub Push GUI")
app.geometry("500x300")
app.resizable(False,False)



def reload_data():

    
    cursor.execute('SELECT path FROM modifs')
    mdf=cursor.fetchall()

    if mdf :
        folder_entry.delete(0,'end')
        folder_entry.insert(0,mdf[0])

    else : pass



def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_entry.delete(0,'end')
        folder_entry.insert(0,str(folder))

        cursor.execute("DELETE FROM modifs")

        cursor.execute('INSERT INTO modifs (path) VALUES (?)',(folder,))
        connect.commit()


def push_to_github():
    repo_path = folder_entry.get().strip()
    commit_message = commit_entry.get().strip()

    if not repo_path:
        messagebox.showerror("error", "Please select a project folder.")
        return
    
    if not commit_message:
        messagebox.showerror("error", "Please enter a commit message.")
        return
    
    try:
        subprocess.run(["git", "-C", repo_path, "add", "."], check=True)
        subprocess.run(["git", "-C", repo_path, "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "-C", repo_path, "push"], check=True)

        messagebox.showinfo("Success","Changes pushed to Github successfully")
    except subprocess.CalledProcessError:
        messagebox.showerror("error", "An error occurred while executing git commands.")


#data
connect=sqlite3.connect('modifications.db')
cursor=connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS modifs (
                path text 
               )''')

connect.commit()


home_frame = ctk.CTkFrame(app)
home_frame.pack(side='left',fill="both",expand=True)

folder_entry = ctk.CTkEntry(home_frame, width=300 ,height=33,placeholder_text="folder path")
folder_entry.pack(pady=50,fill="y")

folder_button = ctk.CTkButton(home_frame, text="📂", width=30,height=27, command=select_folder)
folder_button.place(x=367,y=53)

commit_entry = ctk.CTkEntry(home_frame,width=300,height=33,placeholder_text="your commit")
commit_entry.pack(pady=0)

push_button = ctk.CTkButton(home_frame, text="Push to GitHub", command=push_to_github,fg_color="green")
push_button.pack(pady=50)

reload_data()


app.mainloop()
