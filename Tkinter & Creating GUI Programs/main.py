from tkinter import *

window = Tk()
window.title("First GUI")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

#Label
my_label = Label(text="label", font=("Arial", 24, "bold"))
my_label.config(text='new text')
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Button
def clicked():
    data = input.get()
    my_label.config(text=data)

button = Button(text='Click Me', command=clicked)
button.grid(column=1, row=1)

button_2 = Button(text='Click Me')
button_2.grid(column=2, row=0)

#Entry
input = Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()