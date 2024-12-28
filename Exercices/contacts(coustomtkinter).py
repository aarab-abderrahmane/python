from customtkinter import *
import customtkinter as ck
from spinbox_customtkinter import CTkSpinbox  # Assuming this class is defined properly



# Initialize app
app = CTk()
app.geometry("900x500")
app.title("Contacts")

# Set appearance mode
ck.set_appearance_mode("System")

# Frames
right_frame = CTkFrame(app, bg_color="#d8f3dc")
left_frame = CTkFrame(app)

right_frame.pack(side="right", fill="both")
left_frame.pack(side="left", fill="both")

# __________left frame
name_label = CTkLabel(master=left_frame, text="Name", font=("Arial", 23))
name_label.grid(row=1, column=1, padx=10, pady=10)
last_name_label = CTkLabel(master=left_frame, text="Last Name", font=("Arial", 23))
last_name_label.grid(row=2, column=1, padx=10, pady=10)
country_label = CTkLabel(master=left_frame, text="Country", font=("Arial", 23))
country_label.grid(row=3, column=1, padx=10, pady=10)
phone_number_label = CTkLabel(master=left_frame, text="Phone Number", font=("Arial", 23))
phone_number_label.grid(row=4, column=1, padx=10, pady=10)
gender_label = CTkLabel(master=left_frame, text="Gender", font=("Arial", 23))
gender_label.grid(row=5, column=1, padx=10, pady=10)
children_label = CTkLabel(master=left_frame, text="Number of Children", font=("Arial", 23))
children_label.grid(row=6, column=1, padx=10, pady=10)

# Gender variable for Radio buttons
gender = StringVar()

# Entry widgets
entry_name = CTkEntry(master=left_frame, font=('Arial', 23))
entry_name.grid(row=1, column=2, padx=10, pady=10)
entry_last_name = CTkEntry(master=left_frame, font=('Arial', 23))
entry_last_name.grid(row=2, column=2, padx=10, pady=10)

# ComboBox with state "readonly" (no editing, just display selected value)
entry_country = CTkComboBox(master=left_frame, values=['USA', 'Canada', 'UK', 'India'], state="readonly")
entry_country.grid(row=3, column=2, padx=10, pady=10)

entry_phone_number = CTkEntry(master=left_frame, font=('Arial', 23))
entry_phone_number.grid(row=4, column=2, padx=10, pady=10)

# Create a frame for the Gender radio buttons to keep them together
gender_frame = CTkFrame(master=left_frame, fg_color="#2b2b2b")  # Change background color here

# Place radio buttons inside the gender_frame
CTkRadioButton(master=gender_frame, text="Male", variable=gender, value="Male").pack(side="left", padx=10)
CTkRadioButton(master=gender_frame, text="Female", variable=gender, value="Female").pack(side="left", padx=10)

# Grid the gender_frame at the correct position
gender_frame.grid(row=5, column=2, padx=10, pady=10)

# CTkSpinbox for Number of Children
entry_children = CTkSpinbox(master=left_frame, from_=0, to=10, width=200)
entry_children.grid(row=6, column=2, padx=10, pady=10)

# Start the app
app.mainloop()
