class Book:
     books = [] 
     
     def __init__(self, title, author, disponibilidad, price, sinopsis, editorial, ISBN, num_paginas, idioma, formato, clasificacion, publicationDate):
        self.title = title
        self.author = author
        self.disponibilidad = disponibilidad
        self.price = price
        self.sinopsis = sinopsis
        self.editorial = editorial
        self.ISBN = ISBN
        self.num_paginas = num_paginas
        self.idioma = idioma
        self.formato = formato
        self.clasificacion = clasificacion
        self.publicacionDate = publicationDate