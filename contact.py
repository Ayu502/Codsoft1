import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class ContactBookGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")

        self.contacts = []

        # Labels and Entry widgets for contact details
        self.name_label = tk.Label(self.master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(self.master, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(self.master)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label = tk.Label(self.master, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(self.master)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label = tk.Label(self.master, text="Address:")
        self.address_label.grid(row=3, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(self.master)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons for actions
        self.add_button = tk.Button(self.master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(self.master, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.search_button = tk.Button(self.master, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.update_button = tk.Button(self.master, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.delete_button = tk.Button(self.master, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=8, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {'Name': name, 'Phone': phone, 'Email': email, 'Address': address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully.")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Name and phone are required.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Information", "No contacts available.")
        else:
            contact_list = "\n".join([f"{contact['Name']} - {contact['Phone']}" for contact in self.contacts])
            messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        search_text = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if search_text:
            found_contacts = [contact for contact in self.contacts if
                              search_text.lower() in contact['Name'].lower() or
                              search_text in contact['Phone']]
            if found_contacts:
                contact_list = "\n".join([f"{contact['Name']} - {contact['Phone']}" for contact in found_contacts])
                messagebox.showinfo("Search Result", contact_list)
            else:
                messagebox.showinfo("Search Result", "No contacts found.")

    def update_contact(self):
        search_text = simpledialog.askstring("Update Contact", "Enter name or phone number:")
        if search_text:
            found_contacts = [contact for contact in self.contacts if
                              search_text.lower() in contact['Name'].lower() or
                              search_text in contact['Phone']]
            if found_contacts:
                selected_contact = found_contacts[0]
                updated_name = simpledialog.askstring("Update Contact", "Enter updated name:",
                                                      initialvalue=selected_contact['Name'])
                updated_phone = simpledialog.askstring("Update Contact", "Enter updated phone:",
                                                       initialvalue=selected_contact['Phone'])
                updated_email = simpledialog.askstring("Update Contact", "Enter updated email:",
                                                       initialvalue=selected_contact['Email'])
                updated_address = simpledialog.askstring("Update Contact", "Enter updated address:",
                                                         initialvalue=selected_contact['Address'])

                if updated_name and updated_phone:
                    selected_contact['Name'] = updated_name
                    selected_contact['Phone'] = updated_phone
                    selected_contact['Email'] = updated_email
                    selected_contact['Address'] = updated_address

                    messagebox.showinfo("Success", "Contact updated successfully.")
                else:
                    messagebox.showwarning("Warning", "Name and phone are required for update.")
            else:
                messagebox.showinfo("Information", "No contacts found.")

    def delete_contact(self):
        search_text = simpledialog.askstring("Delete Contact", "Enter name or phone number:")
        if search_text:
            found_contacts = [contact for contact in self.contacts if
                              search_text.lower() in contact['Name'].lower() or
                              search_text in contact['Phone']]
            if found_contacts:
                confirm_delete = messagebox.askyesno("Delete Contact", "Are you sure you want to delete this contact?")
                if confirm_delete:
                    self.contacts.remove(found_contacts[0])
                    messagebox.showinfo("Success", "Contact deleted successfully.")
            else:
                messagebox.showinfo("Information", "No contacts found.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookGUI(root)
    root.mainloop()
