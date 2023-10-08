import numpy as np
import random as rd

class Tablero:
    FILA = 5
    COLUMNA = 5
    BARCOS = {"barco1": 1}

    def __init__(self, jugador):
        self.jugador = jugador
        self.tablero = np.full((Tablero.FILA, Tablero.COLUMNA), 0)  # 0 para agua, 1 para barco
        self.disparos = np.full((Tablero.FILA, Tablero.COLUMNA), 0)  # 0 para no disparado, 1 para impacto, -1 para falla

    def posicion_aleatoria(self, eslora):
        orientacion = rd.choice(["horizontal", "vertical"])
        if orientacion == "horizontal":
            fila = rd.randint(0, Tablero.FILA - 1)
            columna = rd.randint(0, Tablero.COLUMNA - eslora)
        else:
            fila = rd.randint(0, Tablero.FILA - eslora)
            columna = rd.randint(0, Tablero.COLUMNA - 1)
        return fila, columna, orientacion

    def es_posicion_valida(self, fila, columna, orientacion, eslora):
        if orientacion == "horizontal":
            segmento = self.tablero[fila, columna:columna + eslora]
        else:
            segmento = self.tablero[fila:fila + eslora, columna]
        return np.all(segmento == 0)

    def colocar_barco(self, eslora):
        while True:
            fila, columna, orientacion = self.posicion_aleatoria(eslora)
            if self.es_posicion_valida(fila, columna, orientacion, eslora):
                if orientacion == "horizontal":
                    self.tablero[fila, columna:columna + eslora] = 1
                else:
                    self.tablero[fila:fila + eslora, columna] = 1
                break

    def inicializar_tablero(self):
        for eslora in Tablero.BARCOS.values():
            self.colocar_barco(eslora)

    def disparo(self, fila, columna):
        if self.disparos[fila, columna] == 0:
            impacto = self.tablero[fila, columna] == 1
            self.disparos[fila, columna] = 1 if impacto else -1
            return impacto
        return False

    def mostrar_tablero(self):
        print(" ", end="  ")  
        for i in range(Tablero.COLUMNA):
            print(i, end="  ")
        print()  

        for idx, row in enumerate(self.tablero):
            print(idx, end="  ")  
            for cell in row:
                print(cell, end="  ") 
            print()  
    def barcos_restantes(self):
        return np.sum(self.tablero) - np.sum(self.disparos == 1)

    @staticmethod
    def disparo_maquina():
        return rd.randint(0, Tablero.FILA - 1), rd.randint(0, Tablero.COLUMNA - 1)