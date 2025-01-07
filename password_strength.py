import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength():
    password = password_entry.get()

    # Criteria checks
    length_criteria = len(password) >= 8
    lowercase_criteria = any(char.islower() for char in password)
    uppercase_criteria = any(char.isupper() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_criteria = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    # Calculate strength
    strength = 0
    if length_criteria:
        strength += 1
    if lowercase_criteria:
        strength += 1
    if uppercase_criteria:
        strength += 1
    if digit_criteria:
        strength += 1
    if special_criteria:
        strength += 1

    # Display strength
    if strength == 5:
        result_label.config(text="Password Strength: Very Strong", fg="green")
    elif strength >= 4:
        result_label.config(text="Password Strength: Strong", fg="blue")
    elif strength == 3:
        result_label.config(text="Password Strength: Moderate", fg="orange")
    else:
        result_label.config(text="Password Strength: Weak", fg="red")

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x300")
root.configure(bg="#f0f8ff")

# Widgets
header_label = tk.Label(root, text="🔒 Password Strength Checker", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333366")
header_label.pack(pady=10)

instruction_label = tk.Label(root, text="Enter your password to check its strength:", font=("Arial", 12), bg="#f0f8ff", fg="#333366")
instruction_label.pack(pady=5)

password_entry = tk.Entry(root, width=30, show="*", font=("Arial", 14), bd=2, relief="groove")
password_entry.pack(pady=10)

check_button = tk.Button(root, text="Check Strength", command=check_password_strength, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", activebackground="#45a049", relief="raised", bd=3)
check_button.pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f0f8ff")
result_label.pack(pady=10)

footer_label = tk.Label(root, text="Crafted with ❤️ using Python & Tkinter", font=("Arial", 10, "italic"), bg="#f0f8ff", fg="#666666")
footer_label.pack(side="bottom", pady=10)

footer_label = tk.Label(root, text="Priyanshu Kumar Singh", font=("Arial", 10, "italic"), bg="#f0f8ff", fg="#666666")
footer_label.pack(side="bottom", pady=10)

# Run the application
root.mainloop()
