# 1. Definimos la plantilla (Clase)
class Animal:
    def __init__(self, nombre, color, edad, hambre=True, sonido=False):
        self.nombre= nombre
        self.color = color
        self.__hambre = hambre
        self.sonido = sonido
        self.edad = edad
    def dormir(self):
            print(f"{self.nombre} esta durmiendo...ZZZ No lo despiertes")
    
    def comer(self):
            self.__hambre=False
            print(f"{self.nombre} esta lleno")
    
    def jugar(self):
        if self.__hambre == False:
            print(f"{self.nombre} esta jugando contigo😍")
        else:
            print(f"{self.nombre} esta muy hambriento para jugar ahora :( , Alimentalo!😡")

    def hambriento(self):
         """Getter: Devuelve valor del atributo privado"""
         return self.__hambre

    def HacerSonido(self):
         self.sonido=True
         if not self.sonido:
            print(f"{self.nombre} esta haciendo un sonido")

    def MostrarDatos(self):
         print(self.__dict__.items())

class Gato(Animal):
    def __init__(self, nombre, color, edad, casero=False):
          super().__init__(nombre, color, edad)
          self.casero=casero

    def CambioEstado(self):
         self.casero = True

    def adoptar(self):
        if  self.casero:
            print("adoptastes al gatito😍")
        else:
             print("no posee dueño aun😔")
        
     
    def HacerSonido(self):
          print(f"{self.nombre} dice Miau!")
          
     
class Perro(Animal):
     def __init__(self,nombre,color,edad,raza):
        super().__init__(nombre,color,edad)
        self.raza= raza

     def HacerSonido(self):
          print(f"{self.nombre} dice Woof!")

class Ave(Animal):
     def __init__(self, nombre, color, edad, tipo_alado, hambre=True, sonido=False):
                    self.alado = tipo_alado
                    super().__init__(nombre, color, edad)

     def volar(self):
          print(f"{self.nombre} esta volando")

class Elefante(Animal):
     def __init__(self, nombre, color, peso,edad):
          super().__init__(nombre, color,edad)
          self.peso = peso
        

# 2. Creación de un objeto (Instanciación)
mi_gato = Gato(nombre=input("dame un nombre: "),color=input("dime su color: "),edad="4 años")

mi_perro= Perro(nombre= input("dame un nombre para el perro: "),
                color=input("dame un color para el perro: "),raza=input("dame su raza: "),edad="2 años")

elefante = Elefante(nombre=input("dame un nombre: "),color="gris",peso= "2T",edad= "16 años")

Loro = Ave(
     nombre= "Julian",
     color= "Azul,rojo y amarillo",
     edad= "2 años",
     tipo_alado= "tropical"
)

# 3. Metodos de los objetos
print(mi_gato.nombre)
mi_gato.MostrarDatos() 
mi_gato.dormir()
print(f"esta hambriento? {mi_gato.hambriento()}")
mi_gato.jugar()
mi_gato.comer()
mi_gato.jugar()
mi_gato.HacerSonido()
print(mi_gato.casero)
mi_gato.adoptar()
mi_gato.CambioEstado()
mi_gato.adoptar()

mi_perro.MostrarDatos()
print(mi_perro.nombre)
print(mi_perro.raza)
mi_perro.dormir()
mi_perro.jugar()
mi_perro.comer()
mi_perro.jugar()
mi_perro.HacerSonido()

Loro.MostrarDatos()
Loro.dormir()
Loro.jugar()
Loro.comer()
Loro.jugar()
Loro.volar()

elefante.MostrarDatos()
elefante.dormir()
elefante.comer()
elefante.HacerSonido()