import tkinter as tk

contraseña = "123"
usuario = "mia"

#GENERAMOS UNA VENTANA
ventana = tk.Tk()
ventana.title("Saludar") #Titulo de la ventana
ventana.geometry("400x300")

#FUNCION
def login():
    nombre_2 = name.get()
    contraseña_2 = password.get()
    if nombre_2 == usuario and contraseña == contraseña_2:
        saludo["text"] = "Acceso concedido"
    else:
        saludo["text"] = "Usuario o contraseña incorrectos"

#TITULO
etiqueta = tk.Label(text = "Nombre")
etiqueta.pack()

#ENTRADA DE DATOS
name = tk.Entry()
name.pack()

#TITULO
etiqueta = tk.Label(text = "Contraseña")
etiqueta.pack()

#ENTRADA DE DATOS
password = tk.Entry()
password.pack()

#BOTON: Le asignamos una funcion "saludar" con commmand
button = tk.Button(text = "Saludar", command = login)
button.pack()

saludo = tk.Label(text = "")
saludo.pack()

tk.mainloop()