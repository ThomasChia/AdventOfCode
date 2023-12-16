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

def get_seeds(seeds_string):
    seeds = seeds_string.split(': ')[1].strip()
    seeds = seeds.strip().split(' ')
    return seeds

def get_seeds_part_two(seeds_string):
    seeds = []
    seeds_ranges = seeds_string.split(': ')[1].strip().strip().split(' ')
    seeds_ranges = [int(i) for i in seeds_ranges]
    seeds = [(seeds_ranges[i], seeds_ranges[i] + seeds_ranges[i+1]) for i in range(0, len(seeds_ranges), 2)]
    return seeds

def contains(seed, seeds):
    return any(start <= seed < end for start, end in seeds)

def reverse_mapping(maps):
    reversed_maps = []
    for map in maps:
        reversed_map = []
        for destination_start_range, source_start_range, range_length in map:
            reversed_map = [[source_start_range, destination_start_range, range_length]] + reversed_map

        reversed_maps = [reversed_map] + reversed_maps
    return reversed_maps

def location_to_seed(location, maps):
    for map in maps:
        for destination_start_range, source_start_range, range_length in map:
            if int(location) >= source_start_range and int(location) < source_start_range + range_length:
                location = destination_start_range + (int(location) - source_start_range)
                break
    return location

def find_location(seed, maps):
    location = seed
    location = location_to_seed(location, maps)

    return location

def seed_in_original(seed, seeds):
    return any(start <= seed < end for start, end in seeds)

for i, mapping_string in enumerate(data):
    if i == 0:
        # seeds = get_seeds(data[i])
        seeds = get_seeds_part_two(data[i])
    else:
        data[i] = mapping_string.split('\n')
        map = create_generic_mapping(data[i])
        maps.append(map)

maps = reverse_mapping(maps)

location = 0
while True:
    seed = location_to_seed(location, maps)
    if seed_in_original(seed, seeds):
        print(f"r: {location}")
        break

    if location % 1000000 == 0:
        print(location)

    location += 1
