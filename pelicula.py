class Pelicula:

    def __init__(self, id, nombre, sinopsis, reparto, duracion, genero, tipo, clasificacion):
        self.id = id
        self.nombre = nombre
        self.sinopsis = sinopsis
        self.reparto = reparto
        self.duracion = duracion
        self.genero = genero
        self.tipo = tipo
        self.clasificacion = clasificacion
    
    def __str__(self):
        cadena = "\nId: " + str(self.id)
        cadena += "\nNombre: " + self.nombre
        cadena += "\nSinopsis: " + self.sinopsis
        cadena += "\nReparto: " + self.reparto
        cadena += "\nDuración: " + str(self.duracion)
        cadena += "\nGénero: " + self.genero
        cadena += "\nTipo: " + self.tipo
        cadena += "\nClasificación: " + self.clasificacion  
        return cadena

pelicula = Pelicula(1, "Avatar", "Lorem", "Brad Pitt", 120, "Ciencia-Ficción", "Nose", "Muy Bueno")
print(pelicula)