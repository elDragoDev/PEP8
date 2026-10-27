class Empleado:
        def __init__(self,nombre,identificacion,salario):
                self.nombre = nombre
                self.identificacion = identificacion
                self.salario = salario

        def Mostrar_Datos(self):
                print(self.__dict__.items())

        def Trabajar(self):
                print(f"{self.nombre} esta trabajando no lo molestes")

class Desarrollador(Empleado):
        def __init__(self, nombre, identificacion, salario,lenguaje_programacion):
                self.programacion = lenguaje_programacion
                super().__init__(nombre, identificacion, salario)

        def scripting(self):
                print(f"{self.nombre} esta escribiendo codigo")

class Diseñador(Empleado):
        def __init__(self, nombre, identificacion, salario,herramienta):
                self.herramienta = herramienta
                super().__init__(nombre, identificacion, salario)

        def diseñar(self):
                print(f"{self.nombre} esta diseñando")

class Instructor(Empleado):
        def __init__(self, nombre, identificacion, salario,especialidad):
                self.especialidad = especialidad
                super().__init__(nombre, identificacion, salario)

        def orientar(self):
                print(f"{self.nombre} esta dando la formacion ya. Presta atencion")

programador= Desarrollador(
        nombre= "Ricardo",
        identificacion= "10298734",
        salario= "5M de pesos",
        lenguaje_programacion= "Phyton"
)

programador.Mostrar_Datos()
programador.Trabajar()
programador.scripting()

diseñador = Diseñador(
        nombre= "luis",
        identificacion= "1224480",
        salario= "5M de pesos",
        herramienta= "figma"
)

diseñador.Mostrar_Datos()
diseñador.Trabajar()
diseñador.diseñar()

Instru = Instructor(
        nombre= "Diego",
        identificacion= "1228840",
        salario= "8M",
        especialidad= "POO"
)

Instru.Mostrar_Datos()
Instru.Trabajar()
Instru.orientar()