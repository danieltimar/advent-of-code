from typing import List, Tuple


def find_page_pairs(manual: List[str]) -> List[List[str]]:
    manual_length = len(manual)
    page_pairs = []
    for i in range(manual_length):
        for j in range(manual_length):
            if i > j:
                page_pairs.append([manual[i], manual[j]])

    return page_pairs


def is_manual_correct(rules: List[str], manual: List[str]) -> bool:
    page_pairs = find_page_pairs(manual)

    for rule in rules:
        if rule in page_pairs:
            return False

    return True


def reorder_pages(rules: List[str], manual: List[str]) -> List[str]:
    manual_copy = manual.copy()
    while not is_manual_correct(rules, manual_copy):
        page_pairs = find_page_pairs(manual_copy)
        for rule in rules:
            if rule in page_pairs:
                index_1 = manual_copy.index(rule[0])
                index_2 = manual_copy.index(rule[1])
                manual_copy[index_1] = rule[1]
                manual_copy[index_2] = rule[0]
                break
    return manual_copy


def calculate_sum_of_correct(rules: List[str], manuals: List[List[str]]) -> Tuple[int, int]:
    sum_of_correct = 0
    sum_of_reordered = 0
    for manual in manuals:
        if is_manual_correct(rules, manual):
            sum_of_correct += int(manual[len(manual) // 2])
        else:
            reordered_manual = reorder_pages(rules, manual)
            sum_of_reordered += int(reordered_manual[len(reordered_manual) // 2])

    return sum_of_correct, sum_of_reordered


if __name__ == '__main__':
    with open('inputs/day-5-example.txt') as file:
        is_rule = True
        rules_example = []
        manuals_example = []
        for line in file:
            if line == '\n':
                is_rule = False
                continue
            if is_rule:
                rules_example.append(line.replace('\n', '').split('|'))
            else:
                manuals_example.append(line.replace('\n', '').split(','))

    with open('inputs/day-5.txt') as file:
        is_rule = True
        rules = []
        manuals = []
        for line in file:
            if line == '\n':
                is_rule = False
                continue
            if is_rule:
                rules.append(line.replace('\n', '').split('|'))
            else:
                manuals.append(line.replace('\n', '').split(','))

    print(calculate_sum_of_correct(rules_example, manuals_example)[0] == 143)
    print(calculate_sum_of_correct(rules, manuals)[0])
    print(calculate_sum_of_correct(rules_example, manuals_example)[1] == 123)
    print(calculate_sum_of_correct(rules, manuals)[1])
