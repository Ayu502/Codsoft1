import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        self.master.configure(bg='#f0f0f0')  

        
        self.background_image_pil = Image.open("D://CODE//learn python//i.jpg")
        self.background_image = ImageTk.PhotoImage(self.background_image_pil)
        self.background_label = tk.Label(self.master, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        
        self.logo_pil = Image.open("D://CODE//learn python//j.jpg")  
        self.logo_image = ImageTk.PhotoImage(self.logo_pil)
        self.logo_label = tk.Label(self.master, image=self.logo_image, bg='#f0f0f0')
        self.logo_label.grid(row=0, column=0, padx=10, pady=10)

        
        self.inner_box_frame = tk.Frame(self.master, bg='#ffffff', bd=5)
        self.inner_box_frame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.6, anchor='center')

        self.tasks = []

        
        self.task_entry = tk.Entry(self.inner_box_frame, width=40, font=('Arial', 12))
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        
        self.add_button = tk.Button(self.inner_box_frame, text="Add Task", command=self.add_task, bg='#4CAF50', fg='white', font=('Arial', 12))
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        
        self.task_listbox = tk.Listbox(self.inner_box_frame, width=50, height=10, font=('Arial', 12))
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        
        self.complete_button = tk.Button(self.inner_box_frame, text="Mark as Completed", command=self.mark_as_completed, bg='#2196F3', fg='white', font=('Arial', 12))
        self.complete_button.grid(row=2, column=0, padx=10, pady=10)

        
        self.remove_button = tk.Button(self.inner_box_frame, text="Remove Completed", command=self.remove_completed, bg='#FF5722', fg='white', font=('Arial', 12))
        self.remove_button.grid(row=2, column=1, padx=10, pady=10)

        self.update_listbox()

    def add_task(self):
        task_description = self.task_entry.get()
        if task_description:
            self.tasks.append({'description': task_description, 'completed': False})
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task description.")

    def mark_as_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]['completed'] = True
            self.update_listbox()

    def remove_completed(self):
        self.tasks = [task for task in self.tasks if not task['completed']]
        self.update_listbox()

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Done" if task['completed'] else "Not Done"
            self.task_listbox.insert(tk.END, f"{task['description']} - {status}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
