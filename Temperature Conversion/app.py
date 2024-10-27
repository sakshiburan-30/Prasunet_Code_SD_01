import tkinter as tk
from tkinter import messagebox

def convert_temperature(value, unit):
    """Convert temperature between Celsius, Fahrenheit, and Kelvin."""
    if unit == "C":
        fahrenheit = (value * 9/5) + 32
        kelvin = value + 273.15
        return fahrenheit, kelvin
    elif unit == "F":
        celsius = (value - 32) * 5/9
        kelvin = celsius + 273.15
        return celsius, kelvin
    elif unit == "K":
        celsius = value - 273.15
        fahrenheit = (celsius * 9/5) + 32
        return celsius, fahrenheit
    else:
        return None

def convert():
    try:
        temp_value = float(entry_value.get())
        temp_unit = entry_unit.get().strip().upper()
        converted_values = convert_temperature(temp_value, temp_unit)

        if converted_values is not None:
            if temp_unit == "C":
                result = f"{temp_value}°C = {converted_values[0]:.2f}°F, {converted_values[1]:.2f}K"
            elif temp_unit == "F":
                result = f"{temp_value}°F = {converted_values[0]:.2f}°C, {converted_values[1]:.2f}K"
            elif temp_unit == "K":
                result = f"{temp_value}K = {converted_values[0]:.2f}°C, {converted_values[1]:.2f}°F"
            else:
                raise ValueError("Invalid unit")
            messagebox.showinfo("Conversion Result", result)
        else:
            messagebox.showerror("Error", "Invalid unit. Please enter C, F, or K.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the temperature value.")

# Create the main window
root = tk.Tk()
root.title("Temperature Conversion App")
root.geometry("400x300")  # Set a larger window size

# Create and place labels, entries, and buttons
label_value = tk.Label(root, text="Enter temperature value:", font=("Arial", 14))
label_value.pack(pady=10)

entry_value = tk.Entry(root, font=("Arial", 14), width=20)
entry_value.pack(pady=10)

label_unit = tk.Label(root, text="Enter unit (C, F, K):", font=("Arial", 14))
label_unit.pack(pady=10)

entry_unit = tk.Entry(root, font=("Arial", 14), width=20)
entry_unit.pack(pady=10)

convert_button = tk.Button(root, text="Convert", command=convert, font=("Arial", 14), width=15)
convert_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
