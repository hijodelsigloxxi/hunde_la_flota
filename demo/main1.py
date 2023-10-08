import funciones1 as fn

def obtener_coordenadas_disparo():
    fila = int(input("Ingresa la fila (0-4) donde deseas disparar: "))
    columna = int(input("Ingresa la columna (0-4) donde deseas disparar: "))
    return fila, columna

def mostrar_ambos_tableros(jugador_tablero, maquina_tablero):
    print(f"Tablero del jugador:")
    jugador_tablero.mostrar_tablero()
    print("\nTablero de disparos del jugador:")
    print(jugador_tablero.disparos)
    print("\nTablero de disparos de la máquina:")
    print(maquina_tablero.disparos)

def main():
    print("¡Bienvenido al juego de Batalla Naval Simplificado!")
    jugador_nombre = input("Por favor, ingresa tu nombre: ")
    jugador_tablero = fn.Tablero(jugador_nombre)
    jugador_tablero.inicializar_tablero()
    
    maquina_tablero = fn.Tablero("Máquina")
    maquina_tablero.inicializar_tablero()
    
    while True:
        mostrar_ambos_tableros(jugador_tablero, maquina_tablero)
        

        while True:  # Bucle hasta obtener un disparo válido
            try:
                fila, columna = obtener_coordenadas_disparo()
                impacto = maquina_tablero.disparo(fila, columna)
                if impacto:
                    print("¡Impacto!")
                else:
                    print("Fallaste.")
                break  # Salimos del bucle una vez que tenemos un disparo válido
            except IndexError:
                print("Has intentado disparar fuera del tablero. Inténtalo de nuevo.")
            except ValueError:
                print("Entrada inválida. Asegúrate de ingresar un número.")
        
        if maquina_tablero.barcos_restantes() == 0:
            print(f"¡Felicidades {jugador_nombre}! Ganaste.")
            break
        
        # Turno de la máquina
        fila_maquina, columna_maquina = fn.Tablero.disparo_maquina()
        impacto_maquina = jugador_tablero.disparo(fila_maquina, columna_maquina)
        print(f"La máquina disparó en la posición ({fila_maquina}, {columna_maquina}).")
        if impacto_maquina:
            print("La máquina logró un impacto!")
        
        if jugador_tablero.barcos_restantes() == 0:
            print("¡La máquina ganó!")
            break

if __name__ == "__main__":
    main()