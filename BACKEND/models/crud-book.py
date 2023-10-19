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
