class Animal:
    def __init__(self,nombre,edad,peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def mostrar_datos(self):
        print(self.__dict__.items())

    def comer(self):
        print(f"{self.nombre} esta comiendo")

class Perro(Animal):
    def __init__(self, nombre, edad, peso, raza):
        self.raza = raza
        super().__init__(nombre, edad, peso)

    def ladrar(self):
        print(f"{self.nombre} dice WOOF!")

class Gato(Animal):
    def __init__(self, nombre, edad, peso, color):
        self.color = color
        super().__init__(nombre, edad, peso)

    def maullar(self):
        print(f"{self.nombre} dice MEOW!")

class Ave(Animal):
    def __init__(self, nombre, edad, peso, especie):
        self.especie = especie
        super().__init__(nombre, edad, peso)

    def volar(self):
        print(f"{self.nombre} emprende vuelo")

class reptil(Animal):
    def __init__(self, nombre, edad, peso, longuitud):
        self.longuitud = longuitud
        super().__init__(nombre, edad, peso)

    def mudar_piel(self):
        print(f"{self.nombre} esta mudando de piel")

canino1 = Perro(
    nombre= "Fido",
    edad= "4 años",
    peso= "10kg",
    raza= "Belga"
)

canino1.mostrar_datos()
canino1.comer()
canino1.ladrar()

canino2 = Perro(
    nombre= "Firulais",
    edad= "4 años",
    peso= "10kg",
    raza= "Fresh"
)

canino2.mostrar_datos()
canino2.comer()
canino2.ladrar()

felino1 = Gato(
    nombre= "michito",
    edad= "4 años",
    peso= "4 kg",
    color= "naranja"
)

felino1.mostrar_datos()
felino1.comer()
felino1.maullar()

felino2 = Gato(
    nombre= "Max",
    edad= "6 años",
    peso= "5 kg",
    color= "blanco"
)

felino2.mostrar_datos()
felino2.comer()
felino2.maullar()

pajaro1 = Ave(
    nombre= "weiss",
    edad= "3 años",
    peso= "8 kg",
    especie= "rapaz"
)

pajaro1.mostrar_datos()
pajaro1.comer()
pajaro1.volar()

pajaro2 = Ave(
    nombre= "Boo",
    edad= "3 años",
    peso= "8 kg",
    especie= "tropicales"
)

pajaro2.mostrar_datos()
pajaro2.comer()
pajaro2.volar()

gecko1 = reptil(
    nombre= "helix",
    edad= "6 años",
    peso= "200 gr",
    longuitud= "10 cm"
)

gecko1.mostrar_datos()
gecko1.comer()
gecko1.mudar_piel()

gecko2 = reptil(
    nombre= "flex",
    edad= "5 años",
    peso= "100 kg",
    longuitud= "3 mts"
)

gecko2.mostrar_datos()
gecko2.comer()
gecko2.mudar_piel()