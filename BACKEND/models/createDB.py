import sqlite3

def create_database():
    try:
        cnx = sqlite3.connect('librotekaDB.db')
        cursor = cnx.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                disponibilidad TEXT NOT NULL,
                price REAL NOT NULL,
                sinopsis TEXT,
                editorial TEXT,
                ISBN TEXT NOT NULL,
                num_paginas INTEGER,
                idioma TEXT,
                formato TEXT,
                clasificacion TEXT,
                publicationDate DATE
            )
        ''')

        cnx.commit()

        print("Database created successfully.")

    except sqlite3.Error as err:
        print("Error: {}".format(err))

    finally:
        if 'cnx' in locals() and cnx is not None:
            cnx.close()

if __name__ == "__main__":
    create_database()