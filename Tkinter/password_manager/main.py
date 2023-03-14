from tkinter import Tk, Button,Entry,Canvas, PhotoImage, Label, END, messagebox
# from tkinter import *
import os.path
import random
#for copying text to clipboard
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    random.shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #   password += char

    # print(f"Your password is: {password}")

    #copying password to clipboard
    pyperclip.copy(password)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_url_entry.get()
    user_name = username_entry.get()
    user_password = password_entry.get()
    website_name_ok, password_ok = True, True
    text = f"{website_name}     |        {user_name}        |       {user_password}"
    if len(website_name) <= 0:
        messagebox.showinfo(message="Please fill website name")
        website_name_ok = False
    if len(user_password) <= 0:
        messagebox.showinfo(message="Please fill the password field")
        password_ok = False
    if password_ok and website_name_ok:
        is_ok = messagebox.askokcancel(title=website_name, message=f"Username : {user_name}\n Password : {user_password} \n for {website_name} \n click ok to save")
    if is_ok:
        if os.path.isfile("Tkinter/password_manager/data.txt") == False:
            with open("Tkinter/password_manager/data.txt", "w") as file:
                file.write(text)
                print(text)
        else:
            with open("Tkinter/password_manager/data.txt", "a") as file:
                file.write("\n"+text)
                print(text)
        # print(f"{website_name} | {user_name} | {user_password}")
        website_url_entry.delete(0,END)
        password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, background="white")

logo = PhotoImage(file="Tkinter/password_manager/logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0, background="white")
canvas.create_image(100,100,image = logo)
canvas.grid(row=0, column=1)



website_label = Label(text="Website:", background="white", fg="black", padx=5, pady=2)
website_label.grid(row=1, column=0)

website_url_entry = Entry(width=35,background="white", fg="black", highlightthickness=0, insertbackground="black")
website_url_entry.grid(row=1, column=1, columnspan=2)
website_url_entry.focus_set()

username_label = Label(text="Email/User name: ", background="white", fg="black", padx=5, pady=2)
username_label.grid(row=2, column=0)

username_entry = Entry(width=35,background="white", fg="black", highlightthickness=0, insertbackground="black")
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0,"sangeeth695")

password_label= Label(text="Password: ", background="white", fg="black", padx=5, pady=2)
password_label.grid(row=3, column=0)

password_entry = Entry(width=21, background="white", fg="black", highlightthickness=0, insertbackground="black")
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", padx=1, pady=1 , highlightthickness=0, bd=0, width=13, font=("Arial",12,'normal'), command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=31, padx=5, pady=5, highlightthickness=0, bd=0, command=save)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()