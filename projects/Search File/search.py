import customtkinter as ctk
import os


def search_file():
    file_name=entry_name.get()
    matching_files=[]
    
    directories_to_search=["C:\\Users\\group2"]
    for dir in directories_to_search: 
        for root , dirs,files in os.walk(dir):
            for file in files : 
                if file == file_name : 
                    matching_files.append(os.path.join(root,file))

    if matching_files : 
        # entry_result.delete("1.0","end")
        # entry_result.insert("1.0","\n".join(matching_files))
        # txt.set('\n'.join(matching_files))
        for item in matching_files: 
            txt=ctk.StringVar()
            txt.set(item)
            ctk.CTkEntry(app,textvariable=txt,width=400).pack(pady=10)


def write_text(text,index=0):
    if index <len(text):
        current_text=text[:index+1]
        label_title.configure(text=current_text)
        app.after(160,write_text,text,index+1)


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app=ctk.CTk()
app.geometry("600x400")
app.title("Search")


label_title=ctk.CTkLabel(app,text="",font=("Arial",20))
label_title.pack(pady=40)
write_text("type file name")


entry_name=ctk.CTkEntry(app,placeholder_text="     type file name here",height=40,width=250,font=("Arial",20))
entry_name.pack(pady=10)

button_search=ctk.CTkButton(app,text="Search",command=lambda : search_file())
button_search.pack(pady=10)


# txt=ctk.StringVar()
# txt.set("no result")


# entry_result=ctk.CTkEntry(app,textvariable=txt,state="normal",text_color="red")
# entry_result.pack(pady=40)






app.mainloop()