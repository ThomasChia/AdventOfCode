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

scratchcards = len(data)
scratchcard_counts = {i: 1 for i in range(scratchcards)}

for i, event in enumerate(data):
    for j in range(scratchcard_counts[i]):
        winning, own = split_numbers(event)
        winning = string_numbers_to_list(winning)
        own = string_numbers_to_list(own)
        winning_numbers = common_elements(winning, own)
        for k in range(len(winning_numbers)):
            scratchcard_counts[i+k+1] += 1


print(scratchcard_counts)
print(sum(scratchcard_counts.values()))