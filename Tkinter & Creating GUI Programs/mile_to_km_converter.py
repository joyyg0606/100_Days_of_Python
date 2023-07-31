from tkinter import *

def clicked():
    user_input = int(input.get())
    result = round(user_input * 1.609, 3)
    result_label.config(text=result)

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

input = Entry(width=10)
input.grid(column=1, row=0)

miles_label = Label(text='Miles', font=("Arial", 9, 'normal'))
miles_label.grid(column=2, row=0)
    
equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0,row=1)

result = 0
result_label = Label(text=result)
result_label.grid(column=1,row=1)
result_label.config(padx=10)

km_label = Label(text="Km")
km_label.grid(column=2,row=1)

button = Button(text='Calculate', command=clicked)
button.grid(column=1, row=2)

window.mainloop()