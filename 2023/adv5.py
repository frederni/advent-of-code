import numpy as np

def parse_input(filename="input5.txt", part: int = 1) -> tuple[map, dict]:
    with open(filename, "r") as f:
        input = f.read()
    seeds, *maps = input.split("\n\n")
    seeds = map(int, seeds.split(": ")[1].split())
    if part == 2:
        seeds_array = np.array(list(seeds)).reshape((-1, 2))
        seeds = []
        for row in seeds_array:
            seeds.extend([row[0], row[0]+row[1]])
        # seeds = np.concatenate([np.arange(r[0], r[0]+r[1]) for r in seeds])
    data = dict()
    for map_full in maps:
        map_name, map_data = map_full.split(":")
        map_name = map_name.strip().split()[0]
        data[map_name] = dict(dst_start=[], src_start=[], range_length=[])
        for row in map_data.strip().split("\n"):
            dst_start, src_start, range_length = map(int, row.split())
            data[map_name]["dst_start"].append(dst_start)
            data[map_name]["src_start"].append(src_start)
            data[map_name]["range_length"].append(range_length)
    return seeds, data

def get_min_location(seeds, data):
    min_location = float('inf')
    for seed in seeds:
        src_value = seed
        for map_name in data.keys():
            for i in range(len(data[map_name]["dst_start"])):
                if src_value >= data[map_name]["src_start"][i] and \
                src_value <= data[map_name]["src_start"][i] + data[map_name]["range_length"][i]:
                    offset = abs(data[map_name]["src_start"][i] - src_value)
                    # Update src_value as this map's dst_value
                    src_value = data[map_name]["dst_start"][i] + offset
                    break # Go to next map
        
        # Last src_value will then be our location
        seed_location = src_value
        min_location = min(min_location, seed_location)
    return min_location

if __name__ == '__main__':
    for part in [1,2]:
        print(f"Part {part}")
        if part == 1:
            print(get_min_location(*parse_input(part=part)))
        elif part == 2:
            print(get_min_location(*parse_input(part=part)))
        else:
            raise ValueError("Unexpected part number. Must be integer and either 1 or 2")


""" psudeocode
min_location is inf
for each seed_min, seed_max:
    for row in map:
        if seed_max > src_start
# 68589803
"""
