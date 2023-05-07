from tkinter import *
from tkinter import messagebox
import random
import json

WHITE = "white"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)] + \
                    [random.choice(numbers) for _ in range(nr_symbols)] + \
                    [random.choice(symbols) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_name.delete(0, END)
    password_name.insert(0, password)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_name.get()
    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please, provide the name!")
    else:
        try:
            with open("data.json") as data_file:
                # reading the data from json file
                json_data = json.load(data_file)
                show_data = json_data[website]
        except FileNotFoundError:
            messagebox.showinfo(title="Oops", message="Database is empty")
        except KeyError:
            messagebox.showinfo(title="Oops", message="No such name found")
        else:
            email = show_data["email"]
            password = show_data["password"]
            messagebox.showinfo(title=website, message=f"These are yourr credentials: \nEmail: {email} "
                                                       f"\nPassword: {password}")




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_name.get()
    email = email_name.get()
    password = password_name.get()
    data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json") as data_file:
                # reading the data from json file
                json_data = json.load(data_file)


        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=3)
        else:
            # updating the json file
            json_data.update(data)
            with open("data.json", "w") as data_file:
                # saving data to json file
                json.dump(json_data, data_file, indent=3)
        finally:
            website_name.delete(0, END)
            website_name.focus()
            email_name.delete(0, END)
            email_name.insert(0, "aineken93@gmail.com")
            password_name.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("MyPass")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
# row number 1
canvas.grid(column=1, row=0)

# row number 2
Label(text="Website:", bg=WHITE).grid(column=0, row=1)
website_name = Entry(width=21, highlightthickness=0, bg=WHITE)
website_name.focus()
website_name.grid(column=1, row=1)
Button(text="Search", width=15, bg=WHITE, highlightthickness=0, command=find_password).grid(row=1, column=2,
                                                                                                padx=0, pady=0)

# row number 3
Label(text="Email/Username:", bg=WHITE).grid(column=0, row=2)
email_name = Entry(width=36, bg=WHITE, highlightthickness=0)
email_name.insert(0, "aineken93@gmail.com")
email_name.grid(column=1, row=2, columnspan=2)

# row number 4
Label(text="Password:", bg=WHITE).grid(column=0, row=3)
password_name = Entry(width=21, highlightthickness=0)
password_name.grid(column=1, row=3)
Button(width=15, text="Generate Password", bg=WHITE, highlightthickness=0, command=generate_password).grid(row=3,
                                                                                                           column=2,
                                                                                                           padx=0,
                                                                                                           pady=0)

# row number 5
Button(text="add", width=36, bg=WHITE, highlightthickness=0, command=save_data).grid(row=4, column=1, columnspan=2,
                                                                                     padx=0, pady=0)

# Button(window, text="Quit", command=window.destroy).grid(column=0, row=0)

window.mainloop()
