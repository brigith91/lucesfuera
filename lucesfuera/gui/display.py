import string

from rich.console import Console
from rich.panel import Panel

from lucesfuera.game.board import Posicion
from lucesfuera.game.luz import Luz

console = Console()
SIMBOLOS = {
    Luz.OFF: "○",
    Luz.ON: "●",
}


def _nombres_filas() -> str:
    return string.ascii_uppercase


def _nombres_columnas() -> str:
    return string.ascii_lowercase


def clear_screen() -> None:
    """
    Limpia la pantalla de la terminal
    """
    console.clear()


def print_title(title) -> None:
    """
    Se imprime el titulo indicado por parametro dentro de una caja

    Parameters
    ----------
    title : str
        Titulo del texto
    """
    console.print()
    console.print(
        Panel.fit(f"[bold]{title}[/bold]", padding=(1, 10), border_style="green")
    )
    console.print()


def _fit_tablero(tablero: list[list[str]]) -> Panel:
    """
    Devuelve el tablero en formato de texto con el texto enriquecido

    Parameters
    ----------
    tablero : list[list[str]]
        Tablero de luces

    Returns
    -------
    str
        Tablero en formato de texto
    """
    filas: str = _nombres_filas()
    columnas: str = _nombres_columnas()
    fit_columnas: str = " ".join(columnas[: len(tablero[0])])

    tablero_str = f"  [bold][blue]{fit_columnas}[/blue][/bold] \n"

    for i, fila in enumerate(tablero):
        tablero_str += f"[bold][blue]{filas[i]}[/blue][/bold] "

        for columna in fila:
            tablero_str += f"{SIMBOLOS[columna]} "

        tablero_str += "\n"

    return Panel.fit(tablero_str[:-1], padding=(1, 8), border_style="blue")


def imprimir_tablero(tablero: list[list[str]]) -> None:
    panel: Panel = _fit_tablero(tablero)
    console.print(panel)


def get_posicion() -> Posicion | str:
    pos: str = console.input("  [bold cyan]Ingrese la posición: [/bold cyan]")

    if pos == "exit":
        return pos

    fila_str: str = pos[0] if pos[0].isupper() else pos[1]
    columna_str: str = pos[1] if pos[0].isupper() else pos[0]

    fila: int = _nombres_filas().index(fila_str)
    columna: int = _nombres_columnas().index(columna_str)

    return Posicion(fila, columna)
