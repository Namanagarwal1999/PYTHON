from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    random.shuffle(password_list)
    password = "".join(password_list)

    entry_password.insert(END, string=password)
    pyperclip.copy(password)
    messagebox.showinfo(title="", message="Password copied to clipboard")



# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():

    website = entry_website.get()
    user = entry_user.get()
    password = entry_password.get()
    new_data = {
        website: {
            "username": user,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_user.delete(0, END)
            entry_password.delete(0, END)

# ---------------------------- SEARCH COMMAND ------------------------------- #
def search():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data file Found. ")
    else:
        if entry_website.get() in data:
            username = data[entry_website.get()]["username"]
            password = data[entry_website.get()]["password"]
            messagebox.showinfo(title=entry_website.get(), message=f"Username: {username}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No Details for {entry_website.get()} exists. ")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=40)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="../../Day 30/Password manager with search option/logo.png")
canvas.create_image(130, 100, image=logo_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:", font=("Arial", 10))
label_website.grid(column=0, row=1)
label_username = Label(text="Email/ Username:", font=("Arial", 10))
label_username.grid(column=0, row=2)
label_password = Label(text="Password:", font=("Arial", 10))
label_password.grid(column=0, row=3)

entry_website = Entry(width=30)
entry_website.grid(column=1, row=1)
entry_website.focus()
entry_user = Entry(width=50)
entry_user.grid(column=1, row=2, columnspan=2)
entry_password = Entry(width=30)
entry_password.grid(column=1, row=3)

button = Button(width=16)
button.config(text="Generate Password", command=generate_password)
button.grid(column=2, row=3)
button = Button(width=43)
button.config(text="Add", command=add)
button.grid(column=1, row=4, columnspan=2)
button = Button(width=16)
button.config(text="search", command=search)
button.grid(column=2, row=1)


window.mainloop()