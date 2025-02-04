from typing import List, Tuple
from itertools import product


def load_file(filename: str) -> List[Tuple[int, List[int]]]:
    with open(f'inputs/{filename}', 'r') as file:
        puzzle_input = []
        for line in file:
            result = int(line.split(': ')[0])
            inputs = [int(inp) for inp in line.split(': ')[1].replace('\n', '').split(' ')]
            puzzle_input.append((result, inputs))
    return puzzle_input


def can_equation_be_true(equation: Tuple[int, List[int]], has_concat=False) -> bool:
    result, inputs = equation
    if has_concat:
        possible_operators = [ops for ops in product(['*', '+', '||'], repeat=len(inputs) - 1)]
    else:
        possible_operators = [ops for ops in product(['*', '+'], repeat=len(inputs)-1)]

    for operators in possible_operators:
        equation_result = inputs[0]
        for i, operator in enumerate(operators):
            if equation_result > result:
                break
            if operator == '||':
                equation_result = eval(f'{equation_result}{inputs[i+1]}')
            else:
                equation_result = eval(f'{equation_result}{operator}{inputs[i+1]}')
        if equation_result == result:
            return True

    return False


def calculate_total_calibration_result(equations: List[Tuple[int, List[int]]], has_concat=False) -> int:
    sum_of_true_equations = 0
    for i, equation in enumerate(equations):
        if can_equation_be_true(equation, has_concat=has_concat):
            result, _ = equation
            sum_of_true_equations += result
        if i % 50 == 0:
            print(f'{i} equations done')
    return sum_of_true_equations


if __name__ == '__main__':
    example_input = load_file('day-7-example.txt')
    puzzle_input = load_file('day-7.txt')

    print(calculate_total_calibration_result(example_input) == 3749)
    print(calculate_total_calibration_result(puzzle_input))
    print(calculate_total_calibration_result(example_input, has_concat=True) == 11387)
    print(calculate_total_calibration_result(puzzle_input, has_concat=True))
