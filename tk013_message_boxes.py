from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
    response = messagebox.askyesno("This is my popup!", "Hello World")
    # Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You clicked yes").pack()
    else:
        Label(root, text="You clicked no").pack()
if __name__ == '__main__':
    root = Tk()
    root.title("SIEEEMA")
    root.iconbitmap("tk8_icon.ico")

    Button(root, text="popup", command=popup).pack()

    root.mainloop()
