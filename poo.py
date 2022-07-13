class coche():
    def __init__(self):
        self.__ChasisL = 220
        self.__ChasisA = 120
        self.Ruedas = 4
        self.enMarcha = False

    def arracar(self):
        self.enMarcha = True

    def parar(self):
        self.enMarcha = False

    def getEstado(self):
        if (self.enMarcha):
            return "Coche en marcha"
        else:
            return "Coche estacionado"


miCoche = coche()
miCoche.color = "Rojo"

print(miCoche.color)
print(miCoche.getEstado())
miCoche.arracar()
print(miCoche.getEstado())
miCoche2 = coche()

print("POO - Herencia")
class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.arranca = False
        self.frena = False
        self.acelera = False

    def arrancar(self):
        self.arranca = True

    def acelerar(self):
        self.acelera = True

    def frena(self):
        self.frena = True

    def getEstado(self):
        print("Marca: ", self.marca, "Modelo: ", self.modelo, "Arracar estado:", self.arranca, "Frena estado",
                  self.frena)

class Moto(Vehiculo):
    hCaballito = "Manejar"
    def caballito(self):
        self.hCaballito = "Estoy haciendo caballito ayaju"
    def getEstado(self):
        print("Marca: ", self.marca, "Modelo: ", self.modelo, "Arracar estado:", self.arranca, "Frena estado",
                  self.frena,"Ahorita estoy haciendo " , self.hCaballito)
Motomami = Moto("Motomami sordo","Nose pero es motomami chamo")
Motomami.caballito()
Motomami.getEstado()