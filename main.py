from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
from pyzbar.pyzbar import decode
from PIL import Image



# <---------------------------------------------------------------------------------------------------------------------------------->
# db
connector = sqlite3.connect('yeye.db')
cursor = connector.cursor()

a = cursor.execute("SELECT * FROM Hmm_sample")
connector.commit()

# <---------------------------------------------------------------------------------------------------------------------------------->
# Samples
admin_info = {'admin':'password'}
sample_books = [['the diary of a winpy kid', 'jeff kiney', 'puffin'], ['think and grow rich', 'Napoleon Hill', 'bestseller']]



# <---------------------------------------------------------------------------------------------------------------------------------->
# Commands
def pass_statement():
    pass

def exit_1():
    messagebox.showwarning("Attention!", 'You will exit this GUI')
    exit()



# <---------------------------------------------------------------------------------------------------------------------------------->
# Admin
def admin_login():
    window0 = Toplevel()
    window0.geometry('400x400')
    window0.resizable(False, False)
    window0.title("Admin Sign In")

    label1 = Label(window0, text = "Admin Sign In", relief = "solid", width = 20, font = ("arial",19 ,"bold"), fg = 'white', bg = 'black').pack(fill = BOTH, padx = 2, pady = 2)
    label2 = Label(window0, text = "Username", width = 20, font = ("arial",12 ,"bold"), fg = 'red').place(x = 30, y = 145)
    label3 = Label(window0, text = "Password", width = 20, font = ("arial",12 ,"bold"), fg = 'red').place(x = 30, y = 205)
    entry0 = Entry(window0, textvar = usr).place(x = 200, y = 145)
    entry1 = Entry(window0, textvar = pwd, show='*').place(x = 200, y = 205)
    button2 = Button(window0, text = 'Login', command = usr_pwd, relief = RAISED, font = ("arial", 12, "bold"), fg = 'black', bg = 'red').place(x=135, y=250)
    button3 = Button(window0, text = 'Close', command = exit_1, relief = RAISED, font = ("arial", 12, "bold"), fg = 'black', bg = 'red').place(x=200, y=250)
    
    window0.mainloop()


def usr_pwd():
    global username
    global password
    
    username = usr.get()
    password = pwd.get()
    if str(username) in admin_info:
        if admin_info[username] == password:
            messagebox.showinfo("Information","Successfully Signed In!")
            admin_page()
        else:
            messagebox.showerror("Error", "Wrong Password")
    else:
        messagebox.showerror("Error", "Wrong Username")


def admin_page():
    global window2
    window2 = Tk()
    window2.geometry('400x300')
    window2.resizable(False, False)
    window2.title("Admin")

    # label_BG3 = Label(window2, image = img).place(x=0, y=0, relwidth=1, relheight=1)
    
    label1 = Label(window2, text = "Admin Commands", relief = "solid", width = 20, font = ("arial",19 ,"bold"), fg = 'white', bg = 'black').pack(fill = BOTH, padx = 2, pady = 2)
    button1 = Button(window2, text = 'Add Books', command =add_page, relief=RAISED, font = ("arial", 20, "bold"), width=15, fg='black').place(x=65, y= 95)
    button1 = Button(window2, text = "Delete Books", command = del_book, relief=RAISED, font = ("arial", 20, "bold"), width=15, fg='black').place(x=65, y= 175)
    window2.mainloop()



# <---------------------------------------------------------------------------------------------------------------------------------->
# Admin - Add Book
def add_page():
    global new_book_name, new_author_name, new_publisher_name, new_no_copies
    
    add_books_page = Toplevel()
    add_books_page.geometry('450x450')
    add_books_page.resizable(False, False)
    add_books_page.title("Add Books")
    new_book_name = StringVar()
    new_author_name = StringVar()
    new_publisher_name = StringVar()
    new_no_copies = IntVar()
    
    
    label01 = Label(add_books_page, text = 'Add a Book', relief = "solid", width = 20, font = ("arial",19 ,"bold"), fg = 'black', bg = 'red').pack(fill = BOTH, padx = 2, pady = 2)
    label4 = Label(add_books_page, text = 'Enter Book Name:', width = 20, font = ("arial",12 ,"bold"), fg = 'red').place(x = 20, y = 100)
    label5 = Label(add_books_page, text = 'Enter Author Name:', width = 20, font = ("arial",12 ,"bold"), fg = 'red').place(x = 23, y = 175)
    label6 = Label(add_books_page, text = 'Enter Publisher Name:', width = 20, font = ("arial",12 ,"bold"), fg = 'red').place(x = 22, y = 250)
    label7 = Label(add_books_page, text = 'Enter Number of Copies:', width = 20, font = ("arial",12 ,"bold"), fg = 'red').place(x = 22, y = 325)
    
    entry3 = Entry(add_books_page, textvar = new_book_name).place(x = 260, y = 102)
    entry4 = Entry(add_books_page, textvar = new_author_name).place(x = 260, y = 177)
    entry5 = Entry(add_books_page, textvar = new_publisher_name).place(x = 260, y = 252)
    button4 = Button(add_books_page, text = 'Add Book', command = add_book_dict, relief = RAISED, font = ("arial", 12, "bold"), fg = 'black', bg = 'red').place(x=175, y = 375)
    entry5 = Entry(add_books_page, textvar = new_no_copies, width=3).place(x = 310, y = 327)
    
    add_books_page.mainloop()
    
