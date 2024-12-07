from typing import List
import re


def calculate_result(content: str, include_dos=False) -> int:

    if include_dos:
        relevant_content = re.findall(r"(do(?:n't)?\(\))|mul\(([0-9]{,3})\,([0-9]{,3})\)", content)
        result = 0
        is_do = True
        for a, b, c in relevant_content:
            if a in ("do()", "don't()"):
                is_do = True if a == "do()" else False

            if a == '' and is_do:
                result += int(b) * int(c)

        return result

    numbers_to_multiply = re.findall(r'mul\(([0-9]{,3})\,([0-9]{,3})\)', content)
    return sum((int(a) * int(b) for a, b in numbers_to_multiply))


if __name__ == '__main__':

    with open('inputs/day-3.txt') as file:
        content = []
        for line in file:
            content.append(line)
            content_text = ''.join(content)

example_1 = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
example_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
print(calculate_result(example_1) == 161)
print(calculate_result(content_text))
print(calculate_result(example_2, include_dos=True)==48)
print(calculate_result(content_text, include_dos=True))
