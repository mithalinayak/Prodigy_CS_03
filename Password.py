import tkinter as tk
from tkinter import messagebox
import re

def assess_password(password):
    """ Assess the strength of a password based on several criteria. """
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*()_+{}\[\]:;"\'<>,.?/\\|`~]', password))

    score = 0
    if length_criteria: score += 1
    if uppercase_criteria: score += 1
    if lowercase_criteria: score += 1
    if number_criteria: score += 1
    if special_char_criteria: score += 1

    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    else:
        return "Weak"

def check_password():
    """ Check the password strength and show feedback to the user. """
    password = password_entry.get()
    if not password:
        messagebox.showwarning("Warning", "Please enter a password.")
        return
    
    strength = assess_password(password)
    messagebox.showinfo("Password Strength", f"Your password strength is: {strength}")

# Create main window
root = tk.Tk()
root.title("Password Strength Checker")
root.configure(bg="#2c3e50")

# Style
label_style = {
    "font": ("Helvetica", 12),
    "bg": "#2c3e50",
    "fg": "#ecf0f1"
}
entry_style = {
    "font": ("Helvetica", 12),
    "width": 30
}
button_style = {
    "font": ("Helvetica", 12),
    "bg": "#3498db",
    "fg": "#ecf0f1",
    "activebackground": "#2980b9",
    "activeforeground": "#ecf0f1",
    "width": 12
}

# Create widgets
password_label = tk.Label(root, text="Enter Password:", **label_style)
password_entry = tk.Entry(root, **entry_style, show="*")
check_button = tk.Button(root, text="Check Strength", command=check_password, **button_style)

# Layout
password_label.grid(row=0, column=0, padx=10, pady=10)
password_entry.grid(row=0, column=1, padx=10, pady=10)
check_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Run main loop
root.mainloop()

