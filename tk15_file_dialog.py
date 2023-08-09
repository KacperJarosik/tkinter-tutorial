from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

if __name__ == '__main__':
    root = Tk()
    root.title("SIEEEMA")
    root.iconbitmap("tk8_icon.ico")


    def open():
        # Without global variable function can't show image
        global my_image
        root.filename = filedialog.askopenfilename(initialdir="C:\\Users\\PC2\Desktop\\(.)(.)", title="Select a file",
                                                   filetypes=(("png files", "*.png"), ("all files", "*.*")))
        my_label = Label(root, text=root.filename).pack()
        my_image = ImageTk.PhotoImage(Image.open(root.filename))
        my_image_label = Label(image=my_image).pack()


    my_btn = Button(root, text="Open file", command=open).pack()
    root.mainloop()
