data = []
with open("inputs/7.txt", "r") as f:
    for line in f:
        product, terms = line.strip().split(": ", 1)
        data.append({"product": int(product), "terms": terms})


def apply_left_to_right(expression):
    stack = []
    operators = set(["+", "*", "|"])
    num = ""

    for token in expression:
        if token in operators:
            stack.append(float(num))
            num = ""
            stack.append(token)
        else:
            num += token

    stack.append(float(num))

    result = stack[0]
    for i in range(1, len(stack), 2):
        operator = stack[i]
        operand = stack[i + 1]
        if operator == "+":
            result += operand
        elif operator == "*":
            result *= operand
        elif operator == "|": # concat
            result = int(str(int(result))+str(int(operand)))


    return result


import itertools
def day_7(part_2=False):
    valid_products = []
    for d in data:
        terms = d['terms'].split()
        combinations = []
        operations = ['+', '*']
        if part_2:
            operations.append('|')
        for ops in itertools.product(operations, repeat=len(terms) - 1):
            expression = ''.join(t + o for t, o in zip(terms, ops)) + terms[-1]
            combinations.append(expression)
        for c in combinations:
            if apply_left_to_right(c) == d['product']:
                valid_products.append(d['product'])
    print(sum(set(valid_products)))

if __name__ == "__main__":
    # Slow and brute-forcy, but it works ¯\_(ツ)_/¯
    day_7()
    day_7(part_2=True)
