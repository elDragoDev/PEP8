class Vehiculos:
    def __init__(self, identificador, manejo, velocidad, peso, encendido=False):
        self.identificador = identificador
        self.manejo = manejo
        self.velocidad = velocidad
        self.peso = peso
        self.encendido = encendido

    def encender(self):
        self.encendido = True
        print(f"{self.identificador} esta prendido⚡")

    def manejar(self):
        if not self.encendido:
            print("debes encender el vehiculo primero")
            self.encender()
        else:
            print("listo para manejar. Acelera poco a poco")

    def acelerear(self):
        print("aumentando velocidad gradualmente")


class Auto(Vehiculos):
    def __init__(self, identificador, manejo, velocidad, peso, motor):
        self.motor = motor
        super().__init__(identificador, manejo, velocidad, peso)

    def manejar(self):
        return super().manejar()

    def MostrarInfo(self):
        print(self.__dict__.items())

    def AbrirCapó(self):
        print("abriste el capo")

    def CerrarCapó(self):
        print("cerrastes el capo")


carro = Auto(
    identificador=input("digite la placa: "),
    manejo="deportivo",
    velocidad="200km/h",
    peso="700kg",
    motor="v4",
)
carro.MostrarInfo()
carro.manejar()
carro.acelerear()
carro.AbrirCapó()
carro.CerrarCapó()

# class Avion(Vehiculos):
#     def manejar(self):
#         return super().manejar()

# Boing = Avion(identificador=input("digiete la referencia: "),manejo="turbina",velocidad="1000-2500k/h",peso="1-2T")

# Boing.manejar()


class Moto(Vehiculos):
    def __init__(self, identificador, manejo, velocidad, peso, cilindraje):
        self.cilindraje = cilindraje
        super().__init__(identificador, manejo, velocidad, peso)

    def manejar(self):
        return super().manejar()

    def Caballito(self):
        print("la moto esta avanzando en 1 ruerda😎")

    def MostrarInfo(self):
        print(self.__dict__.items())


KawasakiNinja = Moto(
    identificador=input("digite la placa: "),
    manejo="deportivo",
    velocidad="300km/h",
    peso="200kg",
    cilindraje="998cc",
)
KawasakiNinja.MostrarInfo()
KawasakiNinja.manejar()
KawasakiNinja.acelerear()
KawasakiNinja.Caballito()
