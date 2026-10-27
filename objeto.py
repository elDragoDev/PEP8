class centinel:
    def __init__(self,municion=100,calibre="9mm",nivel=2,alcance=20,daño=10,vida=200,disparo="automatico"):
        self.municion=municion
        self.calibre=calibre
        self.nivel=nivel
        self.alcance=alcance
        self.daño=daño
        self.vida=vida
        self.disparo=disparo

    def disparar(self,objetivo):
        print(f"centinel dispara {self.disparo},cargador:{self.municion},calibre usado:{self.calibre} a un zombie")
        objetivo.vida=objetivo.vida - self.daño
        print(f"Impacto a zombie. Vida restante del zombie: {objetivo.vida}")
        return centinel
    


class zombie:
    def __init__(self,vida=150,nivel=2,daño=20,velocidad=10):
        self.vida=vida
        self.nivel=nivel
        self.daño=daño
        self.velocidad=velocidad
    def correr(self):
        print(f"zombie corre a {self.velocidad} metros")
    
    def atacar(self,objetivo):
        objetivo.vida=objetivo.vida - self.daño
        print(f"zombie lanza zarpazo {self.daño}")
        print(f"Impacto a la torreta. Vida restante de la torreta: {objetivo.vida}")

    


torreta= centinel()
un_zombie= zombie()

# inicio del combate
un_zombie.correr()
print("-" * 40)

# La torreta le dispara dos veces mientras se acerca
torreta.disparar(un_zombie)
torreta.disparar(un_zombie)
print("-" * 40)

# El zombie llega a la torreta y la ataca
un_zombie.atacar(torreta)
print("-" * 40)

# La torreta vuelve a defenderse
torreta.disparar(un_zombie)

# El zombie ataca de nuevo
un_zombie.atacar(torreta)
print("-"*40)

# torreta ataca dos veces 
torreta.disparar(un_zombie)
torreta.disparar(un_zombie)
print("-" * 40)

# El zombie ataca de nuevo
un_zombie.atacar(torreta)
print("-"*40)

# torreta ataca dos veces 
torreta.disparar(un_zombie)
torreta.disparar(un_zombie)
print("-" * 40)

# El zombie ataca de nuevo
un_zombie.atacar(torreta)
print("-"*40)

# se despliega una torreta nueva
print("se usaron los 1000 dolares exitosamente.Nueva torreta desplegada")
torreta2=centinel()
torreta2.disparar(un_zombie)

# segunda torreta y primera atacan
torreta.disparar(un_zombie)
torreta.disparar(un_zombie)
# El zombie ataca de nuevo
un_zombie.atacar(torreta)
print("-"*40)
# torreta 2 sigue disparando
torreta2.disparar(un_zombie)
torreta2.disparar(un_zombie)
torreta2.disparar(un_zombie)

# segunda torreta mata a zombie
torreta2.disparar(un_zombie)
torreta2.disparar(un_zombie)
print("zombie elimindo.preparate para la siguiente ronda")

print("dinero disponible: 2000 dolares")
print("\n--- FIN DE LA RONDA ---")