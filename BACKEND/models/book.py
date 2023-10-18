class Book:
    books = []  

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
        new_book = Book(title, author, genre, description, publicationDate, price, stock)
        Book.books.append(new_book)
        return "Libro creado exitosamente."

    @staticmethod
    def read_books():
        return Book.books

    @staticmethod
    def update_book(book_id, title, author, genre, description, publicationDate, price, stock):
        if 0 <= book_id < len(Book.books):
            updated_book = Book(title, author, genre, description, publicationDate, price, stock)
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
            genre = input("Género: ")
            description = input("Descripción: ")
            publicationDate = input("Fecha de publicación: ")
            price = input("Precio: ")
            stock = input("Stock: ")
            result = Book.create_book(title, author, genre, description, publicationDate, price, stock)
            print(result)

        elif choice == "2":
            books = Book.read_books()
            for i, book in enumerate(books):
                print(f"ID: {i}, Título: {book.title}")

        elif choice == "3":
            book_id = int(input("ID del libro a actualizar: "))
            if 0 <= book_id < len(Book.books):
                title = input("Nuevo título: ")
                author = input("Nuevo autor: ")
                genre = input("Nuevo género: ")
                description = input("Nueva descripción: ")
                publicationDate = input("Nueva fecha de publicación: ")
                price = input("Nuevo precio: ")
                stock = input("Nuevo stock: ")
                result = Book.update_book(book_id, title, author, genre, description, publicationDate, price, stock)
                print(result)
            else:
                print("ID de libro no válido.")

        elif choice == "4":
            book_id = int(input("ID del libro a eliminar: "))
            result = Book.delete_book(book_id)
            print(result)

        elif choice == "5":
            break

