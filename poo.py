class coche():
    def __init__(self):
        self.__ChasisL=220
        self.__ChasisA= 120
        self.Ruedas = 4
        self.enMarcha = False
    

    def arracar (self):
        self.enMarcha = True

    def parar (self):
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
miCoche2= coche()
