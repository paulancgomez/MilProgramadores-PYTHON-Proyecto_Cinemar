class Tipo:

    def __init__(self, id_tipo, idioma, formato, subtitulada) -> None:
        self.id_tipo = id_tipo
        self.idioma = idioma
        self.formato = formato
        self.subtitulada = subtitulada
    
    def __str__(self):
        cadena = "\nId: " + str(self.id_tipo)
        cadena += "\nIdioma: " + self.idioma
        cadena += "\nFormato: " + self.formato
        cadena += "\nSubtitulada: " + str(self.subtitulada)
        return cadena

genero = Tipo(1, "Español", "Bla bla", True)
print(genero)