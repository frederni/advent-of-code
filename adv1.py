import re
DEBUG = False
written_num_to_int = {
		"one":  1,
		"two":   2,
		"three": 3,
		"four":  4,
		"five":  5,
		"six":   6,
		"seven": 7,
		"eight": 8,
		"nine":  9,
}
numbers_group =  "|".join(written_num_to_int.keys())

def num_to_int_pad(num):
    """Returns dictionary value as string maintaining original string size"""
    return str(written_num_to_int[num]).ljust(len(num))


with open("1/input1.txt", 'r') as f:
    lines = f.readlines()

total_sum = 0

for line in lines:
    line = line.strip()
    new_string = [c for c in line]

    # Find matching numbers accounting for overlap
    matches = re.findall(r"(?=(" + "|".join(written_num_to_int.keys()) + r"))", line)
    
    repl_list = []
    for match in matches:
        repl_list.append(re.sub(match, num_to_int_pad(match), line))
    # Replace original string with numeric
    for repl in repl_list:
        for i, char in enumerate(repl):
            if char.isnumeric():
                new_string[i] = char
    
    replaced_string = "".join(new_string)

    # Find numerics and get coordinate for row
    matched_nums = re.findall(r"\d", replaced_string)
    assert len(matched_nums) > 0

    last_idx = 0 if len(matched_nums) == 1 else -1 
    row_numbers = int(matched_nums[0] + matched_nums[last_idx])
    if DEBUG:
        with open("output1.txt", "a") as f:
            f.write(f"{row_numbers}\n")
    total_sum += row_numbers

print(total_sum)

