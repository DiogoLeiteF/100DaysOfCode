from tkinter import *


def converter():
    miles = float(entry.get())
    km = miles * 1.609
    label_result.config(text=f"{km}")


window = Tk()
window.title("Miles to Km Converter")
# window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

entry = Entry(width=7)
entry.focus()
entry.grid(column=1, row=0)


label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_result = Label(text="0")
label_result.grid(column=1, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

button = Button(text="Calculate", command=converter)
button.grid(column=1, row=2)


window.mainloop()