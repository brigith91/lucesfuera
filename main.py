from lucesfuera.game.board import Posicion, Tablero
from lucesfuera.gui import display


def end_game() -> None:
    display.clear_screen()
    display.print_title("Bye!\nGracias por jugar!")


def game(tablero: Tablero) -> None:
    while not tablero.is_resuelto():
        display.clear_screen()
        display.print_title("Luces Fuera")
        display.imprimir_tablero(tablero.to_list())
        posicion: Posicion = display.get_posicion()
        if posicion == "exit":
            end_game()
            return
        tablero.switch_luz(posicion)


if __name__ == "__main__":
    tablero: Tablero = Tablero(6, 6)
    tablero.prender_apagar(Posicion(1, 2))
    game(tablero)
