from tkinter import *

if __name__ == '__main__':
    root = Tk()

    #1st version

    # # Creating a Label Widget
    # myLabel1 = Label(root, text="Hello world!")
    # myLabel2 = Label(root, text="Hi, I'm Kacper")
    # myLabel3 = Label(root, text="               ")
    # # Showing it onto the screen
    # myLabel1.grid(row=0, column=0)
    # myLabel2.grid(row=1, column=5)
    # myLabel3.grid(row=1, column=1)

    #2nd version

    # Creating a Label Widget and showing it onto the screen
    myLabel1 = Label(root, text="Hello world!").grid(row=0, column=0)
    myLabel2 = Label(root, text="Hi, I'm Kacper").grid(row=1, column=5)
    myLabel3 = Label(root, text="               ").grid(row=1, column=1)

    root.mainloop()
