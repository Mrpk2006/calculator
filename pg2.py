import random
import tkinter as tk
from tkinter import messagebox

def generate_pass():
    low = "abcdefghijklmnopqrstuvwxyz"
    upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "1234567890"
    sym = "!@#$%^&*"

    all_char = low + upp + num + sym
   
    password = [
        random.choice(low),
        random.choice(upp),
        random.choice(num),
        random.choice(sym)
    ]
    
   
    password += random.sample(all_char, 12 - 4)
    random.shuffle(password)
    final_password = ''.join(password)

    pass_entry.delete(0, tk.END)
    pass_entry.insert(tk.END, final_password)

def copy_pass():
    password = pass_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Password Copied", "Password has been copied to clipboard.")
    else:
        messagebox.showwarning("No Password", "No password generated.")


root = tk.Tk()
root.title("Password Generator")

pass_label = tk.Label(root, text="Generated Password:")
pass_label.pack()

pass_entry = tk.Entry(root, width=30)
pass_entry.pack()

generate_btn = tk.Button(root, text="Generate Password", command=generate_pass)
generate_btn.pack(pady=10)

copy_btn = tk.Button(root, text="Copy Password", command=copy_pass)
copy_btn.pack(pady=10)

root.mainloop()
