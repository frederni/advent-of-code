import re

def mul(a, b):
    """Define mult as a function to take use of `eval`"""
    return a * b

def get_data(input_path: str) -> str:
    """Read data"""
    with open(input_path, 'r', encoding="utf-8") as f:
        data = f.read()
    return data

def part_1(input_path: str) -> int:
    """Solve part 1 of day 3"""
    data = get_data(input_path)
    valid_muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)
    # Regex: \d{1,3} yields all numbers between 1 and 3 digits
    return sum(eval(s) for s in valid_muls)  # pylint: disable=eval-used

def part_2(input_path: str) -> int:
    """Solve part 2 of day 3"""
    data = get_data(input_path)
    valid_funcs = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", data)
    # Regex: Pipe | works like or, so we find any of the three valid functions
    mult_enabled = True
    sum_products = 0
    for func in valid_funcs:
        if func == "do()":
            mult_enabled = True
        elif func == "don't()":
            mult_enabled = False
        elif mult_enabled:
            sum_products += eval(func)  # pylint: disable=eval-used
    return sum_products

if __name__ == '__main__':
    print(
        "Part 1:", part_1("./inputs/3.txt"),
        "Part 2:", part_2("./inputs/3.txt")
        )
