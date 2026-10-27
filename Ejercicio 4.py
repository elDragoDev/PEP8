class Persona:
    def __init__(self,nombre,documento,edad):
        self.nombre = nombre
        self.documento = documento
        self.edad = edad

    def MostrarDatos(self):
        print(self.__dict__.items())

    def Presentarse(self):
        print(f"Hola 👋. Mi nombre es {self.nombre}")

# clases hijas
class Aprendiz(Persona):
    def __init__(self, nombre, documento, edad,ficha):
        self.ficha = ficha
        super().__init__(nombre, documento, edad)

    # Metodo propio
    def Estudiar(self):
        print(f"{self.nombre} esta estudiando📖. Guarda silencio🤫")

# objeto de la clase hija
Estuidante= Aprendiz(
    nombre="Juan",
    documento="10456782112",
    edad= "20 años",
    ficha="3387711"
)
# Uso de los metodos y metodo propio
Estuidante.MostrarDatos()
Estuidante.Presentarse()
Estuidante.Estudiar()

# 2da clase hija
class Instructor(Persona):
    def __init__(self, nombre, documento, edad,especialidad):
        self.especialidad = especialidad
        super().__init__(nombre, documento, edad)

    # su metodo propio
    def Orientar(self):
        print(f"La formacion esta a cargo de {self.nombre}.Prestemos atencion🤫📖")

# objeto de la 2da clase hija
Profe = Instructor(
    nombre="Maira",
    documento="100678312",
    edad="30 años",
    especialidad="Base de Datos"
)
# 2da clase hija usando los metodos y su metodo propio
Profe.MostrarDatos()
Profe.Presentarse()
Profe.Orientar()

# 3ra clase hija
class Coordinador(Persona):
    def __init__(self, nombre, documento, edad,centro_cargo):
        self.centro = centro_cargo
        super().__init__(nombre, documento, edad)

    # metodo propio
    def coordinar(self):
        print(f"{self.nombre} esta a cargo del centro {self.centro}")

# objeto de la 3ra clase hija
Jefe= Coordinador(
    nombre="Yuli",
    documento="1903458765",
    edad="36 años",
    centro_cargo= input("su centro a cargo es: ")
)
# 3ra clase hija usando los metodos y su metodo propio
Jefe.MostrarDatos()
Jefe.Presentarse()
Jefe.coordinar()