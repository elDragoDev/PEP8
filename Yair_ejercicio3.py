class Producto:
        def __init__(self,nombre,precio,codigo):
            self.nombre = nombre
            self.precio = precio
            self.codigo = codigo

        def mostrar_producto(self):
            print(self.__dict__.items())

        def calcular_precio(self):
             print(f"cada {self.nombre} cuesta {self.precio}")

class ProductoElectronico(Producto):
         def __init__(self, nombre, precio, codigo,garantia):
          self.garantia = garantia
          super().__init__(nombre, precio, codigo)

         def mostrar_garantia(self):
          print(f"la garantia de {self.nombre} vence en {self.garantia}")

class ProductoAlimenticio(Producto):
         def __init__(self, nombre, precio, codigo,vencimiento):
              self.vencimiento = vencimiento
              super().__init__(nombre, precio, codigo)

         def mostrar_vencimiento(self):
              print(f"{self.nombre} vence {self.vencimiento}")

        
class Ropa(Producto):
     def __init__(self, nombre, precio, codigo,talla):
          self.talla = talla
          super().__init__(nombre, precio, codigo)

     def cambiar_talla(self):
          print(f"la {self.talla} no era tu tipo. Se cambio a una acorde")

portatil = ProductoElectronico(
     nombre = "portatil HP",
     precio= "2,800.000 COP",
     codigo= "ELE001",
     garantia= "12 meses"
)

portatil.mostrar_producto()
portatil.mostrar_garantia()
portatil.calcular_precio()

pasta = ProductoAlimenticio(
     nombre = "Doria",
     precio= "2.500",
     codigo= "ALI001",
     vencimiento= "21/septiembre/2030"
)

pasta.mostrar_producto()
pasta.mostrar_vencimiento()
pasta.calcular_precio()

camisa = Ropa(
     nombre= "Prada",
     precio= "60.000",
     codigo= "ROP001",
     talla= "talla M"
)

camisa.mostrar_producto()
camisa.calcular_precio()
camisa.cambiar_talla()