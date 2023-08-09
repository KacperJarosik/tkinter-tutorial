from tkinter import *
from PIL import ImageTk, Image


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


if __name__ == '__main__':
    root = Tk()
    root.title("frames")
    root.iconbitmap("tk8_icon.ico")

    r = IntVar()
    r.set(2)
    MODES = [
        ("Pepperoni","Pepperoni"),
        ("Cheese", "Cheese"),
        ("Mushroom", "Mushroom"),
        ("Onion", "Onion")
    ]
    pizza = StringVar()
    pizza.set("Pepperoni")
    for text, mode in MODES:
        Radiobutton(root,text=text, variable=pizza, value=mode).pack(anchor=W)
    # Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
    # Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

    # myLabel = Label(root, text=r.get())
    # myLabel.pack()

    myButton = Button(root, text="show status", command=lambda: clicked(pizza.get()))
    myButton.pack()

    root.mainloop()
