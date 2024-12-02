import sqlite3


def initiate_db():
    with sqlite3.connect('initiate.db') as db:
        cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Products(
     id integer PRIMARY KEY,
     title text NOT NULL,
     description text ,
     price integer NOT NULL);
     """)

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        );
        ''')

    for i in range(1, 5):
        cursor.execute('INSERT INTO Products (title, description, price)VALUES(?,?,?)',
                       (f"Продукт {i}", f"описание {i}", i * 100))

    db.commit()
    # connection.close()


def add_user(username, email, age):
    with sqlite3.connect('initiate.db') as db:
        cursor = db.cursor()
    cursor.execute(f"INSERT INTO Users (username, email, age, balance) VALUES ('{username}', '{email}', '{age}', 1000)")
    db.commit()


def is_included(username):
    connection = sqlite3.connect('initiate.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Users WHERE username = ?", (username,))
    user = cursor.fetchone()
    if user is None:
        return True
    else:
        return False


def get_all_products():
    with sqlite3.connect('initiate.db') as db:
        cursor = db.cursor()
    cursor.execute("SELECT * FROM Products")

    db.commit()
    return cursor.fetchall()
