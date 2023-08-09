from tkinter import *
from PIL import ImageTk, Image


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 4:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back= Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


if __name__ == '__main__':
    root = Tk()
    root.title("Prezentacja")
    root.iconbitmap("tk8_icon.ico")

    my_img1 = ImageTk.PhotoImage(Image.open("tk8_image.jpg"))
    my_img2 = ImageTk.PhotoImage(Image.open("C:\\Users\\PC2\\Desktop\\(.)(.)\\0fc8408806e3e2a4765fee259120bd11.jpg"))
    my_img3 = ImageTk.PhotoImage(Image.open("C:\\Users\\PC2\\Desktop\\(.)(.)\\images.png"))
    my_img4 = ImageTk.PhotoImage(Image.open("C:\\Users\\PC2\\Desktop\\(.)(.)\\pobrane.jpg"))

    image_list = [my_img1, my_img2, my_img3, my_img4]

    my_label = Label(image=my_img1)
    my_label.grid(row=0, column=0, columnspan=3)

    button_back = Button(root, text="<<", command=lambda: back(2),state=DISABLED)
    button_quit = Button(root, text="Exit", command=root.quit)
    button_forward = Button(root, text=">>", command=lambda: forward(2))

    button_back.grid(row=1, column=0)
    button_quit.grid(row=1, column=1)
    button_forward.grid(row=1, column=2)

    root.mainloop()
