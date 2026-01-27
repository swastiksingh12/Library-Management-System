from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
root=Tk()
root.geometry("600x500")
root.maxsize(600,500)
root.title("Library Management System")


#functions
def add_book():
    pass
def view_books():
    pass
def rented_book():
    pass


#Add Book Menu
add_frame=Frame(root, bg='#c0c0c0')
add_frame.place(x=0, y=0, relwidth=1, relheight=1)
up_add=Frame(add_frame, bg='#c0c0c0')
up_add.pack(fill=X, padx=10, pady=(10,0))
back_add=Button(up_add, text="Back", font=("Arial", 12),command=lambda:home_frame.tkraise())
back_add.pack(padx=10, pady=10,side=LEFT,fill=BOTH,expand=True,)
home_add=Button(up_add, text="Home", font=("Arial", 12),command=lambda:home_frame.tkraise())
home_add.pack(padx=10, pady=10,side=RIGHT,fill=BOTH,expand=True)
down_add=Frame(add_frame, bg='white')
down_add.pack(fill=BOTH, expand=True, padx=20, pady=(0,20))
Label(down_add, text="Add Book Section", font=("Arial", 20, 'bold'), bg='white').pack(pady=(10,0))
#entries
add_entry=Frame(down_add, bg='red')
add_entry.pack(expand=True,fill=BOTH,pady=(0,20),padx=20)
add_entry_left=Frame(add_entry, bg='blue')
add_entry_left.pack(side=LEFT,expand=True,fill=BOTH,padx=20,pady=20)
add_entry_right=Frame(add_entry, bg='blue')
add_entry_right.pack(side=RIGHT,expand=True,fill=BOTH,padx=20,pady=20)
Label(add_entry_left, text="Book Title:", font=("Arial", 14)).pack(fill=BOTH, pady=10, anchor='e')
Label(add_entry_left, text="Author Name:", font=("Arial", 14)).pack(fill=BOTH, pady=10, anchor='e')
Label(add_entry_left, text="Genre:", font=("Arial", 14)).pack(fill=BOTH, pady=10, anchor='e')
Label(add_entry_left, text="INBN No.:", font=("Arial", 14)).pack(fill=BOTH, pady=10, anchor='e')
Label(add_entry_left, text="Book Year:", font=("Arial", 14)).pack(fill=BOTH, pady=10, anchor='e')

Genre=['Fantacy', 'Science Fiction', 'Mystery', 'Thriller', 'Romance', 'Westerns', 'Dystopian', 'Contemporary']
sel_opt=StringVar()
sel_opt.set(Genre[0])
combo=Combobox(add_entry_right,textvariable=sel_opt, values=Genre,state='readonly')
combo.pack(fill=BOTH, pady=10)

add_book_btn=Button(down_add, text="Add Book", font=("Arial", 16), command=add_book)
add_book_btn.pack(pady=10)

#main frame
home_frame=Frame(root)
home_frame.place(x=0, y=0, relwidth=1, relheight=1)
bg=ImageTk.PhotoImage(file="bg.jpg")
bg_image=Label(home_frame, image=bg)
bg_image.place(x=0, y=0, relwidth=1, relheight=1)
Label(home_frame, text="Library Management System", font=("Kranky", 30, 'bold')).pack(pady=100)
#buttons
add_book=Button(home_frame, text="Add Book", font=("Arial", 16), command=lambda:add_frame.tkraise())
add_book.place(relheight=0.1, relwidth=0.3, relx=0.35, rely=0.45)

view_books=Button(home_frame, text="View Books", font=("Arial", 16), command=view_books)
view_books.place(relheight=0.1, relwidth=0.3, relx=0.35, rely=0.6)

rented_book=Button(home_frame, text="Rented Book", font=("Arial", 16), command=rented_book)
rented_book.place(relheight=0.1, relwidth=0.3, relx=0.35, rely=0.75)

Label(home_frame, text="All Right Reserved", font=("Arial", 10)).pack(side=BOTTOM, pady=20)
root.mainloop()