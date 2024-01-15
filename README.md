# Password Generator

This Python script generates strong and secure passwords, checks their strength, and saves hashed passwords to a file.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Notes](#notes)


## Features

- **Password Generation:** The script generates passwords of variable length using a mix of lowercase letters, uppercase letters, digits, and special characters.

- **Password Strength Checking:** It evaluates the strength of generated passwords based on length, character types, and the presence of common dictionary words.

- **Secure Password Storage:** The script uses SHA-256 hashing and random salt generation for secure password storage. Hashed passwords are saved to a file along with the associated username and salt.

- **Copy to Clipboard:** Users can copy the generated password to the clipboard for easy use.

## Usage

1. Run the script (`main.py`) using Python 3.x.

2. Enter a name for which you want to generate a password.

3. Specify the desired length of the password.

4. Click the "Generate Password" button.

5. View the generated password and its strength on the GUI.

6. If the password is strong, the "Copy Password" button becomes enabled. Click it to copy the password to the clipboard.

7. The username, salt, and hashed password are saved to the "passwords.txt" file.

## Dependencies

- Python 3.x
- **tkinter (for GUI)**
- **pyperclip (for clipboard functionality)**

## Libraries Used

The script relies on the following Python libraries:

- **string:** Provides string constants used for password generation.
- **random:** Used for generating random passwords.
- **re:** The regular expression module, although it is not actively used in the current version of the script.
- **tkinter (as tk):** The standard GUI toolkit used for creating the graphical interface.
- **messagebox (from tkinter):** Provides pop-up message boxes for user interaction.
- **pyperclip:** Enables copying the generated password to the clipboard.
- **hashlib:** Used for hashing passwords securely.

## Notes

- Ensure that you have Python installed on your system.

- This script is a simplified example for educational purposes. In a real-world scenario, consider additional security measures, such as secure storage of hashed passwords in a database.

- Customize the dictionary word check (`is_dictionary_word` function) based on specific requirements.
