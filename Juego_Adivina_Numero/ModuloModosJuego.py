from MenuDificultades import Dificultad
from MenuDificultades import SubDificultades as Sd
from AdivinarNumero import AdivinarNumeroSolitario as ANS
from AdivinarNumero import AdivinarNumeroDosJugadores as ANDJ
from AdivinarNumero import Supervivencia as Su
from EstadisticasJuego import MostrarEstadisticas as ME
from EstadisticasJuego import EstadisticasFiltradasNombre as EF
from EstadisticasJuego import GuardarResultado as GR
import random
import getpass
import time


def ModoSolitario():
    jugando = True

    while jugando:
        print("\n---¡Hola! Este es el Modo Solitario---")
        
        print("\n¿Quieres adivinar un número aleatorio?\n¡¡¡COMENZEMOS!!!...")

        numeroAleatorio = random.randint(1, 1001)

        # Elegimos dificultad.
        opcion = Dificultad()
  
        if opcion == 4:
            print("\nVolviendo al Menú Principal...")
            jugando = False     # Así sale del modo solitario.

        else:
            # Vamos al menú de subdificultades.
            seleccion = Sd()

            nombre = input("Introduce tu nombre: ").capitalize()

            if seleccion == 4:
                print("\nVolviendo al Menú de dificultades...")
                continue    # Vuelve al menú de dificultades.
            
            # Ahora establecemos los rangos según la dificultad elegida.
            if opcion == 1:
                if seleccion == 1:
                    rangoInferior = max(1, numeroAleatorio-50)
                    rangoSuperior = min(1000, numeroAleatorio+50)
                    intentos, resultado = ANS(numeroAleatorio, 20, rangoInferior, rangoSuperior)
                
                elif seleccion == 2:
                    rangoInferior = max(1, numeroAleatorio-100)
                    rangoSuperior = min(1000, numeroAleatorio+100)
                    intentos, resultado = ANS(numeroAleatorio, 20, rangoInferior, rangoSuperior)

                elif seleccion == 3:
                    rangoInferior = max(1, numeroAleatorio-200)
                    rangoSuperior = min(1000, numeroAleatorio+200)
                    intentos, resultado = ANS(numeroAleatorio, 20, rangoInferior, rangoSuperior)

            elif opcion == 2:
                if seleccion == 1:
                    rangoInferior = max(1, numeroAleatorio-300)
                    rangoSuperior = min(1000, numeroAleatorio+300)
                    intentos, resultado = ANS(numeroAleatorio, 12, rangoInferior, rangoSuperior)

                elif seleccion == 2:
                    rangoInferior = max(1, numeroAleatorio-400)
                    rangoSuperior = min(1000, numeroAleatorio+400)
                    intentos, resultado = ANS(numeroAleatorio, 12, rangoInferior, rangoSuperior)

                elif seleccion == 3:
                    rangoInferior = max(1, numeroAleatorio-500)
                    rangoSuperior = min(1000, numeroAleatorio+500)
                    intentos, resultado = ANS(numeroAleatorio, 12, rangoInferior, rangoSuperior)

            elif opcion == 3:
                if seleccion == 1:
                    rangoInferior = max(1, numeroAleatorio-800)
                    rangoSuperior = min(1000, numeroAleatorio+800)
                    intentos, resultado = ANS(numeroAleatorio, 5, rangoInferior, rangoSuperior)

                elif seleccion == 2:
                    rangoInferior = max(1, numeroAleatorio-900)
                    rangoSuperior = min(1, numeroAleatorio+900)
                    intentos, resultado = ANS(numeroAleatorio, 5, rangoInferior, rangoSuperior)

                elif seleccion == 3:
                    rangoInferior = 1
                    rangoSuperior = 1000
                    intentos, resultado = ANS(numeroAleatorio, 5, rangoInferior, rangoSuperior)

            # Guardamos las partidas
            GR(nombre, "Solitario", f"Dificultad {opcion}", intentos, resultado)


