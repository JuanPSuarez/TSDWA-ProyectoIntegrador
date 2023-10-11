import mysql.connector
from config import host, database, user, password

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        return conn
    except Exception as e:
        print(f"Error al conectar a la base de datos: {str(e)}")
        return None

class Book:
    def __init__(self, title, author, genre, description, publicationDate, price, stock):
        self.title = title
        self.author = author
        self.genre = genre
        self.description = description
        self.publicationDate = publicationDate
        self.price = price
        self.stock = stock

    @staticmethod
    def create_book(title, author, genre, description, publicationDate, price, stock):
        conn = get_db_connection()
        if conn is None:
            return "Error al conectar a la base de datos."

        cursor = conn.cursor()

        try:
            insert_query = "INSERT INTO books (title, author, genre, description, publicationDate, price, stock) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (title, author, genre, description, publicationDate, price, stock))
            conn.commit()
            return "Libro creado exitosamente."

        except Exception as e:
            conn.rollback()
            return f"Error al crear el libro: {str(e)}"

        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def read_books():
        conn = get_db_connection()
        if conn is None:
            return "Error al conectar a la base de datos."

        cursor = conn.cursor()

        try:
            select_query = "SELECT * FROM books"
            cursor.execute(select_query)
            books = cursor.fetchall()
            return books

        except Exception as e:
            return f"Error al leer los libros: {str(e)}"

        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def update_book(book_id, title, author, genre, description, publicationDate, price, stock):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            query = "UPDATE books SET title=%s, author=%s, genre=%s, description=%s, publicationDate=%s, price=%s, stock=%s WHERE id=%s"
            values = (title, author, genre, description, publicationDate, price, stock, book_id)

            cursor.execute(query, values)
            conn.commit()

            return "Libro actualizado exitosamente."

        except Exception as e:
            return f"Error al actualizar el libro: {str(e)}"

        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def delete_book(book_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            query = "DELETE FROM books WHERE id=%s"
            values = (book_id,)

            cursor.execute(query, values)
            conn.commit()

            return "Libro eliminado exitosamente."

        except Exception as e:
            return f"Error al eliminar el libro: {str(e)}"

        finally:
            cursor.close()
            conn.close()
