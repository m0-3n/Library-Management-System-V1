from tkinter import *
from tkinter import messagebox
import sqlite3


connector = sqlite3.connect('List_of_Books.db')
cursor = connector.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS books
               (book_name text,
               author_name text, 
               issue_status text
               )""")
connector.commit()


admin_info = {'admin':'password'}
student_info = {'Moin':'password'}
sample_books = [('the diary of a winpy kid', 'jeff kiney', 'Available'), ('think and grow rich', 'Napoleon Hill', 'Unavailable')]

# pass statement so i dont get errors
def pass_statement():
    pass


def quitt():
    messagebox.showinfo("Attention!", 'You will be exiting the GUI')
    exit()


# main page
def main():
    global root
    root = Tk()
    root.geometry('200x200')
    root.resizable(False, False)
    root.title("Library Management System")
    label0 = Label(root, text = "Library", relief = "solid", width = 20, font = ("arial",19 ,"bold"), fg = 'white', bg = 'black').pack(fill = BOTH, padx = 2, pady = 2)
    Button0 = Button(root, text = "Admin", relief = "solid", width = 8, font = ("arial",19 ,"bold"), fg = 'white', bg = 'black', command=destroy_wind).place(x = 35, y = 62)
    Button1 = Button(root, text = "Student", relief = "solid", width = 8, font = ("arial",19 ,"bold"), fg = 'white', bg = 'black', command=student_page).place(x = 35, y = 127)
    
    root.mainloop()


# The password checker window
def usr_pwd():
    global username
    global password
    global admin_info
    
    username = usr.get()
    password = pwd.get()
    if str(username) in admin_info:
        if admin_info[username] == password:
            messagebox.showinfo("Information","Successfully Signed In!")
        else:
            messagebox.showerror("Error", "Wrong Password")
    else:
        messagebox.showerror("Error", "Wrong Username")
    window0.withdraw()
    admin_page()
    


# admin page where they select to add books or delete them
def admin_page():
    global window2
    window2 = Tk()
    window2.geometry('500x550')
    window2.resizable(False, False)
    window2.title("Admin")
    label1 = Label(window2, text = "Admin Page", relief = "solid", width = 20, font = ("arial",19 ,"bold"), fg = 'white', bg = 'black').pack(fill = BOTH, padx = 2, pady = 2)
    button1 = Button(window2, text = 'Add Books', command =add_page, relief=RAISED, font = ("arial", 20, "bold"), width=20, fg='black').place(x=80, y= 95)
    button1 = Button(window2, text = "Delete Books", command = pass_statement, relief=RAISED, font = ("arial", 20, "bold"), width=20, fg='black').place(x=80, y= 155)
    
    
    window2.mainloop()
    

# the admin page where we enter information of the book to be added
def add_page():
    global new_book_name, new_author_name, new_issue_status
    
    add_books_page = Toplevel()
    add_books_page.geometry('450x450')
    add_books_page.resizable(False, False)
    add_books_page.title("Add Books")
    new_book_name = StringVar()
    new_author_name = StringVar()
    new_issue_status = StringVar()
    label01 = Label(add_books_page, text = 'Add a Book', relief = "solid", width = 20, font = ("arial",19 ,"bold"), fg = 'black', bg = 'red').pack(fill = BOTH, padx = 2, pady = 2)
    label4 = Label(add_books_page, text = 'Enter Book Name:', width = 20, font = ("arial",12 ,"bold"), fg = 'red').place(x = 20, y = 120)
    label5 = Label(add_books_page, text = 'Enter Author Name:', width = 20, font = ("arial",12 ,"bold"), fg = 'red').place(x = 23, y = 195)
    label6 = Label(add_books_page, text = 'Enter Issue Status:', width = 20, font = ("arial",12 ,"bold"), fg = 'red').place(x = 22, y = 270)
    entry3 = Entry(add_books_page, textvar = new_book_name).place(x = 260, y = 122)
    entry4 = Entry(add_books_page, textvar = new_author_name).place(x = 260, y = 197)
    radio1 = Radiobutton(add_books_page, text = 'Available', variable = new_issue_status, value='Available').place(x = 220, y = 273)
    radio1 = Radiobutton(add_books_page, text = 'Unavailable', variable = new_issue_status, value='Unavailable').place(x = 330, y = 273)
    button4 = Button(add_books_page, text = 'Add Book', command = add_book_dict, relief = RAISED, font = ("arial", 12, "bold"), fg = 'black', bg = 'red').place(x=175, y = 355)
    add_books_page.mainloop()


def add_book_dict():
    new_sample_books = (new_book_name.get(),new_author_name.get(),new_issue_status.get())
    sample_books.append(new_sample_books)
    print(sample_books)

def delete_book():
    window3 = Toplevel()
    window3.geometry('450x450')
    window3.resizable(False, False)
    window3.title("Add Books")
    del_book_name = StringVar()
    label01 = Label(window3, text = 'Add a Book', relief = "solid", width = 20, font = ("arial",19 ,"bold"), fg = 'black', bg = 'red').pack(fill = BOTH, padx = 2, pady = 2)
    label00 = Label(window3, text = 'Enter Book Name:', width = 20, font = ("arial",12 ,"bold"), fg = 'red').place(x = 20, y = 120)
    entry1 = Entry(window3, textvar = new_book_name).place(x = 260, y = 122)
    button4 = Button(window3, text = "Delete Book", command = add_book_dict, relief = RAISED, font = ("arial", 12, "bold"), fg = 'black', bg = 'red').place(x=175, y = 355)
    window3.mainloop()


# destroys the root window
def destroy_wind():
    root.destroy()
    


def student_login():
    pass


# student page
def student_page():
    window_login = Tk()
    window_login.geometry('400x400')
    window_login.resizable(False, False)
    window_login.title("Student Login")
    usr_stud = StringVar()
    pwd_stud = StringVar()
    label1 = Label(window_login, text = "Student Sign In", relief = "solid", width = 20, font = ("arial",19 ,"bold"), fg = 'white', bg = 'black').pack(fill = BOTH, padx = 2, pady = 2)
    label2 = Label(window_login, text = "Username", width = 20, font = ("arial",12 ,"bold"), fg = 'red').place(x = 30, y = 125)
    label3 = Label(window_login, text = "Password", width = 20, font = ("arial",12 ,"bold"), fg = 'red').place(x = 30, y = 185)
    entry0 = Entry(window_login, textvar = usr_stud).place(x = 200, y = 125)
    entry1 = Entry(window_login, textvar = pwd_stud, show='*').place(x = 200, y = 185)
    button2 = Button(window_login, text = 'Login', command = pass_statement(), relief = RAISED, font = ("arial", 12, "bold"), fg = 'black', bg = 'red').place(x=135, y=250)
    button3 = Button(window_login, text = 'Close', command = quitt, relief = RAISED, font = ("arial", 12, "bold"), fg = 'black', bg = 'red').place(x=200, y=250)
    window_login.mainloop()


    # def usr_pwd_stud():
    #     global username
    #     global password
        
    #     username = usr_stud.get()
    #     password = pwd_stud.get()
    #     if str(username) in student_info:
    #         if student_info[username] == password:
    #             messagebox.showinfo("Information","Successfully Signed In!")
    #         else:
    #             messagebox.showerror("Error", "Wrong Password")
    #     else:
    #         messagebox.showerror("Error", "Wrong Username")
    #     quitt()



def view_all():
    new_sample_books = (new_book_name.get(),new_author_name.get(),new_issue_status.get())
    sample_books.append(new_sample_books)
    print(sample_books)


# main loop window
if __name__ == "__main__":
    main()
    window0 = Tk()
    window0.geometry('400x400')
    window0.resizable(False, False)
    window0.title("Admin Sign In")
    usr = StringVar()
    pwd = StringVar()
    
    label1 = Label(window0, text = "Admin Sign In", relief = "solid", width = 20, font = ("arial",19 ,"bold"), fg = 'white', bg = 'black').pack(fill = BOTH, padx = 2, pady = 2)
    label2 = Label(window0, text = "Username", width = 20, font = ("arial",12 ,"bold"), fg = 'red').place(x = 30, y = 145)
    label3 = Label(window0, text = "Password", width = 20, font = ("arial",12 ,"bold"), fg = 'red').place(x = 30, y = 205)
    entry0 = Entry(window0, textvar = usr).place(x = 200, y = 145)
    entry1 = Entry(window0, textvar = pwd, show='*').place(x = 200, y = 205)
    button2 = Button(window0, text = 'Login', command = usr_pwd, relief = RAISED, font = ("arial", 12, "bold"), fg = 'black', bg = 'red').place(x=135, y=250)
    button3 = Button(window0, text = 'Close', command = quitt, relief = RAISED, font = ("arial", 12, "bold"), fg = 'black', bg = 'red').place(x=200, y=250)
    
    
    window0.mainloop()

