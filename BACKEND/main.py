from models.user import User
from models.shopping_cart import Shopping_Cart
from models.order import Order
from models.book import Book
from config import host, database, user, password

def get_book_input():
    title = input("Título del libro: ")
    author = input("Autor del libro: ")
    genre = input("Género del libro: ")
    description = input("Descripción del libro: ")
    publicationDate = input("Fecha de publicación del libro: ")
    price = float(input("Precio del libro: "))
    stock = int(input("Cantidad en stock: "))
    return title, author, genre, description, publicationDate, price, stock

# Función para mostrar una lista de libros
def list_books(books):
    print("Lista de libros:")
    for book in books:
        print(f"ID: {book[0]}, Título: {book[1]}")

# Función principal
def main():
    while True:
        print("\nOpciones:")
        print("1. Agregar libro")
        print("2. Listar libros")
        print("3. Editar libro")
        print("4. Eliminar libro")
        print("5. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            title, author, genre, description, publicationDate, price, stock = get_book_input()
            result = Book.create_book(title, author, genre, description, publicationDate, price, stock)
            print(result)
        elif option == "2":
            books = Book.read_books()
            list_books(books)
        elif option == "3":
            book_id = int(input("ID del libro a editar: "))
            new_title, new_author, new_genre, new_description, new_publicationDate, new_price, new_stock = get_book_input()
            result = Book.update_book(book_id, new_title, new_author, new_genre, new_description, new_publicationDate, new_price, new_stock)
            print(result)
        elif option == "4":
            book_id = int(input("ID del libro a eliminar: "))
            result = Book.delete_book(book_id)
            print(result)
        elif option == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()
