from lucesfuera.game.board import Tablero, Posicion
from lucesfuera.game.luz import Luz
import pytest

#Posicion
@pytest.mark.parametrize(
    "fila, col_init, col_fin",
    [
        (0, 0, 1), 
        (0, -5, -4),
        (0, 100, 101),
        (5, 2, 3),           
        (-3, 1, 2),          
        (0, -1, 0),          
        (-2, -3, -2),        
        (10, 0, 1),          
        (0, 50, 51),         
        (0, -10, -9)
    ]
)
def test_posicion_deberia_mover_derecha(fila, col_init, col_fin):
    p = Posicion(fila, col_init)
    resultado = p.new_posicion_derecha()
    esperado = Posicion(fila, col_fin)
    assert resultado == esperado # Verifica que el resultado final es el esperado
    assert resultado.fila == fila # Verifica que la fila sigue siendo la misma
    assert resultado.columna == col_fin # Verifica que la columna final es la correcta

@pytest.mark.parametrize(
    "pos_inicial, pos_final",
    [
        ((0, 0),   (0, -1)),       
        ((0, -5),  (0, -6)),       
        ((0, 100), (0, 99)),       
        ((-5, 0),  (-5, -1)),      
        ((-5, -5), (-5, -6)),      
        ((-5, -100), (-5, 99)), 
        ((2, 3),   (2, 2)),        
        ((-3, 5),  (-3, 4)),       
        ((0, 10),  (0, 9)),        
        ((4, 0),   (4, -1)),       
        ((-2, -3), (-2, -4))   
    ]
)
def test_posicion_deberia_mover_izquierda(pos_inicial, pos_final):
    p = Posicion(pos_inicial[0], pos_inicial[1])
    resultado = p.new_posicion_izquierda()
    esperado = Posicion(pos_final[0], pos_final[1])
    assert resultado == esperado #Verifica si la nueva posición es igual a la esperada.
    assert resultado.fila == pos_final[0] # la fila de la posición obtenida es igual a la fila esperada.
    assert resultado.columna == pos_final[1] #la columna de la posición obtenida es igual a la columna esperada.

@pytest.mark.skip("no se ha implementado el movimiento diagonal")
@pytest.mark.parametrize(
    "pos_inicial, pos_final",
    [
        ((0, 0),   (-1, -1)),      
        ((0, -5),  (0, -6)),       
        ((0, 100), (0, 99)),       
        ((-5, 0),  (-5, -1)),      
        ((-5, -5), (-5, -6)),      
        ((-5, 100), (-5, 99)), 
        ((5, 5),   (4, 4)),        
        ((-2, -3), (-3, -4)),      
        ((2, 3),   (1, 2)),        
        ((0, 0),   (-1, -1))     
    ]
)
def test_posicion_deberia_mover_diagonal_derecha_arriba(pos_inicial, pos_final):
    p = Posicion(pos_inicial[0], pos_inicial[1])
    resultado = p.new_posicion_diagonal_derecha_arriba()
    esperado = Posicion(pos_final[0], pos_final[1])
    assert resultado == esperado #Verifica si la nueva posición es igual a la esperada.
    assert resultado.fila == pos_final[0]  #la fila de la posición obtenida es igual a la fila
    assert resultado.columna == pos_final[1] # la columna de la posición obtenida es igual a la columna esperada.

@pytest.mark.parametrize(
    "pos_inicial, pos_final",
    [
        ((0, 0),   (-1, 1)),      
        ((0, -5),  (-1, -4)),       
        ((0, 100), (-1, 101)),       
        ((-5, 0),  (-6, 1)),      
        ((-5, -5), (-6, -4)),      
        ((-5, 100), (-6, 101)),     
        ((5, 5),   (4, 6)),        
        ((-2, -3), (-3, -2)),      
        ((2, 3),   (1, 4)),        
        ((0, 0),   (-1, 1))      
    ]
)
def test_posicion_deberia_mover_diagonal_izquierda_arriba(pos_inicial, pos_final):
    p = Posicion(pos_inicial[0], pos_inicial[1])
    resultado = p.new_posicion_diagonal_izquierda_arriba()
    esperado = Posicion(pos_final[0], pos_final[1])
    assert resultado == esperado     #Compara si la posición obtenida es igual a la esperada
    assert resultado.fila == pos_final[0]#la fila de la posición obtenida es igual a la fila de la posición esperada
    assert resultado.columna == pos_final[1] # la columna de la posición obtenida es igual a la columna de la posición esperada

