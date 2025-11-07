from ModuloModosJuego import ModoSolitario as MS
from ModuloModosJuego import ModoDosJugadores as MDJ
from ModuloModosJuego import ModoSupervivencia as Supervivencia
from EstadisticasJuego import Estadisticas

def Menu():
    jugando = True

    while jugando:
        try:
            print("\n---BIENVENIDO AL MENÚ---")
            print("  1. Partida modo solitario.")
            print("  2. Partida 2 Jugadores.")
            print("  3. Modo Supervivencia.")
            print("  4. Estadísticas.")
            print("  5. Salir.")

            opcion = int(input("\n¿Qué desea hacer? Elija una opción: "))

            while opcion < 1 or opcion > 5:
                opcion = int(input("\nOpción no válida, por favor, introduce una opción entre 1 y 5: "))

            if opcion == 1:
                MS() 
            elif opcion == 2:
                MDJ() 
            elif opcion == 3:
                Supervivencia()
            elif opcion == 4:
                Estadisticas()
            else:
                print("Gracias por jugar :) \n")
                exit()
                jugando = False
        
        except ValueError:
            print("Error: Hay que ingresar un número váido: ")
        except Exception as e:
            print(f"\nHa ocurrido un error inesperado: {e}")

Menu()