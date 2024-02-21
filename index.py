import tkinter as tk
from tkinter import ttk

def convert_unit():
    length_value = float(entry_length.get())
    selection = int(dropdown.get()[0])

    if selection == 1:
        result = length_value / 30.48
        label_result.config(text=f"{length_value} cm is equal to {result:.2f} feet.")
    elif selection == 2:
        result = length_value * 12
        label_result.config(text=f"{length_value} feet is equal to {result:.2f} inches.")
    elif selection == 3:
        result = length_value / 10.764
        label_result.config(text=f"{length_value} sqft is equal to {result:.2f} sqm.")
    elif selection == 4:
        hectares = length_value / 107639.104
        acres = length_value / 43560
        label_result.config(text=f"{length_value} sqft is equal to {hectares:.2f} hectares or {acres:.2f} acres.")

root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x300")
root.configure(bg="#FFFFFF")

style = ttk.Style()
style.theme_use('clam')

label_title = ttk.Label(root, text="Unit Converter", font=("Arial", 24, "bold"), background="#FFFFFF")
label_title.pack(pady=10)

frame = ttk.Frame(root, padding=20)
frame.pack()

label_dropdown = ttk.Label(frame, text="Choose a conversion category:", font=("Arial", 14), background="#FFFFFF")
label_dropdown.grid(row=0, column=0, pady=10, padx=10, sticky="w")

unit_change = {
    1: "Centimeter to Feet",
    2: "Feet to Inches",
    3: "Square Feet to Square Meters",
    4: "Square Feet to Hectares/Acres"
}

dropdown_options = [f"{key}. {value}" for key, value in unit_change.items()]

dropdown = ttk.Combobox(frame, values=dropdown_options, state="readonly", width=30, font=("Arial", 12))
dropdown.set(dropdown_options[0])
dropdown.grid(row=0, column=1, pady=10, padx=10)

label_length = ttk.Label(frame, text="Enter a number to convert:", font=("Arial", 14), background="#FFFFFF")
label_length.grid(row=1, column=0, pady=10, padx=10, sticky="w")

entry_length = ttk.Entry(frame, font=("Arial", 14), width=10)
entry_length.grid(row=1, column=1, pady=10, padx=10)

convert_button = ttk.Button(root, text="Convert", command=convert_unit, style="Accent.TButton")
convert_button.pack(pady=15)

label_result = ttk.Label(root, text="", font=("Arial", 14), background="#FFFFFF")
label_result.pack(pady=5)

root.mainloop()
