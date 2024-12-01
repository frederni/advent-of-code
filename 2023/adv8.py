import math
def parse_input(filename: str = "input8.txt") -> tuple[str, dict]:
    with open(filename, "r") as f:
        directions = f.readline().strip()
        network = f.readlines()[1:]
    network_map = {}
    for line in network:
        line_kv = line.strip().split(" = ")
        network_map[line_kv[0]] = line_kv[1][1:-1].split(", ")
    return directions, network_map

def part_1(directions, network):
    at_end_node = False
    node_key = "AAA"
    step_no = 0
    n_directions = len(directions)
    while not at_end_node:
        step_idx = 0 if directions[step_no % n_directions] == "L" else 1
        node_key = network[node_key][step_idx]
        at_end_node = node_key == "ZZZ"
        step_no += 1
    return step_no

def part_2(directions, network: dict[str, list[str]]):
    node_keys = [k for k in network.keys() if k.endswith("A")]
    steps = []
    for node_key in node_keys:
        at_end_node = False
        step_no = 0
        n_directions = len(directions)
        while not at_end_node:
            step_idx = 0 if directions[step_no % n_directions] == "L" else 1
            node_key = network[node_key][step_idx]
            at_end_node = node_key.endswith("Z")
            step_no += 1
        steps.append(step_no)
    return math.lcm(*steps)


if __name__ == '__main__':
    directions, network = parse_input("input8.txt")
    print("Part 1:", part_1(directions, network))
    print("Part 2:", part_2(directions, network))
