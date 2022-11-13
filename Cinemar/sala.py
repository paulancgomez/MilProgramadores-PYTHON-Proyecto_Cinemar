class Sala:

    def __init__(self, id_sala, numero, formato, capacidad) -> None:
        self.id_sala = id_sala
        self.numero = numero
        self.formato = formato
        self.capacidad = capacidad

    def __str__(self):
        cadena = "\nId: " + str(self.sala)
        cadena += "\nNumero: " + str(self.numero)
        cadena += "\nFormato: " + self.formato
        cadena += "\nCapacidad: " + str(self.capacidad)

sala = Sala(1, 14, "Bla bla", 100)
print(sala)