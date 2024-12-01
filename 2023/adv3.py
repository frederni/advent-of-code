import re


def get_symbol_list(filename):
    """Scans over input to get set of symbols"""
    symbols = set()
    with open(filename, 'r') as f:
        data = f.read()
    for char in data.strip():
        if not char.isnumeric() and char != "." and char != "\n":
            symbols.add(char)
    return symbols

with open("input3.txt", 'r') as f:
    schematic = f.readlines()

potential_part_numbers = []
for row, line in enumerate(schematic):
    matches = re.finditer(r"\d+", line.strip())
    for match in matches:
        potential_part_numbers.append( {
            "number": match.group(0),
            "r_coords": [row-1, row, row+1],
            "c_coords": list(range(match.start(0)-1, match.end(0) + 1))
            } )

part_number_sum = 0
gear_ratio_sum = 0
symbols = get_symbol_list("input3.txt")
for row, line in enumerate(schematic):
    for col, chr in enumerate(line.strip()):
        if chr in symbols:
            gear_list = []
            for idx, pot_number in enumerate(potential_part_numbers):
                if row in pot_number["r_coords"] and \
                col in pot_number["c_coords"] and \
                pot_number["number"] != "used":
                    part_number = int(pot_number["number"])
                    gear_list.append(part_number)
                    part_number_sum += part_number
                    potential_part_numbers[idx]["number"] = "used"
            if len(gear_list) == 2:
                gear_ratio_sum += gear_list[0]*gear_list[1]
print(f"{part_number_sum = }")
print(f"{gear_ratio_sum = }")