from tkinter import *
from PIL import Image, ImageTk
root=Tk()
root.geometry("600x500")
root.maxsize(600,500)
root.title("Library Management System")

#background image
bg_image=Image.open('bg.jpg')
bg_image=bg_image.resize((600, 500), Image.LANCZOS)
bg_image=ImageTk.PhotoImage(bg_image)
bg_label=Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#functions
def add_book():
    pass
def view_books():
    pass
def rented_book():
    pass


#buttons
add_book=Button(root, text="Add Book", font=("Arial", 16), bg="lightblue", fg="black", padx=10, pady=5, command=add_book)
add_book.pack(padx=10, pady=10)

view_books=Button(root, text="View Books", font=("Arial", 16), bg="lightgreen", fg="black", padx=10, pady=5, command=view_books)
view_books.pack(padx=10, pady=10)

rented_book=Button(root, text="Rented Book", font=("Arial", 16), bg="lightcoral", fg="black", padx=10, pady=5, command=rented_book)
rented_book.pack(padx=10, pady=10)

root.mainloop()