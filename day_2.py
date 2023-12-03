# read in the data as a dictionary of list of lists, where the key is the game number - done
# make dictionary of maximum cubes - done
# iterate through the dictionary, then iterate over the list of lists
# compare the number of cubes in each draw to the respective maximum cubes

from functools import reduce

file_path = "data/day_2_input.txt"
data = {}

with open(file_path, "r") as f:
    for line in f:
        key, value = line.strip().split(":")
        data[key] = value.strip().split(";")

# Part 1
# max_cubes = {
#     "red": 12,
#     "green": 13,
#     "blue": 14
# }

# failed_games = []

# for key, value in data.items():
#     for item in value:
#         pairs = item.strip().split(", ")
#         for pair in pairs:
#             value, colour = pair.split(" ")
#             if int(value) > max_cubes[colour]:
#                 game_number = key.split(" ")[1]
#                 failed_games.append(int(game_number))
#                 break


# successful_games = [int(id.split(" ")[1]) for id in list(data.keys())]
# failed_games = list(set(failed_games))
# print(failed_games)
# print(sum(successful_games) - sum(failed_games))

# Part 2
game_powers = 0
for key, value in data.items():
    min_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for item in value:
        pairs = item.strip().split(", ")
        for pair in pairs:
            value, colour = pair.split(" ")
            if int(value) > min_cubes[colour]:
                min_cubes[colour] = int(value)
        
    game_power = reduce(lambda x, y: x * y, min_cubes.values())
    game_powers += game_power


print(game_powers)