from tkinter import *
from tkinter import messagebox

student_info = {'Moin':'password'}

def quit_1():
    messagebox.showinfo("Attention!", 'You will be exiting the GUI')
    exit()
    
def usr_pwd_stud():
    global username
    global password
    
    username = usr_stud.get()
    password = pwd_stud.get()
    if str(username) in student_info:
        if student_info[username] == password:
            messagebox.showinfo("Information","Successfully Signed In!")
        else:
            messagebox.showerror("Error", "Wrong Password")
    else:
        messagebox.showerror("Error", "Wrong Username")
    quit_1()

if __name__ =='__main__':

    
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
    button2 = Button(window_login, text = 'Login', command = usr_pwd_stud, relief = RAISED, font = ("arial", 12, "bold"), fg = 'black', bg = 'red').place(x=135, y=250)
    button3 = Button(window_login, text = 'Close', command = quit_1, relief = RAISED, font = ("arial", 12, "bold"), fg = 'black', bg = 'red').place(x=200, y=250)
    
    
    window_login.mainloop()