import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess

# Function to run Nmap scan
def run_scan():
    target = entry_target.get()
    if not target:
        messagebox.showerror("Error", "Please enter a target IP/Domain.")
        return
    
    scan_output.delete(1.0, tk.END)  # Clear previous results
    try:
        # Run the Nmap command
        scan_result = subprocess.run(
            ["nmap", "-sV", "-T4", target],
            capture_output=True,
            text=True
        )
        # Display scan results in the Text box
        scan_output.insert(tk.END, scan_result.stdout)
        save_results_to_file(scan_result.stdout)  # Save results to file
    except Exception as e:
        messagebox.showerror("Error", f"Scan Failed: {str(e)}")

# Function to save results to a text file
def save_results_to_file(output):
    try:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            with open(file_path, "w") as file:
                file.write(output)
            messagebox.showinfo("Success", f"Results saved to {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save file: {str(e)}")

# GUI Setup
root = tk.Tk()
root.title("Nmap Vulnerability Scanner")
root.geometry("700x500")

# Title Label

tk.Label(root, text="Nmap Vulnerability Scanner", font=("Helvetica", 16, "bold")).pack(pady=10)
tk.Label(root, text="PRIYANSHU KUMAR SINGH", font=("Helvetica", 12, )).pack(pady=10)

# Input Frame
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Enter Target IP/Domain:", font=("Helvetica", 12)).pack(side=tk.LEFT, padx=5)
entry_target = tk.Entry(frame, width=40, font=("Helvetica", 12))
entry_target.pack(side=tk.LEFT, padx=5)

# Run Scan Button
btn_scan = tk.Button(root, text="Run Scan", font=("Helvetica", 12), bg="green", fg="white", command=run_scan)
btn_scan.pack(pady=10)

# Output Frame
tk.Label(root, text="Scan Results:", font=("Helvetica", 12, "bold")).pack(pady=5)
scan_output = tk.Text(root, height=20, width=80, font=("Courier", 10), wrap=tk.WORD)
scan_output.pack(padx=10, pady=10)

# Run the GUI
root.mainloop()
