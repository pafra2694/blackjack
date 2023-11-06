import random

#**************CLASE CARTA*********************
class Carta:
  def __init__(self, valor, palo):
    self.valor = valor
    self.palo = palo
  def __repr__(self):
    return "{valor} de {palo}".format(valor=self.valor,palo=self.palo)

#*************CLASE BARAJA*********************
class Baraja:
  def __init__(self):
    valor_cartas = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10,'J', 'Q', 'K']
    palo_cartas = ["Corazones", "Diamantes", "Picas", "Treboles"]
    lista_cartas = []
    for elemento_valor in valor_cartas:
      for elemento_palo in palo_cartas:
        nueva_carta = Carta(elemento_valor,elemento_palo)
        lista_cartas.append(nueva_carta)
    self.cartas = lista_cartas

  def __repr__(self):
    return "Baraja con {} cartas".format(len(self.cartas))

  #***********barajea cartas
  def barajear(self):
    random.shuffle(self.cartas)

  #************imprime las cartas de la baraja
  def mostrar(self):
    print(self.cartas)
  
  #*************regresa la última carta de la baraja*****
  def repartir(self):
    return self.cartas.pop()

  #********reinicia la baraja**********
  def reiniciar(self):
    self.__init__()

#**************CLASE JUGADOR**********************
class Jugador:
  def __init__(self, nombre):
    self.nombre = nombre
    self.mano = []
    self.puntuacion = 0
  
  def __repr__(self):
    cadenas = [str(objeto) for objeto in self.mano]
    manoComas = ', '.join(cadenas)

    if len(self.mano) == 0:
      return "{nombre} no tiene una mano aún".format(nombre=self.nombre)
    else:
      return "{nombre} tiene la siguiente mano:\n{mano}.".format(nombre=self.nombre,mano=manoComas)

  def agregar_carta(self,carta):
    self.mano.append(carta)

  #*******calcula puntuacion y la regresa como entero****
  def calcular_puntuacion(self):
    self.puntuacion = 0
    for elemento in self.mano:
      if elemento.valor == "K" or elemento.valor == "Q" or elemento.valor == "J":
        self.puntuacion += 10
      elif elemento.valor == "A":
        puntaje = int(input("{jugador} tiene A, quieres que valga 1 o 10? Teclea tu decision:\n 1. 1\n 2. 11\n".format(jugador=self.nombre)))
        if puntaje == 2:
            puntaje = 11
        elif puntaje != 1:
            print("opcion no permitida, se contará como 1")
            puntaje = 1
        self.puntuacion += int(puntaje)
      else:
        self.puntuacion += elemento.valor
    return self.puntuacion

def comenzarJuego():
        baraja = Baraja()
        baraja.barajear()
        resultados = []
        numeroJugadores = int(input("ingrese el número de jugadores: "))
        jugadores = []
        for i in range(numeroJugadores):
            #nombresJugadores.append()
            jugadores.append(Jugador(input("Ingrese el nombre del jugador número {}:".format(str(i+1)))))
        casa = Jugador("La casa")
        jugadores.append(casa)
        print("\nRepartiendo la primera tanda de cartas...")
        for i in range(2):
            for jugador in jugadores:
                jugador.agregar_carta(baraja.repartir())
        
        for jugador in jugadores:
            print(jugador)

        for jugador in jugadores:
            print("Turno de {}:".format(jugador.nombre))
            agregar = "1"
            while agregar == "1":
                agregar = input("Tienes {puntaje} puntos actualmente, deseas agregar otra carta (1) a tu mano o terminar turno (2)?".format(puntaje = jugador.calcular_puntuacion()))
                if agregar == "1":
                    jugador.agregar_carta(baraja.repartir())
                    print(jugador)
                else:
                    agregar = "2"
                    resultados.append(21-jugador.puntuacion)

        print("\n************Resultados del juego************")        
        puntajeCasa = 21 - jugadores[-1].puntuacion
        puntosCasa = jugadores[-1].puntuacion
        jugadores.pop()
        for jugador in jugadores:
            puntaje = 21 - jugador.puntuacion
            if puntaje < 0:
                print("{jugador} perdió por sobrepasar los 21 puntos con {puntaje} puntos en su mano".format(jugador = jugador.nombre, puntaje=jugador.puntuacion))
            elif puntaje == puntajeCasa:
                print("{jugador} ha empatado con la casa con 21 puntos. No hay ganancia".format(jugador=jugador.nombre))
            elif puntaje >= 0 and puntajeCasa > 0:
                if puntaje < puntajeCasa:
                    print("{jugador} le ha ganado a la casa con {puntaje} puntos contra {puntajeCasa}. Felicidades!".format(jugador=jugador.nombre, puntaje=jugador.puntuacion, puntajeCasa=puntosCasa))
                else:
                    print("{jugador} ha perdido contra la casa con {puntaje} puntos contra {puntajeCasa}. Lo siento".format(jugador=jugador.nombre, puntaje=jugador.puntuacion, puntajeCasa=puntosCasa))
            elif puntaje >= 0 and puntajeCasa < 0:
                print("{jugador} le ha ganado a la casa con {puntaje} puntos contra {puntajeCasa}. Felicidades!".format(jugador=jugador.nombre, puntaje=jugador.puntuacion, puntajeCasa=puntosCasa))
juegoNuevo = "1"
while juegoNuevo != "2":
    juegoNuevo = input("\nDesea iniciar un nuevo juego de blackjack (1) o salir (2)?\n")
    if juegoNuevo == "1":
        comenzarJuego()
    elif juegoNuevo == "2":
        break
    else:
        print("Opción incorrecta intente nuevamente")

    
        