def ModoDosJugadores():
    jugando = True

    print("\n---¡Hola! Este es el Modo de 2 Jugadores---")
    print("¡¡¡COMENZEMOS!!!...")
    print("\nAntes de que el Jugador 2 eliga la dificultad...")

    numeroJugadorUno = 0

    while numeroJugadorUno < 1 or numeroJugadorUno > 1000:
        try:
            numeroJugadorUno = int(getpass.getpass("\nJugador 1, introduce el número secreto entre 1 y 1000: "))
        except ValueError:
            print("Dato no válido. Hay que introducir un número: ")
            continue
    
    while jugando:
        # Elegimos dificultad.
        opcion = Dificultad()

        if opcion == 4:
            print("Volviendo al Menú Principal...")
            jugando = False     # Así sale del modo Dos Jugadores.

        else:
            # Vamos al menú de subdificultades.
            seleccion = Sd()

            nombre = input("\nJugador 2, introduce tu nombre: ").capitalize()

            if seleccion == 4:
                print("\nVolviendo al Menú de dificultades...")
                continue    # Vuelve al menú de dificultades.
            
            # Ahora establecemos los rangos según la dificultad elegida.
            if opcion == 1:
                if seleccion == 1:
                    rangoInferior = max(1, numeroJugadorUno-50)
                    rangoSuperior = min(1000, numeroJugadorUno+50)
                    intentos, resultado = ANDJ(numeroJugadorUno, 20, rangoInferior, rangoSuperior)
                
                elif seleccion == 2:
                    rangoInferior = max(1, numeroJugadorUno-100)
                    rangoSuperior = min(1000, numeroJugadorUno+100)
                    intentos, resultado = ANDJ(numeroJugadorUno, 20, rangoInferior, rangoSuperior)

                elif seleccion == 3:
                    rangoInferior = max(1, numeroJugadorUno-200)
                    rangoSuperior = min(1000, numeroJugadorUno+200)
                    intentos, resultado = ANDJ(numeroJugadorUno, 20, rangoInferior, rangoSuperior)
            
            elif opcion == 2:
                if seleccion == 1:
                    rangoInferior = max(1, numeroJugadorUno-300)
                    rangoSuperior = min(1000, numeroJugadorUno+300)
                    intentos, resultado = ANDJ(numeroJugadorUno, 12, rangoInferior, rangoSuperior)

                elif seleccion == 2:
                    rangoInferior = max(1, numeroJugadorUno-400)
                    rangoSuperior = min(1000, numeroJugadorUno+400)
                    intentos, resultado = ANDJ(numeroJugadorUno, 12, rangoInferior, rangoSuperior)

                elif seleccion == 3:
                    rangoInferior = max(1, numeroJugadorUno-500)
                    rangoSuperior = min(1000, numeroJugadorUno+500)
                    intentos, resultado = ANDJ(numeroJugadorUno, 12, rangoInferior, rangoSuperior)
                    
            elif opcion == 3:
                if seleccion == 1:
                    rangoInferior = max(1, numeroJugadorUno-800)
                    rangoSuperior = min(1000, numeroJugadorUno+800)
                    intentos, resultado = ANDJ(numeroJugadorUno, 5, rangoInferior, rangoSuperior)

                elif seleccion == 2:
                    rangoInferior = max(1, numeroJugadorUno-900)
                    rangoSuperior = min(1000, numeroJugadorUno+900)
                    intentos, resultado = ANDJ(numeroJugadorUno, 5, rangoInferior, rangoSuperior)

                elif seleccion == 3:
                    rangoInferior = 1
                    rangoSuperior = 1000
                    intentos, resultado = ANDJ(numeroJugadorUno, 5, rangoInferior, rangoSuperior)
                    
            # Guardamos las partidas
            GR(nombre, "Partida 2 Jugadores", f"Dificultad {opcion}", intentos, resultado)


# Ahora añadimos la mejora del Modo Supervivencia
def ModoSupervivencia():
    jugando = True

    while jugando:
        print("\n--- ¡Hola! Este es el Modo Supervivencia ---")
        print("\nHay que adivinar el número secreto antes de que se acabe el tiempo. ¡Buena Suerte!")
        
        numeroAleatorio = random.randint(1, 1001)

        # Elegimos la dificultad que va a afectar al tiempo del contador, al ser segundos y no intentos, se crea otro submenú
        print("\nSelecciona la dificultad:")
        print("  1. Fácil (60 segundos)")
        print("  2. Medio (30 segundos)")
        print("  3. Difícil (15 segundos)")
        print("  4. Volver al Menú Principal")

        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print("Opción no válida. Inténtalo de nuevo.")
            continue

        # A continuación confoguramos el tiempo según la dificultad que hayamos elegido
        if opcion == 4:
            print("\nVolviendo al Menú de dificultades...")
            return

        if opcion == 1:
            tiempoLimite = 60     # 60 segundos = nivel fácil
        elif opcion == 2:
            tiempoLimite = 30     # 30 segundos = nivel medio
        elif opcion == 3:
            tiempoLimite = 15     # 15 segundos = nivel difícil
        else:
            print("No válida.")
            continue

        nombre = input("Introduce tu nombre: ").capitalize()

        # Establecer el rango según la dificultad
        if opcion == 1:
            rangoInferior = max(1, numeroAleatorio - 250)
            rangoSuperior = min(1000, numeroAleatorio + 250)
        elif opcion == 2:
            rangoInferior = max(1, numeroAleatorio - 500)
            rangoSuperior = min(1000, numeroAleatorio + 500)
        elif opcion == 3:
            rangoInferior = max(1, numeroAleatorio - 1000)
            rangoSuperior = min(1000, numeroAleatorio + 1000)
        else: 
            print("Opción no válida.")
            continue

        print(f"\nTienes {tiempoLimite} segundos para adivinar el número secreto que está entre {rangoInferior} y {rangoSuperior}.")
        print("¡COMIENZA YA!")

        tiempoInicial = time.time()
        intentos, resultado = Su(numeroAleatorio, tiempoInicial, tiempoLimite, rangoInferior, rangoSuperior)

        GR(nombre, "Modo Supervivencia", f"Dificultad {opcion}", intentos, resultado)

