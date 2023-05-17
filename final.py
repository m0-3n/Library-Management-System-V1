from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
from pyzbar.pyzbar import decode
import sqlite3
import requests
from bs4 import BeautifulSoup

admin_info = {'admin':'password'}
connector = sqlite3.connect("Final_db.db")
cursor = connector.cursor()
cursor.execute("""
               CREATE TABLE IF NOT EXISTS books
               (Book_ID text, 
               issue_status text,
               copies INTEGER)
               """)
connector.commit()

def pass_statement():
    pass

def exit_2():
    window0.destroy()

def exit_1():
    exit()

def admin_login():
    global window0
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
    button3 = Button(window0, text = 'Close', command = exit_2, relief = RAISED, font = ("arial", 12, "bold"), fg = 'black', bg = 'red').place(x=200, y=250)
    
    window0.mainloop()
    
def usr_pwd():
    global username
    global password
    
    username = usr.get()
    password = pwd.get()
    if str(username) in admin_info:
        if admin_info[username] == password:
            messagebox.showinfo("Information","Successfully Signed In!")
            usr.set('')
            pwd.set('')
            window0.destroy()
            admin_page()
        else:
            messagebox.showerror("Error", "Wrong Password")
            # admin_login()
    else:
        messagebox.showerror("Error", "Wrong Username")
        # admin_login()
        
def admin_page():
    
    def exit_admin():
        window2.destroy()

    global window2
    window2 = Tk()
    window2.geometry('400x300')
    window2.resizable(False, False)
    window2.title("Admin")

    # label_BG3 = Label(window2, image = img).place(x=0, y=0, relwidth=1, relheight=1)
    
    label1 = Label(window2, text = "Admin Commands", relief = "solid", width = 20, font = ("arial",19 ,"bold"), fg = 'white', bg = 'black').pack(fill = BOTH, padx = 2, pady = 2)
    button1 = Button(window2, text = 'View Issued Books', command = view_all_admin, relief=RAISED, font = ("arial", 20, "bold"), width=15, fg='white', bg = 'black').place(x=65, y= 95)
    button1 = Button(window2, text = "Exit Admin", command = exit_admin, relief=RAISED, font = ("arial", 20, "bold"), width=15, fg='white', bg = 'black').place(x=65, y= 175)
    window2.mainloop()
    
def issue_return_scanner():
    global qr_data
    cap = cv2.VideoCapture(0)
    def get_qr_data(input_frame):
        try:
            return decode(input_frame)
        except:
            return ""

    while True:
        dont_mind, frame = cap.read()
        try:
            qr_obj = get_qr_data(frame)
            qr_data = str(qr_obj[0][0])
            # qr_data = (qr_data)[2:-1]
            print(qr_data)
            if qr_obj != "":
                break
        except:
            pass
        cv2.imshow("Capture The Barcode!", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def web_scrap():
    try:
        global tag
        barcode = qr_data[2:-1]

        url = "https://isbndb.com/book/" + barcode

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        tag = doc.find_all("td")[0]
    
    except:
        messagebox.showerror("Attention!", "Book Not Found.")

def issue_db(issued="Issued", copies = 1):
    sql_query = """
    INSERT INTO books (Book_ID,issue_status,copies) VALUES (?, ?,?)
    ON CONFLICT(Book_ID) DO UPDATE SET copies = copies + 1; 
    """
    web_scrap()
    record = (tag.string,issued,copies)
    cursor.execute(sql_query, record)
    connector.commit()
    
    messagebox.showinfo("Information","The Book: " + tag.string + ". \nHas been issued!")

def return_db():
    web_scrap()
    tagstr = tag.string
    cursor.execute("SELECT Book_ID FROM books WHERE Book_ID = ?", [tagstr])
    result = cursor.fetchone()
    if result:
        cursor.execute("""
        UPDATE books SET copies = copies - 1 WHERE Book_ID = ?;
        """,[tagstr])
        cursor.execute("DELETE FROM books WHERE copies <= 0")
        connector.commit()
        messagebox.showinfo("Information","The Book: " + tagstr + ". \nHas Been Returned")
    else:
        messagebox.showerror("Attention!", "Book Unavailable!")
        
    connector.commit()
    

def view_all_admin():
    a = cursor.execute("SELECT rowid, * FROM books")
    connector.commit()
    global win001
    win001 = Tk()
    win001.geometry('1080x1080')
    # win001.resizable(False, False)

    win001.title("View Books")
    
    i = 1
    top_heading = ["S.No.", "Book ID", "Issue_Status", "Copies"]
    for top_label in top_heading:
        for column_no in range(4):
            x = Entry(win001, width = len(top_heading[column_no]), fg='black')
            x.grid(row = 0, column = column_no)
            x.insert(END, top_heading[column_no])
    for student in a: 
        for j in range(len(student)):
            e = Entry(win001, width=(len(str(student[j]))), fg='black') 
            e.grid(row=i, column=j)
            e.insert(END, student[j])
        i += 1
    win001.mainloop()

if __name__ == '__main__':
    root = Tk()
    root.geometry('1080x720')
    root.resizable(False, False)
    root.title("LMS")
    
    img = ImageTk.PhotoImage(file= r"download.jpg")
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
    Button0 = Button(root, text = "Issue\na Book", relief = "solid", width = 10, height=8, font = ("arial",40 ,"bold"), bg = 'grey', fg = 'black', command=lambda:[issue_return_scanner(),issue_db()]).place(x = 65, y = 107)
    Button1 = Button(root, text = "Return\na Book", relief = "solid", width = 10, height=8, font = ("arial",40 ,"bold"), bg = 'grey', fg = 'black', command=lambda:[issue_return_scanner(), return_db()]).place(x = 675, y = 107)
    Button3 = Button(root, text = 'Exit', relief = "solid", font = ("arial",15 ,"bold"), bg = 'white', fg = 'black', command=exit_1).place(x = 515,y = 653)
    root.mainloop()
