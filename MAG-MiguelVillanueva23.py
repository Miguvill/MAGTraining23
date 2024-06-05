import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        returned_amount = float(returned_amount_entry.get())
        invested_amount = float(invested_amount_entry.get())
        
        gain = returned_amount - invested_amount
        roi = ((returned_amount - invested_amount) / invested_amount) * 100
        
        gain_label.config(text=f"Gain: {gain:.2f}")
        roi_label.config(text=f"ROI: {roi:.2f}%")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for both fields")

# Create the main window
root = tk.Tk()
root.title("ROI Calculator")

# Create and place labels and entries
tk.Label(root, text="Returned Amount:").grid(row=0, column=0, padx=10, pady=10)
returned_amount_entry = tk.Entry(root)
returned_amount_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Invested Amount:").grid(row=1, column=0, padx=10, pady=10)
invested_amount_entry = tk.Entry(root)
invested_amount_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Create and place labels for displaying results
gain_label = tk.Label(root, text="Gain: ")
gain_label.grid(row=3, column=0, columnspan=2, pady=5)

roi_label = tk.Label(root, text="ROI: ")
roi_label.grid(row=4, column=0, columnspan=2, pady=5)

# Run the application
root.mainloop()

