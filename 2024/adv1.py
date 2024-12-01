def parse_input(file: str = "./inputs/1.txt"):
    left_values, right_values = [], []
    with open(file, "r") as f:
        for line in f:
            left, right = line.strip().split(3*" ")
            left_values.append(int(left))
            right_values.append(int(right))
    return left_values, right_values

def part_1(left_values, right_values):
    left, right = sorted(left_values), sorted(right_values)
    distances = [abs(left[i]-right[i]) for i in range(len(left_values))]
    return sum(distances)

def part_2(left_values, right_values):
    previous_frequency = None
    previous_number = None
    frequency_list = []
    for number in sorted(left_values):
        if number == previous_number:
            frequency_list.append(previous_frequency)
        else:
            previous_number = number
            frequency = number * len([v for v in right_values if v==number])
            frequency_list.append(frequency)
            previous_frequency = frequency
    return sum(frequency_list)

if __name__ == '__main__':
    print("Part 1:", part_1(*parse_input()))
    print("Part 2:", part_2(*parse_input()))
