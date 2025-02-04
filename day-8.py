from typing import List, Tuple

import numpy as np
from numpy.typing import ArrayLike
from itertools import product


def read_input(filename: str) -> ArrayLike:
    with open(f'inputs/{filename}', 'r') as file:
        content = []
        for line in file:
            content.append(list(line.replace('\n', '')))

    return np.array(content)


def find_antinodes(antennas: List[Tuple[int, int]], row_max, col_max) -> List[Tuple[int, int]]:
    antinodes = []
    antenna_pairs = [(a, b) for a, b in product(antennas, repeat=2) if a > b]
    for pair in antenna_pairs:
        row_diff = abs(pair[0][0] - pair[1][0])
        col_diff = abs(pair[0][1] - pair[1][1])
        row = pair[0][0] - row_diff
        col = pair[0][1] - col_diff
        if 0 <= row <= row_max and 0 <= col <= col_max:
            antinodes.append((row, col))
        row = pair[1][0] + row_diff
        col = pair[1][1] + col_diff
        if 0 <= row <= row_max and 0 <= col <= col_max:
            antinodes.append((row, col))
    return antinodes


def count_unique_antinodes(puzzle_map: ArrayLike) -> int:
    antennas_dict = {}
    antinodes = set()
    rows, cols = puzzle_map.shape

    for i in range(rows):
        for j in range(cols):
            frequency = puzzle_map[i, j]
            if frequency != '.':
                if frequency not in antennas_dict:
                    antennas_dict[frequency] = list()
                antennas_dict[frequency].append((i, j))
    for antennas in antennas_dict.values():
        antinodes.update(find_antinodes(antennas, row_max=rows, col_max=cols))

    return len(antinodes)


if __name__ == '__main__':
    example_map = read_input('day-8-example.txt')
    puzzle_map = read_input('day-8.txt')

    print(count_unique_antinodes(example_map))
    print(count_unique_antinodes(puzzle_map))

