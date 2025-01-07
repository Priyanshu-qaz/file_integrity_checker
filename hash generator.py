import tkinter as tk
from tkinter import messagebox
import hashlib

# Function to generate hash
def generate_hash():
    input_text = input_entry.get()
    selected_algorithm = algorithm_var.get()

    if not input_text:
        messagebox.showwarning("Input Error", "Please enter a string to generate hash.")
        return

    if selected_algorithm == "MD5":
        hash_result = hashlib.md5(input_text.encode()).hexdigest()
    elif selected_algorithm == "SHA-1":
        hash_result = hashlib.sha1(input_text.encode()).hexdigest()
    elif selected_algorithm == "SHA-256":
        hash_result = hashlib.sha256(input_text.encode()).hexdigest()
    else:
        messagebox.showerror("Algorithm Error", "Unsupported algorithm selected.")
        return

    result_label.config(text=f"Hash: {hash_result}", fg="blue")

root = tk.Tk()
root.title("Hash Generator")  
root.configure(bg='#f0f0f0') 


tk.Label(root, text="Select Algorithm:", bg='#f0f0f0').pack(pady=5)
algorithm_var = tk.StringVar(root)
algorithm_var.set("MD5")  # Default value
algorithms = ["MD5", "SHA-1", "SHA-256"]
tk.OptionMenu(root, algorithm_var, *algorithms).pack(pady=5)

# Input field
tk.Label(root, text="Enter String:", bg='#f0f0f0').pack(pady=5)
input_entry = tk.Entry(root, width=50)
input_entry.pack(pady=5)

# Generate hash button
tk.Button(root, text="Generate Hash", command=generate_hash, bg='#007bff', fg='white').pack(pady=10)

# Label to display result
result_label = tk.Label(root, text="", wraplength=400, bg='#f0f0f0')
result_label.pack(pady=10)

root.mainloop()
