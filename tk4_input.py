from tkinter import *


def myClick():
    message="Hi, " + e4.get()
    myLabel = Label(root, text=message)
    myLabel.pack()


if __name__ == '__main__':
    root = Tk()

    e0 = Entry(root)
    # change width size
    e1 = Entry(root, width=50)
    # change background colour
    e2 = Entry(root, width=50, bg="black")
    # change text colour
    e3 = Entry(root, width=50, bg="black", fg="yellow")
    # change boarder width size
    e4 = Entry(root, width=50, bg="black", fg="yellow", borderwidth=5)
    #add start text to Entry
    e4.insert(0, "Enter Your Name:")

    e0.pack()
    e1.pack()
    e2.pack()
    e3.pack()
    e4.pack()

    myButton0 = Button(root, text="Enter Your Name", command=myClick)

    myButton0.pack()

    root.mainloop()
