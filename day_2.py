# read in the data as a dictionary of list of lists, where the key is the game number - done
# make dictionary of maximum cubes - done
# iterate through the dictionary, then iterate over the list of lists
# compare the number of cubes in each draw to the respective maximum cubes

file_path = "data/day_2_input.txt"
data = {}

with open(file_path, "r") as f:
    for line in f:
        key, value = line.strip().split(":")
        data[key] = value.strip().split(";")

max_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

failed_games = []

for key, value in data.items():
    for item in value:
        pairs = item.strip().split(", ")
        for pair in pairs:
            value, colour = pair.split(" ")
            if int(value) > max_cubes[colour]:
                game_number = key.split(" ")[1]
                failed_games.append(int(game_number))
                break


successful_games = [int(id.split(" ")[1]) for id in list(data.keys())]
failed_games = list(set(failed_games))
print(failed_games)
print(sum(successful_games) - sum(failed_games))