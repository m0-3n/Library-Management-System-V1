import sqlite3

connector = sqlite3.connect("List_of_Books.db")

cursor = connector.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS books
               (book_name text,
               author_name text, 
               issue_status text
               )""")
connector.commit()


def view_all():
    cursor.execute("SELECT rowid, * FROM books")
    connector.commit()

    for i in cursor.fetchall():
        print(i)

def update_status(book_update):
    sql_query = """
    UPDATE books SET issue_status = 'Unavailable' WHERE book_name = ?
    """
    cursor.execute(sql_query, book_update)
    connector.commit()

def update_information(og_book, name_book, name_author, issue = 'Available'):
    sql_query = """
    UPDATE books SET book_name = ? WHERE book_name = ?
    """
    cursor.execute(sql_query, (name_book, og_book))
    
    sql_query = """
    UPDATE books SET author_name = ? WHERE book_name = ?
    """
    cursor.execute(sql_query, (name_author, name_book))
    
    sql_query = """
    UPDATE books SET issue_status = ? WHERE book_name = ?
    """
    cursor.execute(sql_query, (issue, name_book))
    connector.commit()

def add_books(book_name, author_name,issue = 'Available'):
    sql_query = """
    INSERT INTO books (book_name,author_name,issue_status)
    VALUES (?, ?, ?)
    """
    record = (book_name,author_name,issue)
    cursor.execute(sql_query, record)
    connector.commit()

def del_books(book_del):
    cursor.execute("DELETE FROM books WHERE book_name=?", (book_del))
    connector.commit()

view_all()



connector.close()