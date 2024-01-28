import tkinter as tk
from tkinter import messagebox


def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    contacts.append({"name": name, "phone": phone})
    update_list()


def update_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, contact["name"] + " - " + contact["phone"])


def delete_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to delete this contact?")
        if confirmed:
            contacts.pop(selected_index[0])
            update_list()


def edit_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        selected_contact = contacts[selected_index[0]]
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        name_entry.insert(tk.END, selected_contact["name"])
        phone_entry.insert(tk.END, selected_contact["phone"])


def save_contacts():
    try:
        with open("contacts.txt", "w") as file:
            for contact in contacts:
                file.write(contact["name"] + "," + contact["phone"] + "\n")
        messagebox.showinfo("Success", "Contacts saved successfully.")
    except:
        messagebox.showerror("Error", "Failed to save contacts.")


def import_contacts():
    try:
        with open("contacts.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                contact_data = line.strip().split(",")
                name = contact_data[0]
                phone = contact_data[1]
                contacts.append({"name": name, "phone": phone})
            update_list()
        messagebox.showinfo("Success", "Contacts imported successfully.")
    except:
        messagebox.showerror("Error", "Failed to import contacts.")


def search_contacts():
    keyword = search_entry.get()
    if keyword:
        search_results = [contact for contact in contacts if keyword.lower() in contact["name"].lower()]
        contact_list.delete(0, tk.END)
        for contact in search_results:
            contact_list.insert(tk.END, contact["name"] + " - " + contact["phone"])
    else:
        update_list()


def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)


contacts = []

root = tk.Tk()

name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

phone_label = tk.Label(root, text="Phone:")
phone_label.grid(row=1, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

add_button = tk.Button(root, text="Add", command=add_contact)
add_button.grid(row=2, column=0, pady=5)

edit_button = tk.Button(root, text="Edit", command=edit_contact)
edit_button.grid(row=2, column=1, pady=5)

delete_button = tk.Button(root, text="Delete", command=delete_contact)
delete_button.grid(row=2, column=2, pady=5)

save_button = tk.Button(root, text="Save", command=save_contacts)
save_button.grid(row=2, column=3, pady=5)

import_button = tk.Button(root, text="Import", command=import_contacts)
import_button.grid(row=2, column=4, pady=5)

search_label = tk.Label(root, text="Search:")
search_label.grid(row=3, column=0)
search_entry = tk.Entry(root)
search_entry.grid(row=3, column=1)
search_button = tk.Button(root, text="Search", command=search_contacts)
search_button.grid(row=3, column=2)

contact_list = tk.Listbox(root)
contact_list.grid(row=4, columnspan=5, padx=5, pady=5, sticky="nsew")

clear_button = tk.Button(root, text="Clear Fields", command=clear_fields)
clear_button.grid(row=5, column=0, pady=5)

root.mainloop()
