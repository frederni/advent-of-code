def parse_input(filename="input5.txt"):
    with open(filename, "r") as f:
        data = f.read()
    rules, updates = data.split("\n\n")
    # Parse rules
    rules = rules.split("\n")
    ahead_dict, behind_dict = {}, {}
    for rule in rules:
        ahead, behind = rule.split("|")
        ahead_dict.setdefault(int(ahead), []).append(int(behind))
        behind_dict.setdefault(int(behind), []).append(int(ahead))

    # Parse updates
    updates = updates.split("\n")
    updates = [[int(num) for num in u.split(",")] for u in updates]

    return ahead_dict, behind_dict, updates

def get_valid_updates(updates, ahead_dict, behind_dict):
    valid_updates = []
    for update in updates:
        current_valid = True
        for i, num in enumerate(update):
            ahead_list = ahead_dict.get(num, [])
            behind_list = behind_dict.get(num, [])
            ahead_nums = update[:i]
            behind_nums = update[i+1:]
            # If any numbers ahead are in behind list, the update is invalid
            # If any numbers behind are in the ahead list, the update is invalid
            if set(ahead_nums) & set(ahead_list) or set(behind_nums) & set(behind_list):
                current_valid = False
                break
        if current_valid:
            valid_updates.append(update)
    return valid_updates

def part_1(ahead_dict, behind_dict, updates):
    valid_updates = get_valid_updates(updates, ahead_dict, behind_dict)
    return sum(vu[len(vu)//2] for vu in valid_updates)

def part_2(ahead_dict, behind_dict, updates):
    valid_updates = get_valid_updates(updates, ahead_dict, behind_dict)
    invalid_updates = [u for u in updates if u not in valid_updates]
    print(invalid_updates)


if __name__ == '__main__':
    ahead_list, behind_list, updates = parse_input("inputs/5.txt")
    print("Part 1:", part_1(ahead_list, behind_list, updates))
    print("Part 2:", part_2(ahead_list, behind_list, updates))
