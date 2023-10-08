def obtener_coordenadas_disparo():
    fila = int(input("Ingresa la fila (0-9) donde deseas disparar: "))
    columna = int(input("Ingresa la columna (0-9) donde deseas disparar: "))
    return fila, columna

def mostrar_ambos_tableros(jugador_tablero, maquina_tablero):
    print(f"Tablero del jugador:")
    print(jugador_tablero.mostrar_tablero())
    print("\nTablero de disparos del jugador:")
    print(jugador_tablero.disparos)
    print("\nTablero de disparos de la máquina:")
    print(maquina_tablero.disparos)
