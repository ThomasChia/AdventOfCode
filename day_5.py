import re

file_path = "data/day_5_input.txt"

with open(file_path, "r") as file:
    data = file.read().split('\n\n')

# print(data)

seeds = []
seed_location_mapping = {}

def create_generic_mapping(mapping_details):
    mapping = {}
    for detail in mapping_details[1:]:
        destination_start_range = int(detail.split(' ')[0])
        source_start_range = int(detail.split(' ')[1])
        range_length = int(detail.split(' ')[2])
        for i in range(range_length):
            mapping[destination_start_range+i] = source_start_range+i

    return mapping


def get_seeds(seeds):
    seeds = data[i].split(': ')[1]
    return seeds

for i, mapping_string in enumerate(data[:3]):
    if i == 0:
        seeds = get_seeds(seeds)
        print(seeds)
    else:
        data[i] = mapping_string.split('\n')
        mapping = create_generic_mapping(data[i])

        seed_location_mapping[i-1] = mapping

print(seed_location_mapping)


# print(data)