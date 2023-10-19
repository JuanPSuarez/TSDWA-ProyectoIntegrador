from models.book import Book

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

        
