import os
import subprocess
import customtkinter as ctk
from tkinter import filedialog, messagebox
import sqlite3
import webbrowser
import sys



def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)



ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("GitHub Push GUI")
app.geometry("500x500")
app.resizable(False, False)
app.iconbitmap(resource_path("folder_scheduled_tasks_22598.ico"))



# ____________________________



file_checkboxes = {}
select_all_var = ctk.BooleanVar()

def toggle_select_all():
    state = select_all_var.get()
    for var in file_checkboxes.values():
        var.set(state)

def update_git_status():
    repo_path = folder_entry.get().strip()
    if not repo_path:
        return

    try:
        result = subprocess.run(['git', '-C', repo_path, 'status', '--porcelain'], capture_output=True, text=True, check=True)
        modifies_files = [line.strip().split(" ", 1)[-1] for line in result.stdout.splitlines() if line]

        for widget in file_list_frame.winfo_children():
            widget.destroy()

        if not modifies_files:
            label = ctk.CTkLabel(file_list_frame, text="No modified files found")
            label.pack(pady=10)
            return

        global file_checkboxes
        file_checkboxes = {}

        for file in modifies_files:
            var = ctk.BooleanVar()
            checkbox = ctk.CTkCheckBox(file_list_frame, text=file, variable=var)
            checkbox.pack(anchor="w", pady=5)
            file_checkboxes[file] = var

    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to get Git status. Make sure the repository is valid.")

def reload_data():
    cursor.execute('SELECT path FROM modifs')
    mdf = cursor.fetchall()

    if mdf:
        folder_entry.delete(0, 'end')
        folder_entry.insert(0, mdf[0][0])

        update_git_status()

def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_entry.delete(0, 'end')
        folder_entry.insert(0, str(folder))

        cursor.execute("DELETE FROM modifs")
        cursor.execute('INSERT INTO modifs (path) VALUES (?)', (folder,))
        connect.commit()

        update_git_status()

def push_to_github():
    repo_path = folder_entry.get().strip()
    commit_message = commit_entry.get().strip()

    if not repo_path:
        messagebox.showerror("error", "Please select a project folder.")
        return
    
    if not commit_message:
        messagebox.showerror("error", "Please enter a commit message.")
        return
    
    selected_files = [file for file, var in file_checkboxes.items() if var.get()]
    if not selected_files:
        messagebox.showerror("Error", "Please select at least one file to commit.")
        return

    try:
        subprocess.run(["git", "-C", repo_path, "add"] + selected_files, check=True)
        subprocess.run(["git", "-C", repo_path, "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "-C", repo_path, "push"], check=True)

        messagebox.showinfo("Success", "Changes pushed to GitHub successfully")
        
        update_git_status()

    except subprocess.CalledProcessError:
        messagebox.showerror("error", "An error occurred while executing git commands.")


def open_link(event):
    webbrowser.open("https://abderrahmane-aarab.carrd.co/")




# _________________________________________________



connect = sqlite3.connect('modifications.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS modifs (
                path text 
               )''')

connect.commit()

home_frame = ctk.CTkFrame(app)
home_frame.pack(side='left', fill="both", expand=True)

name= ctk.CTkLabel(home_frame,text="@aarab-abderrahmane",text_color="violet")
name.pack(side='top',anchor="w",padx=10)



name.configure(cursor="hand2")
name.bind("<Button-1>",open_link)

folder_entry = ctk.CTkEntry(home_frame, width=300, height=33, placeholder_text="folder path")
folder_entry.pack(padx=0,pady=50, fill="y")

folder_button = ctk.CTkButton(home_frame, text="📂", width=33, height=33, command=select_folder,fg_color="red",font=('Arial',20),hover_color="green",border_width=1,corner_radius=7)
folder_button.place(x=405, y=78)

select_all_checkbox = ctk.CTkCheckBox(home_frame, text="Select All", variable=select_all_var, command=toggle_select_all)
select_all_checkbox.place(y=120, x=200)

file_list_frame = ctk.CTkScrollableFrame(home_frame, width=350, height=150)
file_list_frame.pack(pady=2)

commit_entry = ctk.CTkEntry(home_frame, width=300, height=33, placeholder_text="your commit")
commit_entry.pack(pady=20)

push_button = ctk.CTkButton(home_frame, text="Push to GitHub", command=push_to_github, fg_color="green",corner_radius=0)
push_button.pack(anchor="s", fill="x", side="bottom")



reload_data()
app.mainloop()
