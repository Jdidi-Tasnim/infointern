import random
import string
from tkinter import *
import pyperclip

# Initialize Window
root = Tk()
root.geometry("400x550")  # Increased height to accommodate the exclusion entry
root.title("Random Password Generator")

# StringVar to store the generated password
output_pass = StringVar()

# IntVar to store the password length
pass_len = IntVar()
pass_len.set(12)  # Default password length

# IntVar to store the password complexity level
pass_complexity = IntVar()
pass_complexity.set(1)  # Default to easy

# StringVar to store excluded characters
exclude_chars = StringVar()

# List of all possible characters
all_combi = [string.ascii_uppercase, string.digits, string.ascii_lowercase]

# -------------------  Random Password generator function
def randPassGen():
    password = ""
    complexity = pass_complexity.get()

    if complexity == 1:  # Easy
        char_types = all_combi[1:]  # Exclude punctuation for easy
    elif complexity == 2:  # Medium
        char_types = all_combi
    else:  # Difficult
        char_types = all_combi[:2]  # Use only letters and digits for difficult

    exclude_set = set(exclude_chars.get())

    for _ in range(pass_len.get()):
        char_type = random.choice(char_types)

        char = random.choice(char_type)

        # Check if the character is in the exclusion set
        while char in exclude_set:
            char = random.choice(char_type)

        password += char

    output_pass.set(password)

# ----------- Copy to clipboard function
def copyPass():
    pyperclip.copy(output_pass.get())

# -----------------------Front-end Designing (GUI)
pass_head = Label(root, text='Password Length', font='arial 12 bold').pack(pady=10)  # to generate label heading
length = Spinbox(root, from_=4, to_=32, textvariable=pass_len, width=24, font='arial 16').pack()

pass_complexity_label = Label(root, text='Password Complexity', font='arial 12 bold').pack(pady=10)
complexity_scale = Scale(root, from_=1, to=3, orient=HORIZONTAL, variable=pass_complexity,
                         label="1: Easy, 2: Medium, 3: Difficult").pack()

exclude_label = Label(root, text='Exclude Characters', font='arial 12 bold').pack(pady=10)
exclude_entry = Entry(root, textvariable=exclude_chars, font='arial 16')
exclude_entry.pack()

# Generate password button
Button(root, command=randPassGen, text="Generate Password", font="Arial 10", bg='lightblue', fg='black',
       activebackground="teal", padx=5, pady=5).pack(pady=20)

pass_label = Label(root, text='Random Generated Password', font='arial 12 bold').pack(pady="30 10")
Entry(root, textvariable=output_pass, width=24, font='arial 16').pack()

# Copy to clipboard button
Button(root, text='Copy to Clipboard', command=copyPass, font="Arial 10", bg='lightblue', fg='black',
       activebackground="teal", padx=5, pady=5).pack(pady=20)

root.mainloop()
