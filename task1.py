## GUI BASED TO DO LIST 
import tkinter as tk ## using the python library  tkinter
from tkinter import messagebox

class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.tasks = []

        self.task_entry = tk.Entry(self.master, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(self.master, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.complete_button = tk.Button(self.master, text="Mark as Completed", command=self.mark_as_completed)
        self.complete_button.grid(row=2, column=0, padx=10, pady=10)

        self.remove_button = tk.Button(self.master, text="Remove Completed", command=self.remove_completed)
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
