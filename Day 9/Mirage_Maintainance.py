with open("Day 9\Mirage_Maintainance.txt", 'r') as f:
    report = f.read()

total = 0
total_1 = 0
def zero_list_check(sequence):
    if all(num == 0 for num in sequence):
        return False
    return True

for line in report.split("\n"):
    history = list(map(int, line.split()))
    first_num = []
    while zero_list_check(history):
        sequence = []
        for i in range(len(history) - 1 ):
            sequence.append(history[i + 1] - history[i])
        first_num.insert(0, history[0])
        total += history[-1]
        history = sequence.copy()
    diff = 0
    for i in range(len(first_num)):
        diff = first_num[i] - diff
    total_1 += diff

        
print(total, total_1)

    