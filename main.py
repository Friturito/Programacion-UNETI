"""i = 0
while i <= 100:
    print (i)
    i += 1
password = ""
while password != "pedro":
    password = input("Escribe contraseña: ")
    if password != "pedro":
        print("Contraseña incorrecta")

for x in "pedro":
    print(x)
edad = 199
while 0<edad>100:
    print("Escribe tu edad")
    edad = int(input())


def divide (n1=0,n2=0):
    n3 = n1/n2
    return round(n3)
print(divide(int(input("inserta un numero: ")), int(input("inserta otro numero: "))))

def dividir (n1,n2):
    try:
        return n1/n2
    except ZeroDivisionError:
        print ("No se puede dividir entre cero")
        return "Operacion erronea"
    finally:
        print ("Fin del la division")

print(dividir(10,2))
print(dividir(0,0))

def edadCalc(edad):
    if edad < 0:
        raise TypeError("La edad no puede ser menor que 0")
    elif edad < 18:
        print("Eres muy joven para entrar a ver este contenido")
    elif edad > 100:
        print ("irga loco tu lo que estas es viejo, oyo")
    else:
        print("Puedes entrar a la pagina")
"""