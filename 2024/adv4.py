from utils import parse_raw
import numpy as np
import re


def part_1():
    data = np.array([[c for c in row] for row in parse_raw("inputs/4.txt").split("\n")])
    number_xmas = sum(  # Horizontal matches
        [len(re.findall(r"(?=XMAS|SAMX)", "".join(r))) for r in data]
    )
    print([(re.findall(r"(?=XMAS|SAMX)", "".join(r))) for r in data])
    print("After horizontal", number_xmas)
    number_xmas += sum( # Vertical matches
        [len(re.findall(r"(?=XMAS|SAMX)", "".join(c))) for c in data.T]
    )
    print("After vertical", number_xmas)
    for diagonal in [np.diag(data, k=-(data.shape[0]-i)) for i in range(1, 2*data.shape[0])]:
        number_xmas += sum(
            [len(re.findall(r"(?=XMAS|SAMX)", "".join(diagonal)))]
        )
    data_flip = np.fliplr(data)
    for anti_diagonal in [np.diag(data_flip, k=-(data_flip.shape[0]-i)) for i in range(1, 2*data_flip.shape[0])]:
        number_xmas += sum(
            [len(re.findall(r"(?=XMAS|SAMX)", "".join(anti_diagonal)))]
        )
        
        
    return number_xmas
    # allowed_neighbors = {"X": ["M"], "M": ["X", "A"], "A": ["M", "S"], "S": ["A"]}
    """Psudeocode
    - Iterate over each character
    - Skip if not at start or end (X/S)
    - If current char is X:
        - Ad (i,j) to possible_xmas
        - For each neighbor
            - If neighbor is 'M'
    """


if __name__ == "__main__":
    print(part_1())
