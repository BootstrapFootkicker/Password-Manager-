from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # enumerate allows you to access index of list
    letter_list = [letter for ind, letter in enumerate(letters) if ind in range(nr_letters)]
    symbol_list = [symbol for ind, symbol in enumerate(symbols) if ind in range(nr_symbols)]
    number_list = [number for ind, number in enumerate(numbers) if ind in range(nr_numbers)]

    password_list = letter_list + symbol_list + number_list

    random.shuffle(password_list)

    password = ''.join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    web_info = website_entry.get()
    email_info = email_user_entry.get()
    password_info = password_entry.get()

    if len(web_info) == 0 or len(email_info) == 0 or len(password_info) == 0:

        messagebox.showinfo(title="", message="You've left somethings blank!", detail="No Way!")
    else:
        is_ok = messagebox.askokcancel(title=web_info,
                                       message=f'These are the details entered: \nEmail: {email_info}\nPassword: {password_info}\n'
                                               f'Is it ok to save?')
        if is_ok:
            with open('Passwords.txt', 'a') as file:
                file.write(f'{web_info} | {email_info} | {password_info}\n')
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_image = PhotoImage(file='logo.png')

canvas = Canvas(width=200, height=200)
canvas.create_image(130, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

website_entry.focus()

email_user_label = Label(text='Email/User:')
email_user_label.grid(row=2, column=0)

email_user_entry = Entry(width=35)
email_user_entry.grid(row=2, column=1, columnspan=2)
email_user_entry.insert(0, 'kyle@email.com')

password_label = Label(text='Website:')
password_label.grid(row=3, column=0)

password_entry = Entry(width=20)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", width=11, command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=32, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
