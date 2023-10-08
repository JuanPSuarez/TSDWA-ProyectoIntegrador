import mysql.connector

# Configura la conexión a la base de datos
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Libroteka"
)



class Book:
    def __init__(self, title, author, genre, description, publicationDate, price, stock):
        self.title = title
        self.author = author
        self.genre = genre
        self.description = description
        self.publicationDate = publicationDate
        self.price = price
        self.stock = stock

# Función para crear un nuevo libro en la base de datos
def create_book(book):
    cursor = db_connection.cursor()
    insert_query = "INSERT INTO books (title, author, genre, description, publicationDate, price, stock) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    data = (book.title, book.author, book.genre, book.description, book.publicationDate, book.price, book.stock)
    cursor.execute(insert_query, data)
    db_connection.commit()
    cursor.close()

# Función para obtener todos los libros de la base de datos
def get_all_books():
    cursor = db_connection.cursor(dictionary=True)
    select_query = "SELECT * FROM books"
    cursor.execute(select_query)
    books = cursor.fetchall()
    cursor.close()
    return books

# Función para obtener un libro por su ID
def get_book_by_id(book_id):
    cursor = db_connection.cursor(dictionary=True)
    select_query = "SELECT * FROM books WHERE id = %s"
    cursor.execute(select_query, (book_id,))
    book = cursor.fetchone()
    cursor.close()
    return book

# Función para actualizar la información de un libro
def update_book(book_id, new_book_data):
    cursor = db_connection.cursor()
    update_query = "UPDATE books SET title=%s, author=%s, genre=%s, description=%s, publicationDate=%s, price=%s, stock=%s WHERE id=%s"
    data = (
        new_book_data.title, new_book_data.author, new_book_data.genre, new_book_data.description,
        new_book_data.publicationDate, new_book_data.price, new_book_data.stock, book_id
    )
    cursor.execute(update_query, data)
    db_connection.commit()
    cursor.close()

# Función para eliminar un libro por su ID
def delete_book(book_id):
    cursor = db_connection.cursor()
    delete_query = "DELETE FROM books WHERE id = %s"
    cursor.execute(delete_query, (book_id,))
    db_connection.commit()
    cursor.close()
