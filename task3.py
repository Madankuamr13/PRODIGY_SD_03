import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts():
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    
    if name and phone and email:
        contacts.append({"name": name, "phone": phone, "email": email})
        save_contacts()
        update_contact_list()
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "All fields are required.")

# Update the listbox with current contacts
def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, contact["name"])

# Clear the input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# View contact details
def view_contact(event):
    selected_index = contact_list.curselection()
    if selected_index:
        contact = contacts[selected_index[0]]
        name_entry.delete(0, tk.END)
        name_entry.insert(tk.END, contact["name"])
        phone_entry.delete(0, tk.END)
        phone_entry.insert(tk.END, contact["phone"])
        email_entry.delete(0, tk.END)
        email_entry.insert(tk.END, contact["email"])

# Edit selected contact
def edit_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        contact = contacts[selected_index[0]]
        contact["name"] = name_entry.get()
        contact["phone"] = phone_entry.get()
        contact["email"] = email_entry.get()
        save_contacts()
        update_contact_list()
        clear_entries()
    else:
        messagebox.showwarning("Selection Error", "Select a contact to edit.")

# Delete selected contact
def delete_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        del contacts[selected_index[0]]
        save_contacts()
        update_contact_list()
        clear_entries()
    else:
        messagebox.showwarning("Selection Error", "Select a contact to delete.")

# Initialize the main window
root = tk.Tk()
root.title("Contact Management System")

# Initialize contacts list
contacts = load_contacts()

# Create and place widgets
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

phone_label = tk.Label(root, text="Phone:")
phone_label.grid(row=1, column=0, padx=10, pady=5)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=2, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=5)

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=3, column=0, padx=10, pady=5)

edit_button = tk.Button(root, text="Edit Contact", command=edit_contact)
edit_button.grid(row=3, column=1, padx=10, pady=5)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=3, column=2, padx=10, pady=5)

contact_list = tk.Listbox(root)
contact_list.grid(row=0, column=3, rowspan=4, padx=10, pady=5)
contact_list.bind("<<ListboxSelect>>", view_contact)

update_contact_list()

# Run the Tkinter event loop
root.mainloop()
