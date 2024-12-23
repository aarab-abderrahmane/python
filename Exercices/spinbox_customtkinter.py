import customtkinter as ctk

class CTkSpinbox(ctk.CTkFrame):
    def __init__(self, master=None, width=120, height=32, step_size=1, from_=0, to=100, **kwargs):
        super().__init__(master, width=width, height=height, **kwargs)

        self.from_ = from_
        self.to = to
        self.step_size = step_size
        self.value = self.from_

        # Entry Widget (Read-Only)
        self.entry = ctk.CTkEntry(self, width=width - 60, state="disabled")
        self.entry.insert(0, str(self.value))  # Set initial value
        self.entry.grid(row=0, column=0, padx=5, pady=5)

        # Up Button
        self.button_up = ctk.CTkButton(
            self, text="▲", width=30, command=self.increase_value
        )
        self.button_up.grid(row=0, column=1, padx=2)

        # Down Button
        self.button_down = ctk.CTkButton(
            self, text="▼", width=30, command=self.decrease_value
        )
        self.button_down.grid(row=0, column=2, padx=2)

    def increase_value(self):
        if self.value + self.step_size <= self.to:
            self.value += self.step_size
            self.update_entry()

    def decrease_value(self):
        if self.value - self.step_size >= self.from_:
            self.value -= self.step_size
            self.update_entry()

    def update_entry(self):
        self.entry.configure(state="normal")  # Temporarily enable editing
        self.entry.delete(0, "end")
        self.entry.insert(0, str(self.value))
        self.entry.configure(state="disabled")  # Disable editing again

    def get(self):
        return self.value

    def set(self, value):
        if self.from_ <= value <= self.to:
            self.value = value
            self.update_entry()