@pytest.mark.parametrize(
    "fila, col_init, col_fin",
    [
        (0, 0, 1), 
        (0, -1, 0), 
        (10, 99, 100),
        (0, -10, -9),
        (100, 1000, 1001),
        (5, 4, 5),    
        (-3, 0, 1),   
        (8, 5, 6),    
        (0, 10, 11),  
        (10, 1, 2)    
    ]
)
def test_posicion_deberia_mover_derecha_borde(fila, col_init, col_fin):
    p = Posicion(fila, col_init)
    resultado = p.new_posicion_derecha()
    esperado = Posicion(fila, col_fin)
    assert resultado == esperado #Compara si la posición obtenida es igual a la esperada
    assert resultado.fila == fila #la fila de la posición obtenida es igual a la fila de la posición esperada
    assert resultado.columna == col_fin # Tercer assert: Compara si la columna de la posición obtenida es igual a la columna de la posición esperada

@pytest.mark.parametrize(
    "pos_inicial, pos_final",
    [
        ((0, 0),   (0, -1)),       
        ((-5, -5), (-5, -6)),       
        ((10, 10), (10, 9)),
        ((0, -5), (0, -6)),
        ((-100, -100), (-100, -101)),
        ((0, 0),   (-1, -1)),
        ((3, 5),   (3, 4)),
        ((0, 2),   (0, 1)),
        ((4, 1),   (4, 0)),
        ((2, 4),   (2, 3))
    ]
)
def test_posicion_deberia_mover_izquierda_borde(pos_inicial, pos_final):
    p = Posicion(pos_inicial[0], pos_inicial[1])
    resultado = p.new_posicion_izquierda()
    esperado = Posicion(pos_final[0], pos_final[1])
    assert resultado == esperado # Compara la posición completa (fila y columna)
    assert resultado.fila == pos_inicial[0]  # Compara la fila de la posición obtenida
    assert resultado.columna == pos_final[1]  # Compara la columna de la posición obtenida


@pytest.mark.parametrize(
    "pos_inicial, col_final",
    [
        ((0, 0), 10),     
        ((-5, 100), 101),  
        ((-10, 0), 11),    
        ((100, 0), 101),   
        ((-100, -100), -99),
        ((2, 50), 51),
        ((-3, 50), 51),
        ((10, 200), 201),
        ((0, 0), 1),
        ((-5, 5), 6)
    ]
)
def test_posicion_fuera_de_limites(pos_inicial, col_final):
    p = Posicion(pos_inicial[0], pos_inicial[1])
    resultado = p.new_posicion_derecha()
    esperado = Posicion(pos_inicial[0], col_final)
    assert resultado == esperado # Compara la posición completa (fila y columna)
    assert resultado.fila == pos_inicial[0]  # Compara la fila de la posición obtenida
    assert resultado.columna == col_final  # Compara la columna de la posición obtenida

#Tablero

