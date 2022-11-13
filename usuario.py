class Usuario:

    def __init__(self, nombre, apellido, email, fecha_nac, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.fecha_nac = fecha_nac
        self.dni = dni
    
    def __str__(self):
        cadena = "\nNombre: " + self.nombre
        cadena += "\nApellido: " + self.apellido
        cadena += "\nEmail: " + self.email
        cadena += "\nFecha de Nacimiento: " + str(self.fecha_nac)
        cadena += "\nDNI: " + str(self.dni)
        return cadena

usuario = Usuario("Olivia", "Luna", "olivia@gmail.com", 1, 123)
print(usuario)