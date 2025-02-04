from typing import List, Tuple
from numpy.typing import ArrayLike
import numpy as np


INSTRUCTIONS = {'^': (-1, 0, '>'), '<': (0, -1, '^'), '>': (0, 1, 'v'), 'v': (1, 0, '<')}


def find_guard(map_layout: ArrayLike) -> Tuple[str, int, int]:
    for i in range(map_layout.shape[0]):
        for j in range(map_layout.shape[1]):
            if map_layout[i, j] in ('^', '<', '>', 'v'):
                return map_layout[i, j], i, j


def is_map_a_loop(map_layout: ArrayLike) -> bool:
    current_direction, current_row, current_col = find_guard(map_layout)
    tracker = list()
    tracker.append((current_direction, current_row, current_col))
    while current_row not in (0, map_layout.shape[0]-1) and current_col not in (0, map_layout.shape[1]-1):
        next_grid = (current_row + INSTRUCTIONS[current_direction][0], current_col + INSTRUCTIONS[current_direction][1])
        if map_layout[next_grid[0], next_grid[1]] == '#':
            current_direction = INSTRUCTIONS[current_direction][2]
        else:
            current_row = current_row + INSTRUCTIONS[current_direction][0]
            current_col = current_col + INSTRUCTIONS[current_direction][1]
            if (current_direction, current_row, current_col) in tracker:
                return True
            tracker.append((current_direction, current_row, current_col))

    return False


def find_covered_territory(map_layout: ArrayLike) -> int:
    current_direction, current_row, current_col = find_guard(map_layout)
    path_tracker = np.zeros((map_layout.shape[0], map_layout.shape[1]))
    path_tracker[current_row, current_col] = 1
    while current_row not in (0, map_layout.shape[0]-1) and current_col not in (0, map_layout.shape[1]-1):
        next_grid = (current_row + INSTRUCTIONS[current_direction][0], current_col + INSTRUCTIONS[current_direction][1])
        if map_layout[next_grid[0], next_grid[1]] == '#':
            current_direction = INSTRUCTIONS[current_direction][2]
        else:
            current_row = current_row + INSTRUCTIONS[current_direction][0]
            current_col = current_col + INSTRUCTIONS[current_direction][1]
            path_tracker[current_row, current_col] = 1

    return int(path_tracker.sum())


def count_potential_obstacles(map_layout: ArrayLike) -> int:
    counter = 0
    for i in range(map_layout.shape[0]):
        for j in range(map_layout.shape[1]):
            if map_layout[i, j] in ('#', '^', '<', '>', 'v'):
                continue
            map_layout_copy = map_layout.copy()
            map_layout_copy[i, j] = '#'
            counter += int(is_map_a_loop(map_layout_copy))

        print(f'Row {i} covered')

    return counter


if __name__ == '__main__':
    with open('inputs/day-6-example.txt', 'r') as file:
        example_map = []
        for line in file:
            example_map.append(list(line.replace('\n', '')))
        example_map = np.array(example_map)

    with open('inputs/day-6.txt', 'r') as file:
        map_layout = []
        for line in file:
            map_layout.append(list(line.replace('\n', '')))
        map_layout = np.array(map_layout)

    print(find_covered_territory(example_map))
    print(find_covered_territory(map_layout))
    print(count_potential_obstacles(example_map))
    print(count_potential_obstacles(map_layout))

