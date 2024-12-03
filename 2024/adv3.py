import re
def part_1(input):
    with open(input, 'r') as f:
        data = f.read()
    valid_muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)
    products = [eval(s) for s in valid_muls]
    return sum(products)

def part_2(input):
    with open(input, "r") as f:
        data = f.read()
    valid_funcs = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", data)
    mult_enabled = True
    sum_products = 0
    for func in valid_funcs:
        if func == "do()":
            mult_enabled = True
        elif func == "don't()":
            mult_enabled = False
        elif mult_enabled:
            sum_products += eval(func)
    return sum_products
        
def mul(a, b):
    return a*b

if __name__ == '__main__':
    print(
        "Part 1:", part_1("./inputs/3.txt"),
        "Part 2:", part_2("./inputs/3.txt")

        )
