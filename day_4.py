file_path = "data/day_4_input.txt"

with open(file_path, "r") as file:
    data = file.read().splitlines()

# print(data)

def split_numbers(lottery_event):
    winning_and_own = lottery_event.split(": ")[1]
    winning = winning_and_own.split(" | ")[0].strip().replace("  ", " ")
    own = winning_and_own.split(" | ")[1].strip().replace("  ", " ")

    return winning, own

def common_elements(list1, list2):
    return list(set(list1) & set(list2))

def string_numbers_to_list(string):
    return [int(number) for number in string.split(" ")]

points = 0

for event in data:
    winning, own = split_numbers(event)
    winning = string_numbers_to_list(winning)
    own = string_numbers_to_list(own)
    winning_numbers = common_elements(winning, own)
    if len(winning_numbers) > 0:
        points += pow(2, len(winning_numbers)-1)


print(points)