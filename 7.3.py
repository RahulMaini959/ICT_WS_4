import tkinter as tk
from tkinter import messagebox

def calculate(operation):
    try:
        # Retrieve numbers from the entry fields
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        # Perform the calculation based on the operation
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = num1 / num2

        # Update the result label
        label_result.config(text=f"Result: {result}")
    
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x250")

# Input fields
tk.Label(root, text="Enter first number:").pack(pady=5)
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

tk.Label(root, text="Enter second number:").pack(pady=5)
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

# Operation buttons
tk.Button(root, text="Add", command=lambda: calculate('add')).pack(pady=5)
tk.Button(root, text="Subtract", command=lambda: calculate('subtract')).pack(pady=5)
tk.Button(root, text="Multiply", command=lambda: calculate('multiply')).pack(pady=5)
tk.Button(root, text="Divide", command=lambda: calculate('divide')).pack(pady=5)

# Result label
label_result = tk.Label(root, text="Result: ")
label_result.pack(pady=10)

# Run the application
root.mainloop()
