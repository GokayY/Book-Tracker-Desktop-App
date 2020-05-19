import sqlite3 as sql
import os.path

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, "books.db")

def connect():
    conn = sql.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sql.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO books Values (NULL, ?, ?, ?, ?)",(title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sql.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbn=""):
    conn = sql.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title=? OR author=? or year=? OR isbn=?", (title, author, year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sql.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn = sql.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect()