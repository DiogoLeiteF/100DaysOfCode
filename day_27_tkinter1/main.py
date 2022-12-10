from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=100)

# pack distributes everything
# place is precise but not practical

# label
my_label = Label(text="I Am a Label", font=("Arial", 24))
my_label["text"] = "New text"
my_label.config(text="Another new text")
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=50)

# button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)


# button
button2 = Button(text="Click Me", command=button_clicked)
# button.pack()
button2.grid(column=2, row=0)

# Entry
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)

window.mainloop()
