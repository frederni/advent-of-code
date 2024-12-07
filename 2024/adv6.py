def part_1(guardmap: list[str], return_set: bool = False):
    positions = ["up", "right", "down", "left"]
    visited_coordinates: set[tuple[int, int, int]] = set()
    # Find start positon
    for i, line in enumerate(guardmap):
        if "^" in line:
            j = line.find("^")
            break
    pos_idx = 0  # Starts upwards
    initial_coords = (i, j, pos_idx)
    visited_coordinates.add(initial_coords)
    out_of_bounds = False
    while not out_of_bounds:
        match positions[pos_idx]:
            case "up":
                next_coordinate = (i - 1, j)
            case "down":
                next_coordinate = (i + 1, j)
            case "left":
                next_coordinate = (i, j - 1)
            case "right":
                next_coordinate = (i, j + 1)
        # Check out of bounds
        if (
            out_of_bounds := next_coordinate[0] < 0
            or next_coordinate[0] >= len(guardmap)
            or next_coordinate[1] < 0
            or next_coordinate[1] >= len(guardmap[0])
        ):
            break
        # Check obstacle
        if guardmap[next_coordinate[0]][next_coordinate[1]] == "#":
            pos_idx = (pos_idx + 1) % 4
        else:
            visited_coordinates.add((next_coordinate[0], next_coordinate[1], pos_idx))
            i = next_coordinate[0]
            j = next_coordinate[1]
    coordinates = set((idx[0], idx[1]) for idx in visited_coordinates)
    print()
    return coordinates if return_set else len(coordinates)

if __name__ == "__main__":
    with open("inputs/6.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
        print("Part 1", part_1(data))