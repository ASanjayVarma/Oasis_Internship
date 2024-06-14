import tkinter as tk
from tkinter import messagebox
import mysql.connector
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Connect to MySQL database
def create_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="bmicalcuser",
            password="password",
            database="bmi_calculator"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Connection Error", f"Error: {err}")
        return None

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def save_bmi_data(name, weight, height, bmi, category):
    conn = create_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO bmi_data (name, weight, height, bmi, category) VALUES (%s, %s, %s, %s, %s)", 
                       (name, weight, height, bmi, category))
        conn.commit()
        conn.close()

def convert_height_to_meters(feet, inches):
    return feet * 0.3048 + inches * 0.0254

def calculate_and_display_bmi():
    try:
        name = name_entry.get()
        weight = float(weight_entry.get())
        feet = float(feet_entry.get())
        inches = float(inches_entry.get())

        if weight <= 0 or feet < 0 or inches < 0:
            messagebox.showerror("Input Error", "Weight and height must be positive values.")
            return

        height_meters = convert_height_to_meters(feet, inches)
        bmi = calculate_bmi(weight, height_meters)
        category = categorize_bmi(bmi)

        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")

        save_bmi_data(name, weight, height_meters, bmi, category)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for weight and height.")

def view_history():
    conn = create_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bmi_data")
        rows = cursor.fetchall()
        conn.close()
        
        if not rows:
            messagebox.showinfo("History", "No history available.")
            return

        history_window = tk.Toplevel(root)
        history_window.title("BMI History")

        history_text = tk.Text(history_window, width=60, height=20)
        history_text.pack()

        for row in rows:
            history_text.insert(tk.END, f"Name: {row[1]}, Weight: {row[2]} kg, Height: {row[3]:.2f} m, BMI: {row[4]:.2f}, Category: {row[5]}, Date: {row[6]}\n")

def plot_trends():
    conn = create_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, bmi FROM bmi_data")
        rows = cursor.fetchall()
        conn.close()
        
        if not rows:
            messagebox.showinfo("Trends", "No data available to plot.")
            return
        
        names = [row[0] for row in rows]
        bmis = [row[1] for row in rows]

        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(names, bmis, marker='o')
        ax.set_title("BMI Trends")
        ax.set_xlabel("Names")
        ax.set_ylabel("BMI")

        trends_window = tk.Toplevel(root)
        trends_window.title("BMI Trends")

        canvas = FigureCanvasTkAgg(fig, master=trends_window)
        canvas.draw()
        canvas.get_tk_widget().pack()

def clear_history():
    response = messagebox.askyesno("Clear History", "Are you sure you want to clear all history?")
    if response:
        conn = create_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("TRUNCATE TABLE bmi_data")
            conn.commit()
            conn.close()
            messagebox.showinfo("History Cleared", "All history has been cleared.")

# Initialize Tkinter
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x550")

# Name
tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

# Weight
tk.Label(root, text="Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(root, width=15)
weight_entry.pack(pady=5)

# Height
tk.Label(root, text="Height:").pack(pady=5)
height_frame = tk.Frame(root)
height_frame.pack(pady=5)
tk.Label(height_frame, text="Feet:").grid(row=0, column=0, padx=5)
feet_entry = tk.Entry(height_frame, width=5)
feet_entry.grid(row=0, column=1, padx=5)
tk.Label(height_frame, text="Inches:").grid(row=0, column=2, padx=5)
inches_entry = tk.Entry(height_frame, width=5)
inches_entry.grid(row=0, column=3, padx=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_and_display_bmi)
calculate_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# View history button
history_button = tk.Button(root, text="View History", command=view_history)
history_button.pack(pady=10)

# Plot trends button
trends_button = tk.Button(root, text="Plot Trends", command=plot_trends)
trends_button.pack(pady=10)

# Clear history button
clear_history_button = tk.Button(root, text="Clear History", command=clear_history)
clear_history_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
