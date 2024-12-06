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

def is_valid_update(update, ahead_dict, behind_dict):
    for i, num in enumerate(update):
        ahead_list = ahead_dict.get(num, [])
        behind_list = behind_dict.get(num, [])
        ahead_nums = update[:i]
        behind_nums = update[i+1:]
        if set(ahead_nums) & set(ahead_list) or set(behind_nums) & set(behind_list):
            return False
    return True


def get_valid_updates(updates, ahead_dict, behind_dict):
    valid_updates = []
    for update in updates:
        if is_valid_update(update, ahead_dict, behind_dict):
            valid_updates.append(update)
    return valid_updates

def part_1(ahead_dict, behind_dict, updates):
    valid_updates = get_valid_updates(updates, ahead_dict, behind_dict)
    return sum(vu[len(vu)//2] for vu in valid_updates)

def part_2(ahead_dict, behind_dict, updates):
    valid_updates = get_valid_updates(updates, ahead_dict, behind_dict)
    invalid_updates = [u for u in updates if u not in valid_updates]
    fixed_updates = []
    for update in invalid_updates:
        while not is_valid_update(update, ahead_dict, behind_dict):
            for i, num in enumerate(update):
                ahead_list = ahead_dict.get(num, [])
                behind_list = behind_dict.get(num, [])
                ahead_nums = update[:i]
                behind_nums = update[i + 1 :]
                should_be_after = set(ahead_nums) & set(ahead_list)
                should_be_before = set(behind_nums) & set(behind_list)
                if should_be_before:
                    update[i], update[i + len(should_be_before)] = (
                        update[i + len(should_be_before)],
                        update[i],
                    )
                elif should_be_after:
                    update[i], update[i - len(should_be_after)] = (
                        update[i - len(should_be_after)],
                        update[i],
                    )
        fixed_updates.append(update)
    return sum(vu[len(vu) // 2] for vu in fixed_updates)


if __name__ == '__main__':
    ahead_list, behind_list, updates = parse_input("inputs/5.txt")
    print("Part 1:", part_1(ahead_list, behind_list, updates))
    print("Part 2:", part_2(ahead_list, behind_list, updates))
