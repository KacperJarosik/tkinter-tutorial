from tkinter import *
from PIL import ImageTk, Image
def open():
    # Without global variable function can't show image
    global my_img
    top = Toplevel()
    top.title("My second window")
    lbl = Label(top, text="Hello World").pack()
    my_img = ImageTk.PhotoImage(Image.open("tk8_image.jpg"))
    my_label= Label(top, image=my_img).pack()
    btn2 = Button(top,text="close the window",command=top.destroy).pack()

if __name__ == '__main__':
    root = Tk()
    root.title("SIEEEMA")
    root.iconbitmap("tk8_icon.ico")

    btn = Button(root, text="Open Second Window", command=open).pack()



    root.mainloop()
