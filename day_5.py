import re
from tqdm import tqdm

file_path = "data/day_5_input.txt"

with open(file_path, "r") as file:
    data = file.read().split('\n\n')

seeds = []
seed_location_mapping = {}
maps = []
locations = []

def create_generic_mapping(mapping_details):
    map = []
    for detail in mapping_details[1:]:
        details_split = detail.split(' ')
        destination_start_range = int(details_split[0])
        source_start_range = int(details_split[1])
        range_length = int(details_split[2])
        single_map = [destination_start_range, source_start_range, range_length]
        map.append(single_map)

    return map


def get_seeds(seeds):
    seeds = data[i].split(': ')[1].strip()
    return seeds

for i, mapping_string in enumerate(data):
    if i == 0:
        seeds = get_seeds(seeds)
        print(seeds)
    else:
        data[i] = mapping_string.split('\n')
        map = create_generic_mapping(data[i])
        maps.append(map)

seeds = seeds.strip().split(' ')

for seed in tqdm(seeds):
    for map in maps:
        for destination_start_range, source_start_range, range_length in map:
            if int(seed) >= source_start_range and int(seed) < source_start_range + range_length:
                seed = destination_start_range + (int(seed) - source_start_range)
                break

    locations.append(seed)

print(min(locations))

# for seed in seeds.strip().split(' '):
#     soil = seed_location_mapping[0][int(seed)]
#     fertiliser = seed_location_mapping[1][soil]
#     water = seed_location_mapping[2][fertiliser]
#     light = seed_location_mapping[3][water]
#     temp = seed_location_mapping[4][light] 
#     humidity = seed_location_mapping[5][temp]
#     location = seed_location_mapping[6][humidity]
#     locations.append(location)

# print(seed_location_mapping)
# print(soil, fertiliser, water, light, temp, humidity, location)
# print(locations)
# print(min(locations))
