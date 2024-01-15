import string
import random
import re
import tkinter as tk
from tkinter import messagebox
import pyperclip
import hashlib

def generate_password(length):
    p1 = string.ascii_lowercase
    p2 = string.ascii_uppercase
    p3 = string.digits
    p4 = string.punctuation

    s = list(p1) + list(p2) + list(p3) + list(p4)
    random.shuffle(s)

    return "".join(s[:length])

def generate_salt():
    # Generate a random salt
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

def hash_password(password, salt):
    # Use SHA-256 for hashing
    hash_object = hashlib.sha256()
    # Combine password and salt before hashing
    hash_object.update((password + salt).encode('utf-8'))
    return hash_object.hexdigest()

def save_to_file(username, salt, hashed_password):
    # Save the username, salt, and hashed password to a file
    with open("passwords.txt", "a") as file:
        file.write(f"{username}:{salt}:{hashed_password}\n")

def is_dictionary_word(word):
    # Implement your dictionary word check logic here
    # For simplicity, let's assume a small dictionary of common words
    dictionary = ["password", "qwerty", "12345", "letmein", "admin"]
    return word.lower() in dictionary

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."

    if not any(char.islower() for char in password) or \
       not any(char.isupper() for char in password) or \
       not any(char.isdigit() for char in password) or \
       not any(char in string.punctuation for char in password):
        return "Weak: Password should include a mix of lowercase, uppercase, digits, and special characters."

    if is_dictionary_word(password):
        return "Weak: Avoid using common dictionary words."

    return "Strong: Password meets recommended criteria."

def generate_and_display_password():
    pwd_len = int(length_entry.get())
    generated_password = generate_password(pwd_len)
    password_display.config(text=f"Your password is: {generated_password}")

    strength_result = check_password_strength(generated_password)
    strength_display.config(text=f"Password Strength: {strength_result}")

    if "Weak" in strength_result:
        messagebox.showwarning("Weak Password", "The generated password is weak. Please generate a new one.")
    else:
        # Enable the "Copy Password" button, set the password to be copied, and save to file
        global clipboard_password
        clipboard_password = generated_password
        copy_button.config(state=tk.NORMAL)
        username = username_entry.get()  # Assuming you have an entry for username
        salt = generate_salt()
        hashed_password = hash_password(generated_password, salt)
        save_to_file(username, salt, hashed_password)

def copy_password_to_clipboard():
    # Copy the password to the clipboard
    pyperclip.copy(clipboard_password)
    messagebox.showinfo("Password Copied", "The password has been copied to the clipboard.")

# GUI setup
root = tk.Tk()
root.title("Password Generator")

# Entry for name to generate password for
username_label = tk.Label(root, text="Enter a name to generate a password for:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Entry for password length
length_label = tk.Label(root, text="Enter the length of the password:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Button to generate and display password
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.pack()

# Labels to display generated password and strength
password_display = tk.Label(root, text="")
password_display.pack()

strength_display = tk.Label(root, text="")
strength_display.pack()

# Button to copy password to clipboard
copy_button = tk.Button(root, text="Copy Password", command=copy_password_to_clipboard, state=tk.DISABLED)
copy_button.pack()

# Run the GUI
root.mainloop()
