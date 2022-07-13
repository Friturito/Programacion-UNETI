from io import open

archivoTexto = open("hola.txt", "r")
print(archivoTexto.read(11))  # Lee hasta el 11
archivoTexto.seek(11)  # Empieza leer a partir del 11
print(archivoTexto.read())
