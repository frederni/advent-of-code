from copy import deepcopy
class LoopError(Exception):
    pass

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
        # Check loop
        elif (*next_coordinate, pos_idx) in visited_coordinates:
            raise LoopError
        else:
            visited_coordinates.add((next_coordinate[0], next_coordinate[1], pos_idx))
            i = next_coordinate[0]
            j = next_coordinate[1]
    coordinates = set((idx[0], idx[1]) for idx in visited_coordinates)
    return coordinates if return_set else len(coordinates)

def part_2(guardmap: list[str]):
    """Find initial path without new obstacles"""
    initial_path = part_1(guardmap, return_set=True)
    initial_map = [list(line) for line in guardmap]
    placements_with_loop = 0
    assert isinstance(initial_path, set)
    for i, j in initial_path:
        if guardmap[i][j] == "^":
            continue
        new_map = deepcopy(initial_map)
        new_map[i][j] = "#"
        try:
            part_1(["".join(line) for line in new_map], return_set=True)
        except LoopError:
            placements_with_loop += 1
    return placements_with_loop

if __name__ == "__main__":
    with open("inputs/6.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
        print("Part 1", part_1(data))
        print("Part 2", part_2(data))
