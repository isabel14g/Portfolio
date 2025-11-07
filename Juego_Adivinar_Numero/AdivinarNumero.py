from EstadisticasJuego import GuardarResultado as GR
from EstadisticasJuego import MostrarEstadisticas as ME
from EstadisticasJuego import EstadisticasFiltradasNombre as EF
from EstadisticasJuego import GuardarResultado as GR
import time

def AdivinarNumeroSolitario(numeroAleatorio, intentosMaximos, rangoInferior, rangoSuperior):
    print(f"\nTienes {intentosMaximos} intentos para adivinar el número.")
    print(f"El número secreto está entre {rangoInferior} y {rangoSuperior}.")

    intento = 1
    adivinado = False

    while intento <= intentosMaximos and not adivinado:
        try:
            resultadoAdivinado = int(input(f"\nIntento {intento}/{intentosMaximos}. Introduce un número: "))
           
            if resultadoAdivinado < 1 or resultadoAdivinado > 1000:
                print("ERROR, el juego solo acepta valores del 1 al 1000. Vuelve a introducir el número.")
                continue

        except ValueError:
            print("Dato no válido. Hay que introducir un número: ")
            continue

        if resultadoAdivinado > numeroAleatorio:
            print("El número es MENOR.")
        elif resultadoAdivinado < numeroAleatorio:
            print("El número es MAYOR.")
        else:
            print(f"\nENHORABUENA! Has acertado el número secreto en {intento} intentos.")
            return intento, "Ganada"
            adivinado = True

        intento += 1
    
    if not adivinado:
        print(f"\nLo siento, has agotado todos los intentos. El número secreto era {numeroAleatorio}.\n\nVolviendo al Menú de dificultades...")
        return intentosMaximos, "Perdida"

    return adivinado


def AdivinarNumeroDosJugadores(numeroJugadorUno, intentosMaximos, rangoInferior, rangoSuperior):
    print(f"\nTienes {intentosMaximos} intentos para adivinar el número.")
    print(f"El número secreto está entre {rangoInferior} y {rangoSuperior}.")

    intento = 1
    adivinado = False

    while intento <= intentosMaximos and not adivinado:
        try:
            resultadoAdivinado = int(input(f"\nIntento {intento}/{intentosMaximos}. Introduce un número: "))

            if resultadoAdivinado < 1 or resultadoAdivinado > 1000:
                print("ERROR, el juego solo acepta valores del 1 al 1000. Vuelve a introducir el número.")
                continue

        except ValueError:
            print("\nDato no válido. Hay que introducir un número: ")
            continue

        if resultadoAdivinado > numeroJugadorUno:
            print("El número es MENOR.")
        elif resultadoAdivinado < numeroJugadorUno:
            print("El número es MAYOR.")
        else:
            print(f"\nENHORABUENA! Has acertado el número secreto en {intento} intentos.")
            adivinado = True
            return intento, "Ganada"

        intento += 1

    if not adivinado:
        print(f"\nLo siento, has agotado todos los intentos. El número secreto era {numeroJugadorUno}.\n\nVolviendo al Menú de dificultades...")
        return intento, "Perdida"

    return adivinado


def Supervivencia(numeroAleatorio, tiempoInicial, tiempoLimite, rangoInferior, rangoSuperior):
    print(f"\nTienes {tiempoLimite} intentos para adivinar el número.")
    print(f"El número secreto está entre {rangoInferior} y {rangoSuperior}.")

    intento = 0
    adivinado = False


    while not adivinado:
        tiempoTranscurrido = int(time.time() - tiempoInicial)
        tiempoRestante = tiempoLimite - tiempoTranscurrido

        if tiempoRestante <= 0:
            break

        # Esperamos un segundo para mostrar lo siguiente
        time.sleep(1)

        # Mostramos el tiempo que queda
        print(f"\nTe quedan {tiempoRestante} segundos.")
    
        try:
            resultadoAdivinado = int(input("Introduce un número: "))
                      
            if resultadoAdivinado < 1 or resultadoAdivinado > 1000:
                print("ERROR, el juego solo acepta valores del 1 al 1000. Vuelve a introducir el número.")
                continue

        except ValueError:
            print("Dato no válido. Hay que introducir un número: ")
            continue

        if resultadoAdivinado > numeroAleatorio:
            print("El número es MENOR.")
        elif resultadoAdivinado < numeroAleatorio:
            print("El número es MAYOR.")
        else:
            tiempoTotal = int(time.time() - tiempoInicial)
            print(f"\n¡Enhorabuena! Has acertado el número secreto en {tiempoTotal} segundos.")
            adivinado = True
            resultado = "Victoria"

            intento += 1
 
    if not adivinado:
        print(f"\n¡Se acabó el tiempo! No lograste adivinar el número. El número secreto era {numeroAleatorio}.")
        resultado = "Derrota"

    return intento, resultado