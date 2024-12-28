from customtkinter import *
from PIL import Image
from tkinter import messagebox
import sqlite3



class reset_password:

    def __init__ (self,app,frame_1,frame_2):
        self.app=app
        self.frame_1=frame_1
        self.frame_2=frame_2

        self.frame_1.grid_forget()
        self.frame_2.grid_forget()