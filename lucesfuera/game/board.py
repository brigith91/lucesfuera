from dataclasses import dataclass
from typing import NewType

from lucesfuera.game.luz import Luz

BoardShape: type = NewType("BoardShape", list[list[str]])


@dataclass
class Posicion:
    fila: int
    columna: int

    def new_posicion_derecha(self):
        return Posicion(self.fila, self.columna + 1)

    def new_posicion_izquierda(self):
        return Posicion(self.fila, self.columna - 1)

    def new_posicion_abajo(self):
        return Posicion(self.fila + 1, self.columna)

    def new_posicion_arriba(self):
        return Posicion(self.fila - 1, self.columna)


class Tablero:
    width: int
    height: int
    tablero: BoardShape

    def __init__(self, width: int, height: int, tablero: BoardShape = None):
        """
        Crea un tablero de luces, si no se especifica un tablero, se crea uno con
        todas las luces apagadas.

        Parameters
        ----------
        width : int
            Ancho del tablero.
        height : int
            Alto del tablero.
        tablero : BoardShape, optional
            Tablero de luces, por defecto es None.
        """
        self.width = width
        self.height = height
        self.tablero = tablero if tablero else self.crear_tablero_vacio(width, height)

    def crear_tablero_vacio(self, width: int, height: int) -> BoardShape:
        """
        Crea un tablero de luces apagadas.

        Parameters
        ----------
        width : int
            Ancho del tablero.
        height : int
            Alto del tablero.

        Returns
        -------
        BoardShape
            Tablero de luces apagadas.
        """
        return [[Luz.OFF for _ in range(width)] for _ in range(height)]

    def prender_apagar(self, posicion: Posicion):
        """
        Prende o apaga una luz en la posición dada.

        Parameters
        ----------
        posicion : Posicion
            Posición de la luz a prender o apagar.
        """
        self.tablero[posicion.fila][posicion.columna] = (
            Luz.ON
            if self.tablero[posicion.fila][posicion.columna] == Luz.OFF
            else Luz.OFF
        )

    def switch_luz(self, posicion: Posicion):
        """
        Prende o apaga las luces cercanas a la posición dada.

        Parameters
        ----------
        posicion : Posicion
            Posición de la luz a prender o apagar.
        """
        self.prender_apagar(posicion)
        self.prender_apagar(posicion.new_posicion_derecha())
        self.prender_apagar(posicion.new_posicion_izquierda())
        self.prender_apagar(posicion.new_posicion_abajo())
        self.prender_apagar(posicion.new_posicion_arriba())
        self.prender_apagar(posicion.new_posicion_derecha().new_posicion_abajo())
        self.prender_apagar(posicion.new_posicion_derecha().new_posicion_arriba())
        self.prender_apagar(posicion.new_posicion_izquierda().new_posicion_abajo())
        self.prender_apagar(posicion.new_posicion_izquierda().new_posicion_arriba())

    def to_list(self) -> list[list[str]]:
        """
        Convierte el tablero a una lista de listas de strings.

        Returns
        -------
        list[list[str]]
            Tablero de luces en formato de lista de listas de strings.
        """
        return [[luz for luz in fila] for fila in self.tablero]

    def is_resuelto(self) -> bool:
        """
        Verifica si el tablero está resuelto.

        Returns
        -------
        bool
            True si el tablero está resuelto, False en caso contrario.
        """
        estado_luz: Luz = self.tablero[0][0]
        return all(all(luz == estado_luz for luz in fila) for fila in self.tablero)
