import sys
from typing import List, Union

board: List[List[Union[int, str]]] = [[0, 0, 0],
                                      [0, 0, 0],
                                      [0, 0, 0]]


def draw_board() -> None:
    print('')
    for line, row in enumerate(board):
        for index, cell in enumerate(row):
            print(f' {cell}', end=' |' if index != 2 else '')

        if line != 2:
            print('\n-----------')


def is_empty(row: int, cell: int) -> bool:
    return not bool(board[row][cell])


def check_game_over(symbol, gamer) -> None:
    win_states = (
        (board[0][0], board[0][1], board[0][2]),
        (board[1][0], board[1][1], board[1][2]),
        (board[2][0], board[2][1], board[2][2]),
        (board[0][0], board[1][0], board[2][0]),
        (board[0][1], board[1][1], board[2][1]),
        (board[0][2], board[1][2], board[2][2]),
        (board[0][2], board[1][1], board[2][0]),
        (board[0][0], board[1][1], board[2][2]),
    )

    for state in win_states:
        if all(cell == symbol for cell in state):
            print(f'\n\nИгрок {gamer} победил!')
            sys.exit()

    rows = sum(board, [])
    if all(cell != 0 for cell in rows):  # проверка на то, что все клетки заняты
        print(f'\n\nНичья!')
        sys.exit()


def turn(gamer: int) -> None:
    symbol = 'X' if gamer == 1 else 'Y'  # Y вместо O, чтобы не путать с 0
    print(f'\n\nХод {gamer}-го игрока.')

    while True:
        print(f'Куда поставить {symbol}?')
        row = int(input('Ряд (0-2): '))
        cell = int(input('Клетка (0-2): '))

        try:
            if is_empty(row, cell):
                board[row][cell] = symbol
                break
            else:
                print('\nКлетка занята!\n')
        except IndexError:
            print('\nРяд и клетка - это числа в диапазоне от 0 до 2!\n')

    draw_board()
    check_game_over(symbol, gamer)


def main() -> None:
    draw_board()

    while True:
        try:
            turn(gamer=1)
            turn(gamer=2)
        except KeyboardInterrupt:
            print('\n\nИгра завершена')
            sys.exit()


if __name__ == '__main__':
    main()
