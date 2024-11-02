def parse_input(filename: str = "input9.txt"):
    with open(filename, "r") as f:
        return [[int(x) for x in line.strip().split()] for line in f]

def part_1(oasis):
    sum_extr = 0
    for reading in oasis:
        all_zero = False
        last_values = [reading[-1]]
        diffs = reading
        while not all_zero:
            # Get pairwise difference between each int in reading
            diffs = [b - a for a, b in zip(diffs, diffs[1:])]
            last_values.append(diffs[-1])
            all_zero = all(d == 0 for d in diffs)
        extrap_value = sum(last_values)
        sum_extr += extrap_value
    return sum_extr

def part_2(oasis):
    sum_extr = 0
    for reading in oasis:
        all_zero = False
        first_values = [reading[0]]
        diffs = reading
        while not all_zero:
            # Get pairwise difference between each int in reading
            diffs = [b - a for a, b in zip(diffs, diffs[1:])]
            first_values.append(diffs[0])
            all_zero = all(d == 0 for d in diffs)
        extrap_value = 0
        for i, v in enumerate(first_values):
            if i%2==0:
                extrap_value -= v
            else:
                extrap_value += v
        sum_extr -= extrap_value
    return sum_extr

if __name__ == '__main__':
    oasis = parse_input()
    print("Part 1:", part_1(oasis))
    print("Part 2:", part_2(oasis))