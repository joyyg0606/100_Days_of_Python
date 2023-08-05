from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_data = web_entry.get()
    email_data = email_entry.get()
    pass_data = pass_entry.get()
    if len(web_data) == 0 or len(pass_data) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=web_data, message=f"These are the details entered: \nEmail: {email_data} \nPassword: {pass_data}\nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file: 
                data_file.write(f"Website: {web_data} | Email: {email_data} | Password: {pass_data}\n")
                web_entry.delete(0, END)
                pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='Password Manager GUI App/logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

#Labels
web_label = Label(text='Website:')
web_label.grid(row=1, column=0)

email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)

pass_label = Label(text='Password:')
pass_label.grid(row=3, column=0)

#Entries
web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'example@gmail.com')

pass_entry = Entry(width=35)
pass_entry.grid(row=3, column=1)

#Buttons
gen_pass_button = Button(text='Generate Password', command=generate_pass)
gen_pass_button.grid(row=3, column=3)

add_button = Button(text='Add', width=25, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()