#vacio
@pytest.mark.parametrize(
    "tablero_esperado, ancho, alto",
    [
        ([[Luz.OFF]], 1, 1),  # Prueba un tablero de 1x1
        ([[Luz.OFF,Luz.OFF], [Luz.OFF,Luz.OFF]], 2, 2),  # Tablero 2x2
        ([], 0, 0),  # Tablero vacío (0x0)
        ([], -1, -1),  # Tamaños negativos
        ([[]], 1, 0),  # Tablero con 1 columna y 0 filas
        ([[Luz.OFF,Luz.OFF]], 2, 1),  # Tablero 2x1
        ([[Luz.OFF, Luz.OFF, Luz.OFF]], 3, 1),  # Tablero 3x1
        ([[Luz.OFF], [Luz.OFF], [Luz.OFF]], 1, 3),  # Tablero 1x3
        ([[Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF], [Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF], [Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF], [Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF]], 4, 4),  # Tablero 4x4
        ([[Luz.OFF]*5]*5, 5, 5),  # Tablero 5x5
    
    ]
)
def test_tablero_creacion_vacio(tablero_esperado, ancho, alto):
    resultado = Tablero(ancho, alto).tablero
    assert tablero_esperado == resultado # Compara el tablero esperado con el resultado obtenido
    assert len(resultado) == alto  # Verifica que la cantidad de filas sea igual al alto
    assert all(len(fila) == ancho for fila in resultado)  # Verifica que todas las filas tengan el ancho correcto



# Fixture para tablero manual
@pytest.fixture
def tablero_manual():
    return [
        [Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF],
        [Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF],
        [Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF],
        [Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF],
        [Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF],
        [Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF],
    ]

# Fixture para tablero grande
@pytest.fixture
def tablero_grande():
    t = Tablero(6, 6)
    return t

