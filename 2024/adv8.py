import itertools


def draw_grid(grid, unique_antinodes):
    data_list = [list(line) for line in grid]
    for x, y in unique_antinodes:
        data_list[x][y] = "#"
    for line in data_list:
        print("".join(line))

def get_antinodes(freq, delta_X, delta_Y, data, how="plus"):
    sign = 1 if how == "plus" else -1
    next_point = (freq[0] + sign * delta_X, freq[1] + sign * delta_Y)
    antinode_list = []
    within_grid = 0 <= next_point[0] < len(data) and 0 <= next_point[1] < len(data[0])
    while within_grid:
        antinode_list.append(next_point)
        next_point = (
            next_point[0] + sign * delta_X,
            next_point[1] + sign * delta_Y,
        )
        within_grid = 0 <= next_point[0] < len(data) and 0 <= next_point[1] < len(
            data[0]
        )
    return antinode_list

def day_8(part_2=False):
    with open("inputs/8.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    frequencies = set(char for line in data for char in line) - set(".")
    antinodes_all = dict()
    for frequency in frequencies:
        indices = [  # Indices with current frequency
            (i, j)
            for i, line in enumerate(data)
            for j, char in enumerate(line)
            if char == frequency
        ]
        if part_2:
            # Also include antennas as antinodes for part 2
            antinodes_all.setdefault(frequency, []).extend(indices)
        for freq1, freq2 in itertools.combinations(indices, 2):
            # Get the distance between the two frequencies
            delta_X, delta_Y = (freq2[0] - freq1[0]), (freq2[1] - freq1[1])
            if not part_2:
                antinodes = [
                    (x, y)
                    for x, y in [
                        (freq2[0] + delta_X, freq2[1] + delta_Y),
                        (freq1[0] - delta_X, freq1[1] - delta_Y),
                    ]
                    if 0 <= x < len(data) and 0 <= y < len(data[0])
                ]
                antinodes_all.setdefault(frequency, []).extend(antinodes)
            else:
                antinodes_all.setdefault(frequency, []).extend(
                    get_antinodes(freq2, delta_X, delta_Y, data, how="plus"))
                antinodes_all.setdefault(frequency, []).extend(
                    get_antinodes(freq1, delta_X, delta_Y, data, how="minus")
                )
    unique_an = set()
    for an in antinodes_all.values():
        unique_an.update(an)
    return len(unique_an)


if __name__ == "__main__":
    """Explanation:
    Part 1:
    First get any non-period character to define as set of frequencies.
    Iterating over these, we find the indices of each occurrence of the frequency.
    For each combination of two frequencies (`itertools.combinations`), we
    compute delta Y and delta X. Then, there is a antinode at (x2+delta_x, y2+delta_y)
    and (x1-delta_x, y1-delta_y). We then check if these are within the grid.
    Finally, we get the unique set of antinodes across all frequencies.

    Part 2:
    Same as above, but we also include the antennas as antinodes. Instead of
    adding two antinodes for each combination of two frequencies, we loop over
    the line spanned out until we're out of bounds.
    """
    print("Part 1:", day_8())
    print("Part 2:", day_8(part_2=True))
