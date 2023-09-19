class User:
    def __init__(self, userId, password, status, registerDate):
        self.userId = userId
        self.password = password
        self.status = status
        self.registerDate = registerDate

    def verifyLogin(self):
        pass


class Costumer(User):
    def __init__(self, costumerId, email, dni, telephone, suscription):
        super().__init__(costumerId, "", "", None)
        self.email = email
        self.dni = dni
        self.telephone = telephone
        self.suscription = suscription

    def register(self):
        pass

    def login(self):
        pass

    def recoverpassword(self):
        pass


class Admin(User):
    def __init__(self, adminName, email):
        super().__init__("", "", "", None)
        self.adminName = adminName
        self.email = email

    def updateCat(self):
        pass


class Shopping_Cart:
    def __init__(self, cartId, title, quantity, totalPurchase, dateAdded):
        self.cartId = cartId
        self.title = title
        self.quantity = quantity
        self.totalPurchase = totalPurchase
        self.dateAdded = dateAdded

    def addCartItem(self):
        pass

    def updateQuantity(self):
        pass

    def viewCartDetails(self):
        pass

    def checkOut(self):
        pass


class Order:
    def __init__(self, idOrder, costumerId, cartId, status):
        self.idOrder = idOrder
        self.costumerId = costumerId
        self.cartId = cartId
        self.status = status

    def placeOrder(self):
        pass


class Book:
    def __init__(self, title, author, genre, description, publicationDate, price, stock):
        self.title = title
        self.author = author
        self.genre = genre
        self.description = description
        self.publicationDate = publicationDate
        self.price = price
        self.stock = stock


class Author:
    def __init__(self, idAuthor, author):
        self.idAuthor = idAuthor
        self.author = author


class Genre:
    def __init__(self, idGenre, genre):
        self.idGenre = idGenre
        self.genre = genre


class Relationship:
    def __init__(self, source, target):
        self.source = source
        self.target = target


if __name__ == "__main__":
    # You can create instances of the classes and use their methods as needed.
    customer1 = Costumer("123", "customer@example.com", "123456789", "555-555-5555", True)
    admin1 = Admin("Admin1", "admin@example.com")
    book1 = Book("Sample Book", "John Doe", "Fiction", "A sample book description.", "2023-01-01", 29.99, 100)
