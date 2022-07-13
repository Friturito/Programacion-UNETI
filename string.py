text = "hola wacho como estas"

print(text.capitalize())
print(text.upper())
print(text.lower())

print("--Separador---")

edad = input("Hola, Inserta tu edad: ")

while edad.isdigit()== False:
    print("Porfavor introduce un valor numerico")
    edad = input("Hola, Inserta tu edad: ")

if int(edad)<18:
    print("No puedes pasar")
else:
    print("Mi loco dele pa dentro")
