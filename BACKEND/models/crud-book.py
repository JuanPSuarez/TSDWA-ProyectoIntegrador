from book import Book
import sqlite3

class BookCRUD:
    @staticmethod
    def create_book(title, author, disponibilidad, price, sinopsis, editorial, ISBN, num_paginas, idioma, formato, clasificacion, publicationDate):
        try:
            cnx = sqlite3.connect('librotekaDB.db')  # Update the database name

            cursor = cnx.cursor()
            add_book = (
                "INSERT INTO books "
                "(title, author, disponibilidad, price, sinopsis, editorial, ISBN, num_paginas, idioma, formato, clasificacion, publicationDate) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            )

            book_data = (title, author, disponibilidad, price, sinopsis, editorial, ISBN, num_paginas, idioma, formato, clasificacion, publicationDate)
            cursor.execute(add_book, book_data)

            cnx.commit()

            return "Libro creado exitosamente."

        except sqlite3.Error as err:
            return "Error: {}".format(err)
        finally:
            if 'cnx' in locals() and cnx is not None:
                cursor.close()
                cnx.close()
    @staticmethod
    def read_books():
        try:
            cnx = sqlite3.connect('librotekaDB.db')
            cursor = cnx.cursor()

            cursor.execute("SELECT * FROM books")
            books = cursor.fetchall()

            # Creating Book instances for better display
            book_instances = [Book(*book) for book in books]

            return book_instances

        except sqlite3.Error as err:
            print("Error:", err)
        finally:
            if 'cnx' in locals() and cnx is not None:
                cursor.close()
                cnx.close()



    @staticmethod
    def update_book(book_id, title, author, disponibilidad, price, sinopsis, editorial, ISBN, num_paginas, idioma, formato, clasificacion, publicationDate):
        try:
            cnx = sqlite3.connect('librotekaDB.db')
            cursor = cnx.cursor()

            update_book = (
                "UPDATE books SET "
                "title=?, author=?, disponibilidad=?, price=?, sinopsis=?, editorial=?, ISBN=?, num_paginas=?, idioma=?, formato=?, clasificacion=?, publicationDate=? "
                "WHERE id=?"
            )

            book_data = (title, author, disponibilidad, price, sinopsis, editorial, ISBN, num_paginas, idioma, formato, clasificacion, publicationDate, book_id)

            print("Executing SQL:", update_book)
            print("Data:", book_data)

            cursor.execute(update_book, book_data)

            cnx.commit()

            return "Libro actualizado exitosamente."

        except sqlite3.Error as err:
            print("Error:", err)
        finally:
            if 'cnx' in locals() and cnx is not None:
                cursor.close()
                cnx.close()

    @staticmethod
    def delete_book(book_id):
        try:
            cnx = sqlite3.connect('librotekaDB.db')
            cursor = cnx.cursor()

            delete_book = "DELETE FROM books WHERE id=?"

            cursor.execute(delete_book, (book_id,))

            cnx.commit()

            return "Libro eliminado exitosamente."

        except sqlite3.Error as err:
            print("Error:", err)
        finally:
            if 'cnx' in locals() and cnx is not None:
                cursor.close()
                cnx.close()
        
if __name__ == "__main__":
    while True:
        print("\nOpciones:")
        print("1. Crear libro")
        print("2. Leer libros")
        print("3. Actualizar libro")
        print("4. Eliminar libro")
        print("5. Salir")
        choice = input("Selecciona una opción: ")


        if choice == "1":
            title = input("Título: ")
            author = input("Autor: ")
            disponibilidad = input("Disponibilidad: ")
            price = input("Precio: ")
            sinopsis = input("Sinopsis: ")
            editorial = input("Editorial: ")
            ISBN = input("ISBN: ")
            num_paginas = input("Número de páginas: ")
            idioma = input("Idioma: ")
            formato = input("Formato: ")
            clasificacion = input("Clasificación: ")
            publicationDate = input("Fecha de publicación: ")

            result = BookCRUD.create_book(title, author, disponibilidad, price, sinopsis, editorial, ISBN, num_paginas, idioma, formato, clasificacion, publicationDate)
            print(result)
            
        elif choice == "2":
            books = BookCRUD.read_books()
            for book in books:
                print(f"ID: {book.id}, Título: {book.title}, Autor: {book.author}, ISBN: {book.ISBN}")

        elif choice == "3":
            book_id = int(input("ID del libro a actualizar: "))
            if 0 <= book_id < len(books):
                title = input("Nuevo título: ")
                author = input("Nuevo autor: ")
                disponibilidad = input("Nueva disponibilidad: ")
                price = input("Nuevo precio: ")
                sinopsis = input("Nueva sinopsis: ")
                editorial = input("Nueva editorial: ")
                ISBN = input("Nuevo ISBN: ")
                num_paginas = input("Nuevo número de páginas: ")
                idioma = input("Nuevo idioma: ")
                formato = input("Nuevo formato: ")
                clasificacion = input("Nueva clasificación: ")
                publicationDate = input("Nueva fecha de publicación: ")

                result = BookCRUD.update_book(book_id, title, author, disponibilidad, price, sinopsis, editorial, ISBN, num_paginas, idioma, formato, clasificacion, publicationDate)
                print(result)
            else:
                print("ID de libro no válido.")
           
        elif choice == "4":
            book_id = int(input("ID del libro a eliminar: "))
            result = BookCRUD.delete_book(book_id)
            print(result)
            
        elif choice == "5":
            break    