def add_book_dict():
    new_sample_books = (new_book_name.get(),new_author_name.get(),new_publisher_name.get(), new_no_copies.get())
    sample_books.append(new_sample_books)
    print(sample_books)

# <---------------------------------------------------------------------------------------------------------------------------------->
# Admin - Delete Book
def del_book():
    global del_book_name
    
    del_book_wind = Toplevel()
    del_book_wind.geometry("450x250")
    del_book_wind.title("Delete Books")
    del_book_wind.resizable(False, False)
    del_book_name = StringVar()
    
    
    label01 = Label(del_book_wind, text = 'Delete a Book', relief = "solid", width = 20, font = ("arial",19 ,"bold"), fg = 'black', bg = 'red').pack(fill = BOTH, padx = 2, pady = 2)
    label4 = Label(del_book_wind, text = 'Enter Book Name:', width = 20, font = ("arial",12 ,"bold"), fg = 'red').place(x = 20, y = 100)
    entry3 = Entry(del_book_wind, textvar = del_book_name).place(x = 260, y = 102)
    button4 = Button(del_book_wind, text = 'Delete Book', command = del_func, relief = RAISED, font = ("arial", 12, "bold"), fg = 'black', bg = 'red').place(x=175, y = 175)
    
    
    del_book_wind.mainloop()

def del_func():
    pass

# <---------------------------------------------------------------------------------------------------------------------------------->
# detect barcode for issuing
def detect_code():
    global win_detect
    win_detect = Tk()
    win001.title("Issue Book")
    for bar in decode(Image.open('C:/Users/moin6/PycharmProjects/Projects/LMS/barcode.jpg')):
        print(bar.data)
        print(bar.type)



# <---------------------------------------------------------------------------------------------------------------------------------->
# view the books in tabular form
def view_all():
    global win001
    win001 = Tk()
    win001.geometry('1080x1080')
    # win001.resizable(False, False)

    win001.title("View Books")
    
    i = 0
    for student in a: 
        for j in range(len(student)):
            e = Entry(win001, width=(len(str(student[j]))), fg='black') 
            e.grid(row=i, column=j)
            e.insert(END, student[j])
        i += 1
    win001.mainloop()
    


# <---------------------------------------------------------------------------------------------------------------------------------->
# main()
if __name__ == '__main__':
    root = Tk()
    root.geometry('500x550')
    root.resizable(False, False)
    root.title("LMS")
    
    img = ImageTk.PhotoImage(file= r"C:\Users\moin6\PycharmProjects\Projects\LMS\download.jpg")
    Label_BG = Label(root, image=img).place(x=0, y=0, relwidth=1, relheight=1)
    
    usr = StringVar()
    pwd = StringVar()
    
    menu = Menu(root)
    root.config(menu = menu)
    
    sub_menu_1 = Menu(menu)
    menu.add_cascade(label = "Option", menu = sub_menu_1)
    sub_menu_1.add_command(label = "Admin", command = admin_login)
    sub_menu_1.add_command(label = "Exit", command = exit_1)
    
    label0 = Label(root, text = "Library Management System", relief = "solid", width = 25, font = ("arial",25 ,"bold"), fg = 'white', bg = 'black').pack(fill = BOTH, padx = 0, pady = 0)
    Button0 = Button(root, text = "Issue", relief = "solid", width = 8, font = ("arial",27 ,"bold"), bg = 'white', fg = 'black', command=detect_code).place(x = 155, y = 107)
    Button1 = Button(root, text = "Return", relief = "solid", width = 8, font = ("arial",27 ,"bold"), bg = 'white', fg = 'black', command=pass_statement).place(x = 155, y = 247)
    Button1 = Button(root, text = "View", relief = "solid", width = 8, font = ("arial",27 ,"bold"), bg = 'white', fg = 'black', command=view_all).place(x = 155, y = 387)

    root.mainloop()