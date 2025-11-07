def Dificultad():
    opcion = 0
    while opcion not in [1,2,3,4]:
        print("\nHola!! Elija la dificultad:")
        print("  1. Fácil (20 intentos)")
        print("  2. Intermedio (12 intentos)")
        print("  3. Difícil (5 intentos)")
        print("  4. Volver al Menú Principal")

        try:
            opcion = int(input("\nSelecciona una opción entre 1 y 4: "))
        except ValueError:
            print("Dato no válido. Hay que introducir un número entre 1 y 4: ")
    
    return opcion


def SubDificultades():
    seleccion = 0
    while seleccion not in [1,2,3,4]:
        print("\n---Este es el submenú de dificultades. ¿Qué nivel eliges?---")
        print("  1. Principiante")
        print("  2. Medio")
        print("  3. Avanzado")
        print("  4. Volver a elegir dificultad")

        try:
            seleccion = int(input("\nSelecciona una opción entre 1 y 4: "))
        except ValueError:
            print("Dato no válido. Hay que introducir un número entre 1 y 4: ")

    return seleccion


