from typing import List


def calc_report_diffs(report: List[int]) -> List[int]:
    return [b-a for a, b in zip(report, report[1:])]


def assess_safetiness(report: List[int], with_tolerance=False) -> bool:
    report_diffs = calc_report_diffs(report)
    if max([abs(diff) for diff in report_diffs]) <= 3 and report_diffs.count(0) == 0 and max(report_diffs) * min(report_diffs) > 0:
        return True

    if with_tolerance:
        for i in range(len(report)):
            report_modified = report[:i] + report[i+1:]
            report_diffs = calc_report_diffs(report_modified)
            if max([abs(diff) for diff in report_diffs]) <= 3 and report_diffs.count(0) == 0 and max(report_diffs) * min(report_diffs) > 0:
                return True
    return False


def calculate_safe_reports(reports: List[List[int]], with_tolerance=False) -> int:
    return sum([assess_safetiness(report, with_tolerance=with_tolerance) for report in reports])


if __name__ == '__main__':

    with open('inputs/day-2.txt', 'r') as file:
        reports = []
        for line in file:
            reports.append([int(level) for level in line.split()])

    example = [[7, 6, 4, 2, 1],
               [1, 2, 7, 8, 9],
               [9, 7, 6, 2, 1],
               [1, 3, 2, 4, 5],
               [8, 6, 4, 4, 1],
               [1, 3, 6, 7, 9]]

    print(calculate_safe_reports(example) == 2)
    print(calculate_safe_reports(reports))
    print(calculate_safe_reports(example, with_tolerance=True) == 4)
    print(calculate_safe_reports(reports, with_tolerance=True))

