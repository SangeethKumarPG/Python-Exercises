from tkinter import Tk, Button,Entry,Canvas, PhotoImage, Label, END, messagebox
# from tkinter import *
import random
#for copying text to clipboard
import pyperclip
#for json data 
import json
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

#----------------------------- FIND USER -----------------------------------#
def find_user():
    website_name = website_url_entry.get().lower()
    try:
        with open("Tkinter/password_manager_with_json/data.json", "r") as file:
            json_data_dump = json.load(file)
        case_insensitive_dict = {key.lower():value for (key,value) in json_data_dump.items()}
        if case_insensitive_dict.get(website_name) != None:
            website_user_data = case_insensitive_dict.get(website_name)
            registered_email = website_user_data.get("email")
            registered_password = website_user_data.get("password")
            messagebox.showinfo(title="Details", message=f"user name : {registered_email}\npassword={registered_password}")
        else:
            messagebox.showinfo(title="Website not found", message="The provided website name is not found in the data")
    except FileNotFoundError:
        messagebox.showinfo(title="No data file found", message="No data file is found for the given user name")
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title="No data found in the file", message="No data is found in the data file")
    finally:
        website_url_entry.delete(0,END)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_url_entry.get()
    user_name = username_entry.get()
    user_password = password_entry.get()
    website_name_ok, password_ok = True, True
    data_dict = {
        website_name : {
        "email" : user_name,
         "password" : user_password
        }
    }
    text = f"{website_name}     |        {user_name}        |       {user_password}"
    if len(website_name) <= 0:
        messagebox.showinfo(message="Please fill website name")
        website_name_ok = False
    if len(user_password) <= 0:
        messagebox.showinfo(message="Please fill the password field")
        password_ok = False
    if password_ok and website_name_ok:
        is_ok = True
    if is_ok:
        json_data = dict()
        #Loading and updating data
        try:
            with open("Tkinter/password_manager_with_json/data.json", "r") as file:
                json_data = json.load(file)
                json_data.update(data_dict)
        except FileNotFoundError:
            json_data = data_dict
        except json.decoder.JSONDecodeError:
            json_data = data_dict
        finally:
            with open("Tkinter/password_manager_with_json/data.json", "w") as file:   
                json.dump(json_data, file, indent=4)
                print(text)
            # print(f"{website_name} | {user_name} | {user_password}")
            website_url_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, background="white")

logo = PhotoImage(file="Tkinter/password_manager_with_json/logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0, background="white")
canvas.create_image(130,100,image = logo)
canvas.grid(row=0, column=1)



website_label = Label(text="Website:", background="white", fg="black", padx=5, pady=2)
website_label.grid(row=1, column=0, padx=2, pady=4)

website_url_entry = Entry(width=21,background="white", fg="black", highlightthickness=0, insertbackground="black")
website_url_entry.grid(row=1, column=1, padx=2, pady=4)
website_url_entry.focus_set()

search_button = Button(text="Search", width=15, padx=2, pady=2, bd=0, highlightthickness=0, command=find_user)
search_button.grid(row=1, column=2, padx=2, pady=4)

username_label = Label(text="Email/User name: ", background="white", fg="black", padx=5, pady=2)
username_label.grid(row=2, column=0, padx=2, pady=4)

username_entry = Entry(width=40,background="white", fg="black", highlightthickness=0, insertbackground="black")
username_entry.grid(row=2, column=1, columnspan=2, padx=2, pady=4)
username_entry.insert(0,"sangeeth695")

password_label= Label(text="Password: ", background="white", fg="black", padx=5, pady=2)
password_label.grid(row=3, column=0, padx=2, pady=4)

password_entry = Entry(width=21, background="white", fg="black", highlightthickness=0, insertbackground="black")
password_entry.grid(row=3, column=1, padx=2, pady=4)

generate_password_button = Button(text="Generate Password", padx=2, pady=2 , highlightthickness=0, bd=0, width=15, command=generate_password)
generate_password_button.grid(row=3, column=2, padx=2, pady=4)

add_button = Button(text="Add", width=38, padx=2, pady=2, highlightthickness=0, bd=0, command=save)
add_button.grid(row=4, column=1, columnspan=2, padx=2, pady=4)



window.mainloop()