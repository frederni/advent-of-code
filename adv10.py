import sys
from itertools import chain
import logging

# Setup
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
sys.setrecursionlimit(10000)


def load_input(filename: str = "input10.txt") -> list[list[str]]:
    """Parse input file, returns 2D list of one-character strings"""
    with open(filename, "r") as f:
        data = f.read().split("\n")
    splitted_data = [list(line.strip()) for line in data]
    return splitted_data


connectable: dict[str, tuple[str, ...]] = {
    "|": ("north", "south"),
    "-": ("east", "west"),
    "L": ("north", "east"),
    "J": ("north", "west"),
    "7": ("south", "west"),
    "F": ("south", "east"),
    ".": (),
}


def is_connected(current: str, neighbour: str, how: str) -> bool:
    opposites = {"north": "south", "south": "north", "west": "east", "east": "west"}
    return how in connectable[current] and opposites[how] in connectable[neighbour]


def get_connected_pipes_new(data: list[list[str]], distances: list[list[int]], indices_to_check: list[tuple[int, int]]):
    """Recursively propagate across the loop from start point and increment distance for connected nodes"""
    new_neighbour_indices: list[tuple[int, int]] = []
    for curr_row, curr_col in indices_to_check:
        for next_row, next_col, direction in [
            (curr_row - 1, curr_col, "north"),
            (curr_row, curr_col + 1, "east"),
            (curr_row + 1, curr_col, "south"),
            (curr_row, curr_col - 1, "west"),
        ]:
            try:
                neighbour_value = data[next_row][next_col]
            except IndexError:
                logger.debug("IndexError at %s,%s", next_row, next_col)
                continue
            if is_connected(data[curr_row][curr_col], neighbour_value, direction):
                current_distance = distances[curr_row][curr_col] or 0
                if distances[next_row][next_col] == -1:
                    distances[next_row][next_col] = distances[curr_row][curr_col] + 1
                    new_neighbour_indices.append((next_row, next_col))
                else:
                    logger.debug(
                        "Neighbor node already visisted and has value %s. This iteration would have set it to %s",
                        distances[next_row][next_col],
                        current_distance + 1,
                    )
    if new_neighbour_indices:
        get_connected_pipes_new(data, distances, new_neighbour_indices)


def find_index_of_start(data: list[list[str]]) -> tuple[int, int]:
    for row_index, row in enumerate(data):
        if "S" in row:
            return row_index, row.index("S")
    logger.debug("Could not find 'S' in data")
    return -1, -1


if __name__ == "__main__":
    data: list[list[str]] = load_input()
    distances: list[list[int]] = [[-1] * len(r) for r in data]
    # Find row and col index of "S"
    row_s, col_s = find_index_of_start(data)

    # Manually adjust 'actual' pipe type of S (must be manually set based on input!)
    data[row_s][col_s] = "J"
    distances[row_s][col_s] = 0 
    get_connected_pipes_new(data, distances, [(row_s, col_s)])
    print("Part 1", max(list(chain.from_iterable(distances))))
