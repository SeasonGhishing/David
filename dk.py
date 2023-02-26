import tkinter as tk
from tkinter import ttk

def login():
    # code to check the entered username and password
    # against a database or file goes here
    pass

root = tk.Tk()
root.geometry("300x150")
root.title("Login")

# Set the style of the widgets
s = ttk.Style()
s.configure('.', font=('Helvetica', 12))
s.configure('TButton', font=('Helvetica', 12, 'bold'))

# Create the username label and entry
username_label = ttk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=5, pady=5, sticky='E')

username_entry = ttk.Entry(root)
username_entry.grid(row=0, column=1, padx=5, pady=5)

# Create the password label and entry
password_label = ttk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5, sticky='E')

password_entry = ttk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

# Create the login button
login_button = ttk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
