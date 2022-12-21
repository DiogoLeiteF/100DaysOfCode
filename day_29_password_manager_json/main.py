from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for x in range(randint(8, 10))]
    password_symbols = [choice(symbols) for x in range(randint(2, 4))]
    password_numbers = [choice(numbers) for x in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    pass_input.delete(0, END)
    pass_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_input.get()
    email_user = email_user_input.get()
    password = pass_input.get()
    new_data = {
        website: {
            "email": email_user,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email_user) == 0:
        messagebox.showinfo(title="ERROR", message="Don't leave any field empty!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # update old data with new data
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                # writing new data to file
                json.dump(data, data_file, indent=4)
        finally:
            web_input.delete(0, "end")
            pass_input.delete(0, "end")
            web_input.focus()


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website = web_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"user/email:  {email}\nPassword:  {password}")
        else:
            messagebox.showinfo(title=website, message="No Details for this website")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
web_input = Entry(width=32)
web_input.grid(row=1, column=1)
web_input.focus()
email_user_input = Entry(width=58)
email_user_input.grid(row=2, column=1, columnspan=2)
email_user_input.insert(0, "dummypc@gmail.com")
pass_input = Entry(width=32)
pass_input.grid(row=3, column=1)

# Buttons
generate_button = Button(text="Generate Password", width=20, command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=50, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=20, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
