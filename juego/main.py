import funciones as fn
import clases as cl

def main():
    print("¡Bienvenido al juego de Batalla Naval!")
    jugador_nombre = input("Por favor, ingresa tu nombre: ")
    jugador_tablero = cl.Tablero(jugador_nombre)
    jugador_tablero.inicializar_tablero()
    
    maquina_tablero = cl.Tablero("Máquina")
    maquina_tablero.inicializar_tablero()
    
    while True:
        fn.mostrar_ambos_tableros(jugador_tablero, maquina_tablero)

        while True:  
            try:
                fila, columna = fn.obtener_coordenadas_disparo()
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
        fila_maquina, columna_maquina = cl.Tablero.disparo_maquina()
        impacto_maquina = jugador_tablero.disparo(fila_maquina, columna_maquina)
        print(f"La máquina disparó en la posición ({fila_maquina}, {columna_maquina}).")
        if impacto_maquina:
            print("La máquina logró un impacto!")
        
        if jugador_tablero.barcos_restantes() == 0:
            print("¡La máquina ganó!")
            break

if __name__ == "__main__":
    main()

