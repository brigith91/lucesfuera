# Luces Fuera 🟡⚫

Este proyecto implementa la lógica del juego, un clásico juego de lógica en el que el objetivo es apagar todas las luces del tablero,para las clases Posicion y Tablero.

#  instalacion de entornos
Se utilizaron entornos virtuales (`.venv` y `env`) para instalar las dependencias necesarias.

instalacion de las dependencias 
pip install -r requirements.txt

# Estructura del Proyecto
El código se organiza en dos módulos principales:

lucesfuera.game.board:

Define la clase Tablero que representa el tablero del juego.

Define la clase Posicion que representa una posición en el tablero.

lucesfuera.game.luz:

Define la clase Luz que puede estar encendida (ON) o apagada (OFF).

# Estructura del Proyecto
1. Clase Posicion
La clase Posicion maneja las coordenadas de una posición en el tablero, representadas por fila y columna. Los métodos de la clase permiten mover la posición de diferentes formas

2. Clase Tablero
La clase Tablero representa un tablero de juego donde las luces pueden ser encendidas o apagadas. El tablero es una matriz de objetos Luz, y se utiliza el siguiente método para manipular el tablero.

3. Clase Luz
La clase Luz tiene dos estados posibles:

Luz.OFF: La luz está apagada.
Luz.ON: La luz está encendida.

# Pruebas Unitarias
Las pruebas unitarias están organizadas en varios conjuntos de pruebas utilizando la librería pytest. Las pruebas cubren varios aspectos del juego:

1. Pruebas de Posición
Se verifica si las posiciones se mueven correctamente en las direcciones especificadas (derecha, izquierda, diagonal derecha arriba, diagonal izquierda arriba).

Se incluyen pruebas que validan los movimientos en los bordes del tablero y aseguran que las posiciones sean correctas.

2. Pruebas de Tablero
Se comprueba la correcta creación del tablero .

Se realiza la prueba de encender y apagar luces en varias posiciones del tablero y se valida que el estado de las luces en el tablero sea el esperado.
