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