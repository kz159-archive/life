"""
Conway game of live implementation
"""
from time import sleep
from typing import List
from random import randrange
from os import system, get_terminal_size
from copy import deepcopy


terminal = get_terminal_size()

ARRAY = [[0 for l in range(terminal.columns//2)] for i in range(terminal.lines-2)]
glider = [[0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 1, 0],
          [0, 0, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 0]]
good_glider = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
ALIVE_CELL = '■'
ALIVE_CELL_NUM = 1
DEAD_CELL = '.'
DEAD_CELL_NUM = 0
PERCENT = 80


def generate_universe(array) -> List[List]:
    result = []
    for num, row in enumerate(array):
        result.append([])
        for cell in row:
            if randrange(start=0, stop=100, step=2) > PERCENT:
                result[num].append(1)
            else:
                result[num].append(0)

    return result


def next_turn(array: list) -> List[List]:
    result = deepcopy(array)
    for y, row in enumerate(array):
        for x, cell in enumerate(row):
            neighbors = count_neighbors(array, x, y)
            if neighbors == 3 and cell == DEAD_CELL_NUM:
                result[y][x] = ALIVE_CELL_NUM
            if (neighbors == 2 or neighbors == 3) and cell == ALIVE_CELL_NUM:
                continue
            if (neighbors > 3 or neighbors < 2) and cell == ALIVE_CELL_NUM:
                result[y][x] = DEAD_CELL_NUM
    return result


def count_neighbors(array: list, x: int, y: int) -> int:
    num = 0

    try:
        if array[y+1][x]:
            num += 1
    except IndexError:
        pass

    try:
        if array[y+1][x+1]:
            num += 1
    except IndexError:
        pass

    try:
        if array[y+1][x-1]:
            num += 1
    except IndexError:
        pass

    try:
        if array[y-1][x]:
            num += 1
    except IndexError:
        pass

    try:
        if array[y-1][x+1]:
            num += 1
    except IndexError:
        pass

    try:
        if array[y-1][x-1]:
            num += 1
    except IndexError:
        pass

    try:
        if array[y][x+1]:
            num += 1
    except IndexError:
        pass

    try:
        if array[y][x-1]:
            num += 1
    except IndexError:
        pass

    return num


def clear():
    system('clear')


def print_array(array):
    for row in array:
        for cell in row:
            if cell:
                print(ALIVE_CELL, end=' ')
            else:
                print(DEAD_CELL, end=' ')
        print()
    print(f'Space - pause, {terminal}', end='\n')


def spin(array):
    clear()
    while True:
        print_array(array)
        sleep(0.5)
        clear()
        array = next_turn(array)


spin(generate_universe(ARRAY))
