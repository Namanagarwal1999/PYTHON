from tkinter import *

window = Tk()
window.title("Mile to Km Convertor")
window.minsize(width=300, height=100)
window.config(padx=50, pady=20)

entry = Entry(width=12)
entry.grid(column=1, row=0)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = Label(text="0")
label3.grid(column=1, row=1)

label4 = Label(text="Km")
label4.grid(column=2, row=1)


def action():
    question = float(entry.get())
    answer = round(question * 1.609, 2)
    label3.config(text=answer)


button = Button(text="Calculate", command=action)
button.grid(column=1, row=2)
window.mainloop()
