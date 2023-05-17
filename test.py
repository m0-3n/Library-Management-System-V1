# import sqlite3
# from tkinter import *

# connector = sqlite3.connect("story_books.db")
# cursor = connector.cursor()
# cursor.execute("SELECT * FROM BOOKS")
# while True:
#     data = cursor.fetchone()
#     if data == None:
#         break
#     print(data)
    
# def view_all_admin():
#     a = cursor.execute("SELECT * FROM BOOKS")
#     connector.commit()
#     global win001
#     win001 = Tk()
#     win001.geometry('1080x1080')
#     # win001.resizable(False, False)
    
#     win001.title("View Books")
    
#     i = 1
#     top_heading = ["S.No.", "Book ID", "Issue_Status", "Copies"]
#     for top_label in top_heading:
#         for column_no in range(4):
#             x = Entry(win001, width = len(top_heading[column_no]), fg='black')
#             x.grid(row = 0, column = column_no)
#             x.insert(END, top_heading[column_no])
#     for student in a: 
#         for j in range(len(student)):
#             e = Entry(win001, width=(len(str(student[j]))), fg='black') 
#             e.grid(row=i, column=j)
#             e.insert(END, student[j])
#         i += 1
#     win001.mainloop()
# view_all_admin()