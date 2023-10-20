from book import Book

class BookCRUD:
    @staticmethod
    def create_book(title, author, disponibilidad, price, sinopsis, editorial, ISBN, num_paginas, idioma, formato, clasificacion, publicationDate):
        new_book = Book(title, author, disponibilidad, price, sinopsis, editorial, ISBN, num_paginas, idioma, formato, clasificacion, publicationDate)
        Book.books.append(new_book)
        return "Libro creado exitosamente."
    
    @staticmethod
    def read_books():
        return Book.books

    @staticmethod
    def update_book(book_id, title, author, disponibilidad, price, sinopsis, editorial, ISBN, num_paginas, idioma, formato, clasificacion, publicationDate):
        if 0 <= book_id < len(Book.books):
            updated_book = Book(title, author, disponibilidad, price, sinopsis, editorial, ISBN, num_paginas, idioma, formato, clasificacion, publicationDate)
            Book.books[book_id] = updated_book
            return "Libro actualizado exitosamente."
        else:
            return "ID de libro no válido."
   
    @staticmethod
    def delete_book(book_id):
        if 0 <= book_id < len(Book.books):
            del Book.books[book_id]
            return "Libro eliminado exitosamente."
        else:
            return "ID de libro no válido."
        
        
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
            for i, book in enumerate(books):
                print(f"ID: {i}, Título: {book.title}")

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
