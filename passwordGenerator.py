import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        self.length_label = tk.Label(self.master, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        self.length_entry = tk.Entry(self.master)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10, sticky="W")

        self.complexity_label = tk.Label(self.master, text="Password Complexity:")
        self.complexity_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        self.complexity_combobox = ttk.Combobox(self.master, values=["Low", "Medium", "High"])
        self.complexity_combobox.current(1)  # Set default to Medium
        self.complexity_combobox.grid(row=1, column=1, padx=10, pady=10, sticky="W")

        self.generate_button = tk.Button(self.master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(self.master, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            complexity = self.complexity_combobox.get()

            if length <= 0:
                raise ValueError("Length should be a positive integer.")

            if complexity == "Low":
                characters = string.ascii_letters
            elif complexity == "Medium":
                characters = string.ascii_letters + string.digits
            elif complexity == "High":
                characters = string.ascii_letters + string.digits + string.punctuation

            generated_password = ''.join(random.choice(characters) for _ in range(length))
            self.result_label.config(text=f"Generated Password: {generated_password}")
        except ValueError as e:
            self.result_label.config(text=f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
