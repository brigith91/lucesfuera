from lucesfuera.game.board import Tablero, Posicion
from lucesfuera.game.luz import Luz
import pytest


@pytest.mark.parametrize(
    "fila, col_init, col_fin",
    [
        (0, 0, 1) # 1
        (0, -5, -4) # 2
        (0, 100, 101) # 3
    ]
)

def test_posicion_deberia_mover_derecha(fila, col_init, col_fin):
    p= Posicion(fila, col_init)
    resultado = Posicion =p.new_posicion_derecha()
    esperado: Posicion = Posicion(fila,col_fin) 
    assert resultado == esperado

@pytest.mark.parametrize(
    "pos_inicial, pos_final"
    [
        ((0, 0),   (0, -1)),       # 1
        ((0, -5),  (0, -6)),       # 2
        ((0, 100), (0, 99)),       # 3
        ((-5, 0),  (-5, -1)),      # 4
        ((-5, -5), (-5, -6)),      # 5
        ((-5, -100), (-5, 99)),    # 6
    ]
)

def test_posicion_deberia_mover_izquierda(pos_inicial, pos_final):
    p= Posicion(pos_inicial, [0],pos_inicial[1] )
    resultado = Posicion =p.new_posicion_izquierda()
    esperado: Posicion = Posicion(pos_final[0], pos_final[1]) # type: ignore
    assert resultado == esperado

@pytest.mark.skip("no se ha implementado el movimiento diagonal")
@pytest.mark.parametrize(
    "pos_inicial, pos_final"
    [
        ((0, 0),   (-1, -1)),      # 1
        ((0, -5),  (0, -6)),       # 2
        ((0, 100), (0, 99)),       # 3
        ((-5, 0),  (-5, -1)),      # 4
        ((-5, -5), (-5, -6)),      # 5
        ((-5, 100), (-5, 99)),     # 6
    ]

)
def test_posicion_deberia_mover_diagonal_derecha_arriba(pos_inicial, pos_final):
    p= Posicion(pos_inicial, [0],pos_inicial[1] )
    resultado = Posicion =p.new_posicion_diagonal_derecha_arriba()
    esperado: Posicion = Posicion(pos_final[0], pos_final[1])
    assert resultado == esperado

@pytest.mark.parametrize(
    "tablero_esperado, ancho, alto"
    [
        ([[Luz.OFF]], 1, 1),
        ([[Luz.OFF,Luz.OFF], [Luz.OFF,Luz.OFF]], 2, 2),
        ([], 0, 0),
        ([], -1, -1),
        ([[]], 1, 0),
        ([[Luz.OFF,Luz.OFF]], 2, 1),
    ]       
)
def test_tablero_creacion_vacio(tablero_esperado, ancho, alto):
    resultado = Tablero(ancho, alto).tablero
    assert tablero_esperado == resultado

@pytest.fixture
def talero_manual():
    return [
        [Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF,]
        [Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF,]
        [Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF,]
        [Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF,]
        [Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF,]
        [Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF,]

    ]

def test_tablero_prender_apagar(tablero_grande:Tablero, tablero_manual: lis[list[int]])-> none:
    tablero_grande.prender_apagar(Posicion(0, 0))
    tablero_manual[0][0] = Luz.ON
    assert tablero_grande.tablero== tablero_manual

    tablero_grande.prender_apagar(Posicion(0, 0))
    tablero_manual[0][0] = Luz.OFF
    assert tablero_grande.tablero== tablero_manual

    tablero_grande.prender_apagar(Posicion(5, 5))
    tablero_manual[5][5] = Luz.ON
    assert tablero_grande.tablero== tablero_manual

    tablero_grande.prender_apagar(Posicion(5, 5))
    tablero_manual[5][5] = Luz.OFF
    assert tablero_grande.tablero== tablero_manual

@pytest.mark.parametrize()
def test_tablero_switch_Luz(tablero_grande, tablero_manual):
    tablero_grande.switch_Luz = (Posicion(0, 0))
    tablero_manual =[0][0]=Luz.ON
    tablero_manual =[0][1]=Luz.ON
    tablero_manual =[1][0]=Luz.ON
    tablero_manual =[1][1]=Luz.ON

