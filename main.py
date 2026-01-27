from customtkinter import *
import tkinter as tk
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
bg_label=tk.Label(root, image=bg_image, text="", padx=0, pady=0)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#functions
def add_book():
    pass
def view_books():
    pass
def rented_book():
    pass

tk.Label(bg_label, text="Library Management System", font=("Arial", 24), fg="black").pack(pady=20)


#buttons
add_book=CTkButton(bg_label, text="Add Book", font=("Arial", 16), fg_color="#d9d9d9",text_color='black',corner_radius=0,bg_color='transparent', command=add_book)
add_book.pack(padx=10, pady=10)

view_books=CTkButton(bg_label, text="View Books", font=("Arial", 16), fg_color="#d9d9d9",text_color='black',corner_radius=0,bg_color='transparent', command=view_books)
view_books.pack(padx=10, pady=10)

rented_book=CTkButton(bg_label, text="Rented Book", font=("Arial", 16), fg_color="#d9d9d9",text_color='black',corner_radius=0,bg_color='transparent', command=rented_book)
rented_book.pack(padx=10, pady=10)

root.mainloop()