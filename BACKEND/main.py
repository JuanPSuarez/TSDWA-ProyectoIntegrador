from models.user import User
from models.shopping_cart import Shopping_Cart
from models.order import Order
from models.book import Book
from models.author import Author
from models.genre import Genre
from models.relationship import Relationship



if __name__ == "__main__":
    customer1 = User("123", "password123", "active", "2023-09-18")
    shopping_cart1 = Shopping_Cart(1, "Sample Cart", 5, 149.95, "2023-09-18")