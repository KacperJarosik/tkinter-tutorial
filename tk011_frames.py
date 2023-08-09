from tkinter import *
from PIL import ImageTk, Image

if __name__ == '__main__':
    root = Tk()
    root.title("frames")
    root.iconbitmap("tk8_icon.ico")

    frame = LabelFrame(root, text="This is my Frame...", padx=10, pady=10)
    frame.pack(padx=100, pady=100)

    b = Button(frame, text="Don't click here")
    # b.pack()
    b.grid(row=0, column=0)
    b2 = Button(frame, text="...")
    b2.grid(row=1, column=1)
    root.mainloop()
