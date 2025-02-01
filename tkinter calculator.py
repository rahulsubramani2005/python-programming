import tkinter as tk

# Function to update the expression in the input field
def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(key))

# Function to evaluate the expression and display the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Set up the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display the expression/result
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Buttons layout (button text, row, column)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Create buttons and add them to the grid
for (text, row, column) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=calculate)
    elif text == "C":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=clear)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=lambda key=text: press(key))
    button.grid(row=row, column=column)

# Run the Tkinter event loop
root.mainloop()


'''Key points:
Entry widget (entry) is used to display the current expression and result.
Buttons for numbers, operators, and functions are created in a grid layout.
The press() function appends the button value to the expression.
The calculate() function evaluates the expression using Python's eval() function.
clear() resets the entry field.'''
