from models.book import Book

class BookCRUD:
    @staticmethod
    def create_book(title, author, disponibilidad, price, sinopsis, editorial, ISBN, num_paginas, idioma, formato, clasificacion, publicationDate):
        new_book = Book(title, author, disponibilidad, price, sinopsis, editorial, ISBN, num_paginas, idioma, formato, clasificacion, publicationDate)
        Book.books.append(new_book)
        return "Libro creado exitosamente."