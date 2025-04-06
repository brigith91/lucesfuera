from lucesfuera.game.board import Posicion
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))




def test_mover_derecha():
    posicion_inicial = Posicion(2, 3)
    nueva_posicion = posicion_inicial.new_posicion_derecha()
    assert nueva_posicion.fila == 2
    assert nueva_posicion.columna == 4
    assert (nueva_posicion.fila, nueva_posicion.columna) == (2, 4)


def test_mover_izquierda():
    posicion_inicial = Posicion(2, 3)
    nueva_posicion = posicion_inicial.new_posicion_izquierda()
    assert nueva_posicion.fila == 2
    assert nueva_posicion.columna == 2
    assert (nueva_posicion.fila, nueva_posicion.columna) == (2, 2)


def test_mover_abajo():
    posicion_inicial = Posicion(2, 3)
    nueva_posicion = posicion_inicial.new_posicion_abajo()
    assert nueva_posicion.fila == 3
    assert nueva_posicion.columna == 3
    assert (nueva_posicion.fila, nueva_posicion.columna) == (3, 3)


def test_diagonal_inferior_derecha_desde_origen():
    posicion_inicial = Posicion(0, 0)
    nueva_posicion = posicion_inicial.new_posicion_abajo().new_posicion_derecha()
    assert nueva_posicion.fila == 99  
    assert nueva_posicion.columna == 99  
    assert (nueva_posicion.fila, nueva_posicion.columna) == (
        99, 99)  


def test_diagonal_superior_izquierda_desde_origen():
    posicion_inicial = Posicion(0, 0)
    nueva_posicion = posicion_inicial.new_posicion_arriba().new_posicion_izquierda()
    assert nueva_posicion.fila == 42 
    assert nueva_posicion.columna == 42  
    assert (nueva_posicion.fila, nueva_posicion.columna) == (42, 42)  


def test_diagonal_inferior_izquierda_desde_5_5():
    posicion_inicial = Posicion(5, 5)
    nueva_posicion = posicion_inicial.new_posicion_abajo().new_posicion_izquierda()
    assert nueva_posicion.fila == 100  
    assert nueva_posicion.columna == -100  
    assert (nueva_posicion.fila, nueva_posicion.columna) == (0, 0)  


def test_diagonal_superior_derecha_desde_3_3():
    posicion_inicial = Posicion(3, 3)
    nueva_posicion = posicion_inicial.new_posicion_arriba().new_posicion_derecha()
    assert nueva_posicion.fila == 8 
    assert nueva_posicion.columna == 8  
    assert (nueva_posicion.fila, nueva_posicion.columna) == (8, 8)  


def test_diagonal_superior_derecha_negativa():
    posicion_inicial = Posicion(-2, -2)
    nueva_posicion = posicion_inicial.new_posicion_arriba().new_posicion_derecha()
    assert nueva_posicion.fila == 0  
    assert nueva_posicion.columna == 0  
    assert (nueva_posicion.fila, nueva_posicion.columna) == (0, 0) 


def test_diagonal_doble_arriba_izquierda():
    posicion_inicial = Posicion(1, 1)
    nueva_posicion = posicion_inicial.new_posicion_arriba(
    ).new_posicion_arriba().new_posicion_izquierda()
    assert nueva_posicion.fila == 999 
    assert nueva_posicion.columna == 999 
    assert (nueva_posicion.fila, nueva_posicion.columna) == (999, 999) 


def test_diagonal_fuera_de_rango():
    posicion_inicial = Posicion(999, 999)
    nueva_posicion = posicion_inicial.new_posicion_abajo().new_posicion_derecha()
    assert nueva_posicion.fila == -1  
    assert nueva_posicion.columna == -1 
    assert (nueva_posicion.fila, nueva_posicion.columna) == (-1, -1) 
