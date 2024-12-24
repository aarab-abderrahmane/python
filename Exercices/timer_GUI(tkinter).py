import tkinter as tk
from tkinter import ttk , messagebox




class TimerApp:
    def __init__(self,root):
        self.root=root
        self.root.geometry('600x200')
        self.root.title('timer')
        self.root.config(bg="white")
        self.root.resizable(False,False)

        self.minute=tk.StringVar(value="00")
        self.seconds=tk.StringVar(value="00")
        self.running=False


        # minute
        self.entry_minutes=tk.Entry(self.root,textvariable=self.minute,bg="white",fg="black",font=('Arial',50))
        self.entry_minutes.place(relheight=0.4,relwidth=0.3,x=100,y=50)

        # seconds
        self.entry_seconds=tk.Entry(self.root,textvariable=self.seconds,bg="white",fg="black",font=('Arial',50))
        self.entry_seconds.place(relheight=0.4,relwidth=0.3,x=300,y=50)

        #point
        tk.Label(self.root,text=":",font=("Arial",50),bg="white",height=2).place(x=278,y=15)


        # buttons
        self.start=ttk.Button(self.root,text="start",command=self.start_timer)
        self.start.pack(side="right",fill="y")

        self.stop=ttk.Button(self.root,text="Stop",command=self.stop_timer)
        self.stop.pack(side="left",fill="y")

    def start_timer(self):
        if not self.running : 
            try:
                mins=int(self.entry_minutes.get())
                secs=int(self.entry_seconds.get())

                self.totale_seconds=mins *60 +secs

                if self.totale_seconds <=0:
                    messagebox.showwarning('Invalid Input','Please enter a positive time value.')
                    return
                
                self.running=True
                self.update_timer()
            
            except ValueError:
                messagebox.showerror('Invalid Input','Please ennter valid numbers for minutes and seconds')

    def update_timer(self):            
        if self.running and self.totale_seconds > 0 :
            mins=self.totale_seconds // 60
            secs=self.totale_seconds % 60

            self.minute.set(f"{mins:02d}")
            self.seconds.set(f"{secs:02d}")

            self.totale_seconds -=1

            self.root.after(1000,self.update_timer)
    
        elif self.totale_seconds == 0 : 
            self.minute.set("00")
            self.seconds.set("00")
            self.running=False
            messagebox.showinfo("Time's up!","The timer has finished!")
    
    def stop_timer(self):
        self.running=False


if __name__ == '__main__':
    root=tk.Tk()
    app=TimerApp(root)
    root.mainloop()