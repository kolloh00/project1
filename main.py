from tkinter import *

def calculate_lot_size():
    risk = float(entry_risk.get())
    pips = float(entry_pips.get())

    # Subtract 5 from pips
    pips -= 5

    # Check if pips is not zero before calculating lot size
    if pips != 0:
        lot_size = risk / pips
        result_label.config(text=f"The calculated lot size is: {lot_size}")
    else:
        result_label.config(text="Error: Division by zero!")

def clear_inputs():
    entry_risk.delete(0, END)
    entry_pips.delete(0, END)
    result_label.config(text="")

# Create the main window
root = Tk()
root.geometry("800x600")
root.resizable(False, False)
root.title("Lot Size Calculator")

# Create labels, entry widgets, and buttons
label_risk = Label(root, text="Risk amount:")
label_pips = Label(root, text="Pips:")
entry_risk = Entry(root)
entry_pips = Entry(root)
calculate_button = Button(root, text="Calculate", command=calculate_lot_size)
clear_button = Button(root, text="Clear", command=clear_inputs)
result_label = Label(root, text="")

# Place widgets in the window
label_risk.grid(row=0, column=0, padx=10, pady=10)
entry_risk.grid(row=0, column=1, padx=10, pady=10)
label_pips.grid(row=1, column=0, padx=10, pady=10)
entry_pips.grid(row=1, column=1, padx=10, pady=10)
calculate_button.grid(row=2, column=0, pady=10)
clear_button.grid(row=2, column=1, pady=10)
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
