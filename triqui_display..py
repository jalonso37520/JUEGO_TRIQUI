def mostrar_tablero(tablero):
    print("\nTablero:")
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 5)
    print()
