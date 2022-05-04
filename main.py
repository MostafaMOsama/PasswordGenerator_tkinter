from tkinter import *
from random import random, choice, randint, shuffle
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_genertor():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    # nr_letter = random.randint(8, 10)
    # nr_number = random.randint(2, 4)
    # nr_symbols = random.randint(2, 4)
    web_password.delete(0, END)

    password_letter = [choice(letters)
                       for _ in range(randint(8, 10))]
    password_number = [choice(numbers)
                       for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols)
                        for _ in range(randint(2, 4))]

    password_list = password_letter + password_number + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    web_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = web_input.get()
    email = web_email.get()
    password = web_password.get()
    # anther soulotion

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(
            title="Empty", message="Plase Dont leave Feild Empty")

    else:

        is_ok = messagebox.askokcancel(
            title=f"{website}", message=f"these are the details entered: \n website : {website}  \n Email : {email} \n Password : {password}")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f" {website} | {email} | {password} \n")
                web_input.delete(0, END)
                web_password.delete(0, END)
    # if website == "":
    #     messagebox.showwarning(
    #         title="Empty", message="the Website input is Reqaurid")
    # elif password == "":
    #     messagebox.showwarning(
    #         title="Empty", message="the Password input is Reqaurid")

    # else:
    #     with open("data.txt", "a") as data_file:
    #         data_file.write(f" {website} | {email} | {password} \n")
    #         web_input.delete(0, END)
    #         web_password.delete(0, END)
    #         messagebox.askokcancel(
    #             title=f"{website}", message=f"these are the details entered: \n website : {website}  \n Email : {email} \n Password : {password}")


# ---------------------------- UI SETUP ------------------------------- #
window = Canvas(width=200, height=200, bg="white")
image_photo = PhotoImage(file="/Users/mostafa/web/day 25_30/day29/logo.png")
window.create_image(100, 100, image=image_photo)
window.grid(row=0, column=1, padx=20)

# Handle Lable
web_lable = Label(text="Website")
web_lable.grid(row=1, column=0)
email_lable = Label(text="Email/UserName")
email_lable.grid(row=2, column=0)
passwword_lable = Label(text="Password")
passwword_lable.grid(row=3, column=0)

# Handle Input

web_input = Entry(width=35)
web_input.grid(row=1, column=1, columnspan=2)
web_input.focus()
web_email = Entry(width=35)
web_email.grid(row=2, column=1, columnspan=2)
web_email.insert(0, "Mostafa.jr.97@gmail.com")
web_email.config(state="disabled")


web_password = Entry(width=21)
web_password.grid(row=3, column=1, padx=(25, 0))

# Button
generator_password = Button(
    text="Genertor-Password", command=password_genertor)
generator_password.grid(row=3, column=2)
add = Button(text="Add", width=35, command=save)
add.grid(row=4, column=1, columnspan=2, )

mainloop()
