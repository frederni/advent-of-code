import numpy as np
import itertools

def draw_grid(grid, unique_antinodes):
    data_list = [list(line) for line in grid]
    for x, y in unique_antinodes:
        data_list[x][y] = "#"
    for line in data_list:
        print("".join(line))

def part_1():
    with open("inputs/8.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    frequencies = set(char for line in data for char in line) - set(".")
    antinodes_all = dict()
    for frequency in frequencies:
        indices = [ # Indices with current frequency
            (i, j)
            for i, line in enumerate(data)
            for j, char in enumerate(line)
            if char == frequency
        ]
        for freq1, freq2 in itertools.combinations(indices, 2):
            # Get the distance between the two frequencies
            delta_X, delta_Y = (freq2[0] - freq1[0]), (freq2[1] - freq1[1])
            antinodes = [
                (x, y)
                for x, y in [
                    (freq2[0] + delta_X, freq2[1] + delta_Y),
                    (freq1[0] - delta_X, freq1[1] - delta_Y),
                ]
                if 0 <= x < len(data) and 0 <= y < len(data[0])
            ]
            antinodes_all.setdefault(frequency, []).extend(antinodes)
    unique_an = set()
    for an in antinodes_all.values():
        unique_an.update(an)
    print(len(unique_an))


if __name__ == "__main__":
    part_1()