# prender y apagar luces 
def test_tablero_prender_apagar(tablero_grande: Tablero, tablero_manual: list[list[Luz]]):
    
    # Encender una luz en una esquina (0, 0)
    tablero_grande.prender_apagar(Posicion(0, 0))
    tablero_manual[0][0] = Luz.ON
    assert tablero_grande.tablero == tablero_manual  # Verifica que la luz en la posición (0, 0) esté encendida
    assert tablero_grande.tablero[0][0] == Luz.ON  # Verifica que la luz en la posición (0, 0) esté encendida 
    assert tablero_grande.tablero != [[Luz.OFF]]  # Verifica que no todo el tablero esté apagado

    # Apagar la luz en la misma posición (0, 0)
    tablero_grande.prender_apagar(Posicion(0, 0))
    tablero_manual[0][0] = Luz.OFF
    assert tablero_grande.tablero == tablero_manual  # Verifica que la luz en la posición (0, 0) esté apagada
    assert tablero_grande.tablero[0][0] == Luz.OFF  # Verifica que la luz en la posición (0, 0) esté apagada específicamente
    assert tablero_grande.tablero != [[Luz.ON]]  # Verifica que no todo el tablero esté encendido


    # Encender una luz en la esquina inferior derecha (5, 5)
    tablero_grande.prender_apagar(Posicion(5, 5))
    tablero_manual[5][5] = Luz.ON
    assert tablero_grande.tablero == tablero_manual  # Verifica que la luz en la posición (5, 5) esté encendida
    assert tablero_grande.tablero[5][5] == Luz.ON  # Verifica que la luz en la posición (5, 5) esté encendida específicamente
    assert tablero_grande.tablero != [[Luz.OFF]*6]*6  # Verifica que no todo el tablero esté apagado

    # Apagar la luz en la esquina inferior derecha (5, 5)
    tablero_grande.prender_apagar(Posicion(5, 5))
    tablero_manual[5][5] = Luz.OFF
    assert tablero_grande.tablero == tablero_manual  # Verifica que la luz en la posición (5, 5) esté apagada
    assert tablero_grande.tablero[5][5] == Luz.OFF  # Verifica que la luz en la posición (5, 5) esté apagada específicamente
    assert tablero_grande.tablero != [[Luz.ON]*6]*6  # Verifica que no todo el tablero esté encendido

    # Encender una luz en el borde superior (0, 2)
    tablero_grande.prender_apagar(Posicion(0, 2))
    tablero_manual[0][2] = Luz.ON
    assert tablero_grande.tablero == tablero_manual  # Verifica que la luz en la posición (0, 2) esté encendida
    assert tablero_grande.tablero[0][2] == Luz.ON  # Verifica que la luz en la posición (0, 2) esté encendida específicamente
    assert tablero_grande.tablero != [[Luz.OFF]*6]*6  # Verifica que no todo el tablero esté apagado

    # Apagar una luz en el borde superior (0, 2)
    tablero_grande.prender_apagar(Posicion(0, 2))
    tablero_manual[0][2] = Luz.OFF
    assert tablero_grande.tablero == tablero_manual  # Verifica que la luz en la posición (0, 2) esté apagada
    assert tablero_grande.tablero[0][2] == Luz.OFF  # Verifica que la luz en la posición (0, 2) esté apagada específicamente
    assert tablero_grande.tablero != [[Luz.ON]*6]*6  # Verifica que no todo el tablero esté encendido
    
    # Encender una luz en una fila intermedia (3, 3)
    tablero_grande.prender_apagar(Posicion(3, 3))
    tablero_manual[3][3] = Luz.ON
    assert tablero_grande.tablero == tablero_manual  # Verifica que la luz en la posición (3, 3) esté encendida
    assert tablero_grande.tablero[3][3] == Luz.ON  # Verifica específicamente que la luz en la posición (3, 3) esté encendida
    assert tablero_grande.tablero != [[Luz.OFF]*6]*6  # Verifica que no todo el tablero esté apagado

    # Apagar una luz en la fila intermedia (3, 3)
    tablero_grande.prender_apagar(Posicion(3, 3))
    tablero_manual[3][3] = Luz.OFF
    assert tablero_grande.tablero == tablero_manual  # Verifica que la luz en la posición (3, 3) esté apagada
    assert tablero_grande.tablero[3][3] == Luz.OFF  # Verifica específicamente que la luz en la posición (3, 3) esté apagada
    assert tablero_grande.tablero != [[Luz.ON]*6]*6  # Verifica que no todo el tablero esté encendido

    # Encender una luz en la columna inferior (5, 0)
    tablero_grande.prender_apagar(Posicion(5, 0))
    tablero_manual[5][0] = Luz.ON
    assert tablero_grande.tablero == tablero_manual  # Verifica que la luz en la posición (5, 0) esté encendida
    assert tablero_grande.tablero[5][0] == Luz.ON  # Verifica específicamente que la luz en la posición (5, 0) esté encendida
    assert Luz.ON in tablero_grande.tablero[5]  # Verifica que haya al menos una luz encendida en la fila 5

    # Apagar una luz en la columna inferior (5, 0)
    tablero_grande.prender_apagar(Posicion(5, 0))
    tablero_manual[5][0] = Luz.OFF
    assert tablero_grande.tablero == tablero_manual  # Verifica que la luz en la posición (5, 0) esté apagada
    assert tablero_grande.tablero[5][0] == Luz.OFF  # Verifica específicamente que la luz en la posición (5, 0) esté apagada
    assert Luz.OFF in tablero_grande.tablero[5]  # Verifica que haya al menos una luz apagada en la fila 5


