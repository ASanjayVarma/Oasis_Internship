import random
import string
import tkinter as tk
from tkinter import messagebox, ttk
import pyperclip

def generate_password(length, use_letters, use_uppercase, use_numbers, use_symbols, exclude_chars):
    characters = (
        (string.ascii_lowercase if use_letters else '') +
        (string.ascii_uppercase if use_uppercase else '') +
        (string.digits if use_numbers else '') +
        (string.punctuation if use_symbols else '')
    )
    
    characters = ''.join([c for c in characters if c not in exclude_chars])
    
    if not characters:
        messagebox.showerror("Error", "No characters available for password generation!")
        return ''
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    if (use_letters and not any(c in string.ascii_lowercase for c in password)) or \
       (use_uppercase and not any(c in string.ascii_uppercase for c in password)) or \
       (use_numbers and not any(c in string.digits for c in password)) or \
       (use_symbols and not any(c in string.punctuation for c in password)):
        return generate_password(length, use_letters, use_uppercase, use_numbers, use_symbols, exclude_chars)
    
    return password

def copy_to_clipboard(password):
    pyperclip.copy(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x400")

length_label = ttk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)
length_var = tk.IntVar(value=12)
length_entry = ttk.Entry(root, textvariable=length_var, width=5)
length_entry.grid(row=0, column=1, padx=10, pady=10)

letters_var = tk.BooleanVar(value=True)
ttk.Checkbutton(root, text="Include Lowercase Letters", variable=letters_var).grid(row=1, column=0, padx=10, pady=5)

uppercase_var = tk.BooleanVar(value=True)
ttk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var).grid(row=2, column=0, padx=10, pady=5)

numbers_var = tk.BooleanVar(value=True)
ttk.Checkbutton(root, text="Include Numbers", variable=numbers_var).grid(row=3, column=0, padx=10, pady=5)

symbols_var = tk.BooleanVar(value=True)
ttk.Checkbutton(root, text="Include Symbols", variable=symbols_var).grid(row=4, column=0, padx=10, pady=5)

exclude_label = ttk.Label(root, text="Exclude Characters:")
exclude_label.grid(row=5, column=0, padx=10, pady=10)
exclude_var = tk.StringVar()
ttk.Entry(root, textvariable=exclude_var, width=20).grid(row=5, column=1, padx=10, pady=10)

password_var = tk.StringVar()
ttk.Entry(root, textvariable=password_var, width=30).grid(row=6, column=0, columnspan=2, padx=10, pady=10)

def on_generate():
    password_var.set(generate_password(
        length_var.get(), letters_var.get(), uppercase_var.get(), numbers_var.get(), symbols_var.get(), exclude_var.get()
    ))

ttk.Button(root, text="Generate", command=on_generate).grid(row=7, column=0, padx=10, pady=10)

ttk.Button(root, text="Copy", command=lambda: copy_to_clipboard(password_var.get())).grid(row=7, column=1, padx=10, pady=10)

root.mainloop()
