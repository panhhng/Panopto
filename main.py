# main.py
import tkinter as tk
from tkinter import messagebox
from config import userkey, password, applicationkey, servername

from auth_utils import generate_auth_code
from file_utils import browse_file, merge_files
from panopto_api import get_client, delete_users

auth_code = generate_auth_code(userkey, servername, applicationkey)
AuthenticationInfo = {
    'AuthCode': auth_code,
    'Password': password,
    'UserKey': userkey
}

client = get_client(servername)

root = tk.Tk()
root.title("Panopto Delete Users")

all_users_var = tk.StringVar()
grads_var = tk.StringVar()
merged_df = None

def on_merge_click():
    global merged_df
    try:
        merged_df, _ = merge_files(all_users_var.get(), grads_var.get())
        if merged_df is not None:
            delete_button.grid()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def on_delete_click():
    try:
        count = delete_users(client, AuthenticationInfo, merged_df)
        messagebox.showinfo("Success", f"{count} users deleted from Panopto.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

tk.Label(root, text="All Users File (with Email + UserID):").grid(row=0, column=0, sticky="w", padx=10, pady=5)
tk.Entry(root, textvariable=all_users_var, width=50).grid(row=0, column=1, padx=10)
tk.Button(root, text="Browse", command=lambda: browse_file(all_users_var)).grid(row=0, column=2, padx=10)

tk.Label(root, text="Graduates File (with Email):").grid(row=1, column=0, sticky="w", padx=10, pady=5)
tk.Entry(root, textvariable=grads_var, width=50).grid(row=1, column=1, padx=10)
tk.Button(root, text="Browse", command=lambda: browse_file(grads_var)).grid(row=1, column=2, padx=10)

tk.Button(root, text="Merge Files", command=on_merge_click).grid(row=2, column=1, pady=15)

delete_button = tk.Button(root, text="Delete Users", command=on_delete_click)
delete_button.grid(row=3, column=1, pady=10)
delete_button.grid_remove()

root.mainloop()