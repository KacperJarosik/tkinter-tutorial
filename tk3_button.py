from tkinter import *


def myClick():
    myLabel = Label(root, text="Look! I Clicked a Button!")
    myLabel.pack()


if __name__ == '__main__':
    root = Tk()

    myButton0 = Button(root, text="Click Me! [0]")
    # change x size
    myButton1 = Button(root, text="Click Me! [1]", padx=50)
    # change x and y size
    myButton2 = Button(root, text="Click Me! [2]", padx=50, pady=50)
    # change disabled
    myButton3 = Button(root, text="Click Me! [3]", state=DISABLED)
    # add function
    myButton4 = Button(root, text="Click Me! [4]", command=myClick)
    # change text colour
    myButton5 = Button(root, text="Click Me! [5]", fg="red")
    # change text colour and background colour (hex colours or colours name)
    myButton6 = Button(root, text="Click Me! [6]", fg="#ffffff", bg="black")

    myButton0.pack()
    myButton1.pack()
    myButton2.pack()
    myButton3.pack()
    myButton4.pack()
    myButton5.pack()
    myButton6.pack()

    root.mainloop()
