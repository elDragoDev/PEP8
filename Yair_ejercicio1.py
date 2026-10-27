class vehiculo:
        def __init__(self,marca,modelo,velocidad):
                self.marca = marca
                self.modelo = modelo
                self.velocidad = velocidad

        def Mostrar_informacion(self):
                print(self.__dict__.items())

        def acelerar(self):
                print(f"aumentando de 0 a {self.velocidad}km/h.")

class auto(vehiculo):
        def __init__(self, marca, modelo, velocidad,numero_puertas):
                self.numero_puertas = numero_puertas
                super().__init__(marca, modelo, velocidad)

        def tocar_bocina(self):
                print("bing biing🔊")

carro = auto(
        marca= "Toyota",
        modelo= "4x4",
        velocidad= "120km/h",
        numero_puertas= "4"
)

carro.Mostrar_informacion()
carro.acelerar()
carro.tocar_bocina()

class motocicleta(vehiculo):
        def __init__(self, marca, modelo, velocidad,cilindraje):
                self.cilindraje = cilindraje
                super().__init__(marca, modelo, velocidad)

        def caballito(self):
                print("estas andando en 1 rueda. WOW!")

moto = motocicleta(
        marca= "kawasaki",
        modelo= "deportiva",
        velocidad= "100km/h",
        cilindraje= "450cc"
)

moto.Mostrar_informacion()
moto.acelerar()
moto.caballito()