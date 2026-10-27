class Empleado:
    def __init__(self,nombre,identificacion,salario):
        self.nombre = nombre
        self.identificacion = identificacion
        self.salario = salario

    def MostrarDatos(self):
        print(self.__dict__.items())

    def Trabajar(self):
        print(f"{self.nombre} esta trabajando")

# creamos las clases hijas

class Desarrollador(Empleado):
    def __init__(self, nombre, identificacion, salario,lenguaje_programacion):
        self.lenguaje= lenguaje_programacion
        super().__init__(nombre, identificacion, salario)

    def Scripting(self):
        print(f"{self.nombre} esta escribiendo codigo. No lo molestes🤫")

class Diseñador(Empleado):
    def __init__(self, nombre, identificacion, salario,herramienta):
        self.herramienta = herramienta
        super().__init__(nombre, identificacion, salario)

    def Decorar(self):
        print(f"{self.nombre} esta decorando la app. ¡Que lindo!😍")

# primer objeto
backend = Desarrollador(
    nombre= input("ingrese el nombre: "),
    identificacion= "1234",
    salario= "5M COP",
    lenguaje_programacion= "Phyton"
)
backend.MostrarDatos()
backend.Trabajar()
backend.Scripting()
# segundo objeto
frontend = Desarrollador(
    nombre= input("ingrese el nombre: "),
    identificacion= "1234",
    salario= "5M COP",
    lenguaje_programacion= "Phyton y HTML"
)
frontend.MostrarDatos()
frontend.Trabajar()
frontend.Scripting()
# tercer objeto
diseñador = Diseñador(
    nombre= input("ingrese el nombre: "),
    identificacion= "29876",
    salario= "4M",
    herramienta= "Paint"
)
diseñador.MostrarDatos()
diseñador.Trabajar()
diseñador.Decorar()