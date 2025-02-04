from typing import List
import re
import numpy as np
from numpy.typing import ArrayLike


def count_in_text(text: str) -> int:
    return len(re.findall('XMAS', text)) + len(re.findall('SAMX', text))


def is_x(piece: ArrayLike) -> bool:
    right = ''.join([piece[0, 0], piece[1, 1], piece[2, 2]]) in ('MAS', 'SAM')
    left = ''.join([piece[0, 2], piece[1, 1], piece[2, 0]]) in ('MAS', 'SAM')
    return right and left


def screen_content(content_matrix: ArrayLike, window=3) -> List[ArrayLike]:
    pieces_list = []
    for row in range(content_matrix.shape[0]-window+1):
        for col in range(content_matrix.shape[1]-window+1):
            pieces_list.append(content_matrix[row:row+window, col:col+window])

    return pieces_list


def count_words(content: List[str]) -> int:

    content_as_matrix = np.array([list(row) for row in content])

    counter = 0

    for row in content:
        counter += count_in_text(row)

    for col in content_as_matrix.transpose():
        counter += count_in_text(''.join(col))

    for col in range(content_as_matrix.shape[1]):
        diag = content_as_matrix.diagonal(offset=col)
        diag_flipped = np.fliplr(content_as_matrix).diagonal(offset=col)
        counter += count_in_text(''.join(diag))
        counter += count_in_text(''.join(diag_flipped))

    for row in range(1, content_as_matrix.shape[0]):
        diag = content_as_matrix[row:].diagonal(offset=0)
        diag_flipped = np.fliplr(content_as_matrix[row:]).diagonal(offset=0)
        counter += count_in_text(''.join(diag))
        counter += count_in_text(''.join(diag_flipped))

    return counter


def count_x(content: List[str]) -> int:
    content_as_matrix = np.array([list(row) for row in content])
    counter = 0
    pieces = screen_content(content_as_matrix, window=3)
    for p in pieces:
        counter += int(is_x(p))

    return counter


if __name__ == '__main__':
    example = ['MMMSXXMASM',
               'MSAMXMSMSA',
               'AMXSXMAAMM',
               'MSAMASMSMX',
               'XMASAMXAMM',
               'XXAMMXXAMA',
               'SMSMSASXSS',
               'SAXAMASAAA',
               'MAMMMXMMMM',
               'MXMXAXMASX']

    print(count_words(example) == 18)

    with open('inputs/day-4.txt', 'r') as file:
        content_text = []
        for line in file:
            content_text.append(line.replace('\n', ''))

    print(count_words(content_text))
    print(count_x(example) == 9)
    print(count_x(content_text))




