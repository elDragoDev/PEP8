# creamos clase padre
class Producto:
    def __init__(self,nombre,precio,codigo):
        self.nombre = nombre
        self.precio = precio
        self.codigo = codigo

    def Mostrar_Producto(self):
        print(f"{self.nombre} es el numero: {self.codigo}")

    def Calcular_Precio(self):
        print(f"cada {self.nombre} cuesta: {self.precio}")

#creamos las clases hijas
class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, codigo,garantia):
        self.garantia = garantia
        super().__init__(nombre, precio, codigo)

    #metodo propio de la clase hija
    def mostrar_garantia(self):
        print(f"{self.nombre} posee una garantia de {self.garantia}")

class ProductoAlimenticio(Producto):
    def __init__(self, nombre, precio, codigo,fechaVencimiento):
        self.fechaVencimiento = fechaVencimiento
        super().__init__(nombre, precio, codigo)

    def verificar_vencimiento(self):
        print(f"{self.nombre} caducara en {self.fechaVencimiento}")

class Ropa(Producto):
    def __init__(self, nombre, precio, codigo, talla):
        self.talla = talla
        super().__init__(nombre, precio, codigo)

    def CambiarTalla(self):
        print(f"{self.nombre} esta pequeña. Nesesito talla {self.talla} para que sea optima para mi")

computador = ProductoElectronico(
    nombre= "portatil HP",
    precio= "2,500.000",
    codigo= "ELE001",
    garantia= "12 meses"
) 
computador.Mostrar_Producto()
computador.mostrar_garantia()
computador.Calcular_Precio()

celular = ProductoElectronico(
    nombre= "Samsumg S24 Ultra",
    precio= "1,800.000",
    codigo= "ELE002",
    garantia= "12 meses"
)

celular.Mostrar_Producto()
celular.mostrar_garantia()
celular.Calcular_Precio()

leche = ProductoAlimenticio(
    nombre= "Leche alpina",
    precio= "4.500",
    codigo= "ALI001",
    fechaVencimiento= "2026-10-15"
)

leche.Mostrar_Producto()
leche.Calcular_Precio()
leche.verificar_vencimiento()

arroz = ProductoAlimenticio(
    nombre="Arroz Diana",
    precio="3.800",
    codigo="ALI002",
    fechaVencimiento="2026-12-20"
)

arroz.Mostrar_Producto()
arroz.Calcular_Precio()
arroz.verificar_vencimiento()