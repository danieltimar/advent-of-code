from typing import List


def calculate_distances_between_lists(list_1: List[int], list_2: List[int]) -> int:
    return sum([abs(left - right) for left, right in zip(sorted(list_1), sorted(list_2))])


def calculate_similarity_score(list_1: List[int], list_2: List[int]) -> int:
    counts = [list_2.count(i) for i in list_1]
    return sum([left * count for count, left in zip(counts, list_1)])


if __name__ == '__main__':
    print(calculate_distances_between_lists([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]) == 11)

    with open('inputs/day-1.txt', 'r') as f:
        col_1 = []
        col_2 = []

        for line in f:
            parts = line.split()

            col_1.append(int(parts[0]))
            col_2.append(int(parts[1]))

    print(calculate_distances_between_lists(col_1, col_2))

    print(calculate_similarity_score([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]) == 31)
    print(calculate_similarity_score(col_1, col_2))