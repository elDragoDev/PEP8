class Persona:
    def __init__(self,nombre,documento,edad):
        self.nombre = nombre
        self.doc = documento
        self.edad = edad

    def Mostrar_datos(self):
        print(self.__dict__.items())

    def saludar(self):
        print(f"{self.nombre} dice hola👋")

    def presentarse(self):
        print(f"{self.nombre} dice que se llama {self.nombre} y su edad es de {self.edad}")

class Aprendiz(Persona):
    def __init__(self, nombre, documento, edad, ficha):
        self.ficha = ficha
        super().__init__(nombre, documento, edad)

    def estudiar(self):
        print(f"{self.nombre} tomo sus apuntes y empezo a estudiarlos")

class Instructor(Persona):
    def __init__(self, nombre, documento, edad, especialidad):
        self.especialidad = especialidad
        super().__init__(nombre, documento, edad)

    def orientar_formacion(self):
        print(f"{self.nombre} empezo su formacion. Escucha y aprende")

class Coordinador(Persona):
    def __init__(self, nombre, documento, edad, area):
        self.area = area
        super().__init__(nombre, documento, edad)

    def coordinar(self):
        print(f"{self.nombre} asigno un nuevo instructor a una ficha")

estudiante = Aprendiz(
    nombre= "Luis",
    documento= "1002264",
    edad= "18 años",
    ficha= "245987"
)

estudiante.Mostrar_datos()
estudiante.saludar()
estudiante.presentarse()
estudiante.estudiar()

instru = Instructor(
    nombre= "Lucas",
    documento= "10224586",
    edad= "30 años",
    especialidad= "Base de Datos"
)

instru.Mostrar_datos()
instru.saludar()
instru.presentarse()
instru.orientar_formacion()

coordinador = Coordinador(
    nombre= "Jhon", 
    documento= "10897634",
    edad= "44 años",
    area= "CBC"
)

coordinador.Mostrar_datos()
coordinador.saludar()
coordinador.presentarse()
coordinador.coordinar()