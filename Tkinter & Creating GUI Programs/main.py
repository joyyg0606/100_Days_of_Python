from tkinter import *

window = Tk()
window.title("First GUI")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="label", font=("Arial", 24, "bold"))
my_label.config(text='new text')
my_label.place(x=100, y=200)

#Button
def clicked():
    data = input.get()
    my_label.config(text=data)

button = Button(text='Click Me', command=clicked)
button.pack()

#Entry
input = Entry(width=10)
input.pack()


window.mainloop()