from tkinter import *
from PIL import ImageTk, Image

if __name__ == '__main__':
    root = Tk()
    root.title("SIEEEMA")
    root.iconbitmap("tk8_icon.ico")

    my_img = ImageTk.PhotoImage(Image.open("tk8_image.jpg"))
    my_label = Label(image=my_img)
    my_label.pack()

    button_quit = Button(root, text="Exit", command=root.quit)
    button_quit.pack()

    root.mainloop()
