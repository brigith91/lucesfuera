# Luces Fuera 🟡⚫

Este proyecto implementa la lógica del juego, un clásico juego de lógica en el que el objetivo es apagar todas las luces del tablero.

#  instalacion de entornos
Se utilizaron entornos virtuales (`.venv` y `env`) para instalar las dependencias necesarias.

instalacion de las dependencias 
pip install -r requirements.txt

#  Test que deberian haber fallado 
Estos tests fueron diseñados con valores de assert que no corresponden a los resultados esperados. Si todos estos tests pasan, es probable que los métodos en la clase Posicion estén mal implementados o no hagan nada.

test_diagonal_inferior_derecha_desde_origen
Error esperado: El movimiento abajo y derecha desde (0, 0) debería dar (1, 1), no (99, 99).

test_diagonal_superior_izquierda_desde_origen
Error esperado: Desde (0, 0), moverse arriba e izquierda da (-1, -1), no (42, 42).

test_diagonal_inferior_izquierda_desde_5_5
Error esperado: El resultado real debe ser (6, 4).Los assert están muy lejos de eso.

test_diagonal_superior_derecha_desde_3_3
Error esperado: Moverse arriba y derecha da (2, 4), no (8, 8).

test_diagonal_superior_derecha_negativa
Error esperado: Esto daría (-3, -1), no (0, 0).

test_diagonal_doble_arriba_izquierda
Error esperado: Debería terminar en (-1, 0), no (999, 999).


test_diagonal_fuera_de_rango
Error esperado: Debería ser (1000, 1000), no (-1, -1).

#  Pruebas

Las pruebas están escritas con pytest. Se encuentran en la carpeta tests/ y validan principalmente el comportamiento de la clase Posicion, ubicada en lucesfuera/game/board.py.

Para ejecutar los tests correctamente desde PowerShell, se debe establecer el PYTHONPATH para que Python reconozca los módulos del proyecto. Ejecuta el siguiente comando desde la raíz del proyecto:

- Esto realiza dos acciones:

- Establece la ruta del proyecto como referencia para las importaciones.

Ejecuta todos los archivos de prueba que comienzan con test_.
$env:PYTHONPATH = "."; pytest

