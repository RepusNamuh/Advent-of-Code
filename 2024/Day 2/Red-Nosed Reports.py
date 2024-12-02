with open("2024\Day 2\Red-Nosed Reports.txt") as f:
    reports = []
    for line in f:
        reports.append(list(map(int, line.split())))

def report_check(report):
    inOrder = False
    inRange = True
    if report == sorted(report) or report == sorted(report, reverse=True):
        inOrder = True
    for i in range(0, len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        if diff < 1 or diff > 3:
            inRange = False
            break
    return inOrder and inRange

def part1(reports):
    safe_count = 0
    for report in reports:
        if report_check(report):
            safe_count += 1
    return safe_count

def part2(reports):
    safe_count = 0
    for report in reports:
        good = False
        for i in range(len(report)):
            temp = report[:i] + report[i + 1:] # This part here remove one element from the list 
            if report_check(temp):
                good = True
        if good:
            safe_count += 1
    return safe_count

print(part1(reports))
print(part2(reports))