# is resuelto
@pytest.mark.parametrize(
    "tablero_inicial, esperado",
    [
        ([[Luz.OFF, Luz.OFF], [Luz.OFF, Luz.OFF]], True),  # Todas las luces apagadas,
        ([[Luz.OFF, Luz.ON], [Luz.OFF, Luz.OFF]], False),  # Una luz está encendida
        ([[Luz.ON, Luz.OFF], [Luz.OFF, Luz.OFF]], False),  # Una luz está encendida
        ([[Luz.OFF, Luz.OFF], [Luz.ON, Luz.OFF]], False),  # Una luz está encendida
        ([[Luz.ON, Luz.ON], [Luz.OFF, Luz.OFF]], False),   # Dos luces encendidas
        ([[Luz.OFF, Luz.ON], [Luz.ON, Luz.OFF]], False),   # Varias luces encendidas
        ([[Luz.ON, Luz.ON], [Luz.ON, Luz.OFF]], False),    # Tres luces encendidas
        ([[Luz.ON, Luz.ON], [Luz.ON, Luz.ON]], False),     # Todas las luces encendidas
        ([[Luz.OFF, Luz.OFF], [Luz.OFF, Luz.OFF], [Luz.OFF, Luz.OFF]], True),  # Todas las luces apagadas (más grande)
        ([[Luz.OFF, Luz.ON], [Luz.OFF, Luz.OFF], [Luz.OFF, Luz.OFF]], False),  # Una luz está encendida en un tablero grande
    ]
)
def test_is_resuelto(tablero_inicial, esperado):
    tablero = Tablero(len(tablero_inicial[0]), len(tablero_inicial))
    tablero.tablero = tablero_inicial  
    resultado = tablero.is_resuelto()
    assert resultado == esperado                      # Verifica que el resultado sea el esperado
    assert type(resultado) == bool                    # Verifica que el resultado sea de tipo booleano
    assert tablero.ancho == len(tablero_inicial[0])   # Verifica que el ancho del tablero se haya asignado correctamente


#to list
@pytest.mark.parametrize(
    "tablero_inicial, esperado",
    [
        ([[Luz.OFF, Luz.OFF], [Luz.OFF, Luz.OFF]], [[Luz.OFF, Luz.OFF], [Luz.OFF, Luz.OFF]]),  # Tablero vacío
        ([[Luz.ON, Luz.OFF], [Luz.OFF, Luz.OFF]], [[Luz.ON, Luz.OFF], [Luz.OFF, Luz.OFF]]),  # Una luz encendida
        ([[Luz.OFF, Luz.OFF], [Luz.ON, Luz.OFF]], [[Luz.OFF, Luz.OFF], [Luz.ON, Luz.OFF]]),  # Una luz encendida
        ([[Luz.OFF, Luz.OFF], [Luz.OFF, Luz.ON]], [[Luz.OFF, Luz.OFF], [Luz.OFF, Luz.ON]]),  # Una luz encendida
        ([[Luz.ON, Luz.ON], [Luz.OFF, Luz.OFF]], [[Luz.ON, Luz.ON], [Luz.OFF, Luz.OFF]]),  # Dos luces encendidas
        ([[Luz.OFF, Luz.ON], [Luz.OFF, Luz.OFF]], [[Luz.OFF, Luz.ON], [Luz.OFF, Luz.OFF]]),  # Varias luces encendidas
        ([[Luz.ON, Luz.ON], [Luz.ON, Luz.OFF]], [[Luz.ON, Luz.ON], [Luz.ON, Luz.OFF]]),  # Tres luces encendidas
        ([[Luz.ON, Luz.ON], [Luz.ON, Luz.ON]], [[Luz.ON, Luz.ON], [Luz.ON, Luz.ON]]),  # Todas las luces encendidas
        ([[Luz.OFF, Luz.OFF], [Luz.OFF, Luz.OFF], [Luz.OFF, Luz.OFF]], [[Luz.OFF, Luz.OFF], [Luz.OFF, Luz.OFF], [Luz.OFF, Luz.OFF]]),  # Tablero más grande vacío
        ([[Luz.OFF, Luz.ON], [Luz.OFF, Luz.OFF], [Luz.OFF, Luz.OFF]], [[Luz.OFF, Luz.ON], [Luz.OFF, Luz.OFF], [Luz.OFF, Luz.OFF]]),  # Una luz encendida en un tablero grande
    ]
)
def test_to_list(tablero_inicial, esperado):
    tablero = Tablero(len(tablero_inicial[0]), len(tablero_inicial))
    tablero.tablero = tablero_inicial  
    resultado = tablero.to_list()
    assert resultado == esperado  # Verifica que la conversión a lista sea la esperada
    assert type(resultado) == list  # Verifica que el resultado sea una lista
    assert resultado[0][0] == tablero_inicial[0][0]  # Verifica que la primera celda coincide con la original