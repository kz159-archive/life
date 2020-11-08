"""
Conway game of live implementation
"""
from time import sleep
from typing import List
from random import randrange


ARRAY = [[0, 0, 0, 0, 0, 0, 0, 0] for i in range(8)]
ALIVE_CELL = '■'
ALIVE_CELL_NUM = 1
DEAD_CELL = ' '
DEAD_CELL_NUM = 0

def generate_universe(array) -> List[List]:
    result = []
    for num, row in enumerate(array):
        result.append([])
        for cell in row:
            if randrange(start=0, stop=100, step=2) > 69:
                result[num].append(1)
            else:
                result[num].append(0)

    return result


def next_turn(array: list) -> List[List]:
    result = array[:]
    for y, row in enumerate(array):
        for x, cell in row:
            neighbors = find_neighbors(array, x, y)
            if neighbors == 3 and cell == DEAD_CELL_NUM:
                result[x][y] = ALIVE_CELL_NUM
            if (neighbors == 2 or neighbors == 3) and cell == ALIVE_CELL_NUM:
                continue
            if (neighbors > 3 or neighbors < 2) and cell == ALIVE_CELL_NUM:
                result[x][y] = DEAD_CELL_NUM
    return result


def find_neighbors(array: list, x: int, y: int) -> int:
    num = 0

    if array[y+1][x]:
        num += 1
    if array[y-1][x]:
        num += 1
    if array[y+1][x+1]:
        num += 1
    if array[y+1][x-1]:
        num += 1

    return num


def clear():
    print('\n'*10)


def print_array(array):
    for row in array:
        for cell in row:
            if cell:
                print(ALIVE_CELL, end=' ')
            else:
                print(DEAD_CELL, end=' ')
        print()


def spin(array):
    array = generate_universe(array)
    while True:
        print_array(array)
        sleep(1)
        clear()
        array = next_turn(array)


# spin(ARRAY)
