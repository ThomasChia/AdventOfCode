from typing import List

file_path = "data/day_3_input.txt"

with open(file_path, "r") as file:
    data = file.read().splitlines()

# def has_non_digit_or_period(string):
#     for char in string:
#         if not char.isdigit() and char != ".":
#             return True
#     return False

# def has_number(string):
#     number = []
#     for char in string:
#         if char.isdigit():
#             number.append(char)
#     return number

# def check_row(row_number, left_col_number, right_col_number, data):
#     row = data[row_number]
#     if left_col_number == 0:
#         row_string = row[left_col_number:right_col_number+1]
#     elif right_col_number == len(row) - 1:
#         row_string = row[left_col_number-1:right_col_number+1]
#     else:
#         row_string = row[left_col_number-1:right_col_number+1]
#     if has_non_digit_or_period(row_string):
#         return True
    
# def check_row_numbers(row_number, left_col_number, right_col_number, data):
#     row = data[row_number]
#     if left_col_number == 0:
#         row_string = row[left_col_number:right_col_number+1]
#     elif right_col_number == len(row) - 1:
#         row_string = row[left_col_number-1:right_col_number+1]
#     else:
#         row_string = row[left_col_number-1:right_col_number+1]
#     if has_non_digit_or_period(row_string):
#         return True

# def check_adjacent(row_number, left_col_number, right_col_number, data):
#     """
#     Checks the row above, the current row, and the row below for adjacent symbols
#     returns True if there are adjacent symbols, False otherwise
#     """
#     if row_number == 0:
#         below = row_number + 1
#         if check_row(row_number, left_col_number, right_col_number, data):
#             return True
#         elif check_row(below, left_col_number, right_col_number, data):
#             return True
#     elif row_number == len(data) - 1:
#         above = row_number - 1
#         if check_row(row_number, left_col_number, right_col_number, data):
#             return True
#         elif check_row(above, left_col_number, right_col_number, data):
#             return True
#     else:
#         above = row_number - 1
#         below = row_number + 1
#         if check_row(above, left_col_number, right_col_number, data):
#             return True
#         elif check_row(row_number, left_col_number, right_col_number, data):
#             return True
#         elif check_row(below, left_col_number, right_col_number, data):
#             return True
        

# part_numbers = 0

# for i, row in enumerate(data):
#     print(f"row {i}")
#     left = 0
#     right = 0
#     at_digit = False
#     for j, char in enumerate(row):
#         if char.isdigit():
#             if j == len(row) - 1:
#                 if at_digit == True:
#                     if check_adjacent(i, left, right, data):
#                         part_numbers += int(row[left:right+1])
#                 else:
#                     left = j
#                     right = j+1
#                     if check_adjacent(i, left, right, data):
#                         part_numbers += int(row[left:right])
#             if at_digit == True:
#                 right += 1
#             else:
#                 left = j
#                 right = j+1
#             at_digit = True
#         else:
#             if at_digit == True:
#                 if check_adjacent(i, left, right, data):
#                     part_numbers += int(row[left:right])
#                 at_digit = False
#             else:
#                 at_digit = False
    
# print(part_numbers)



# loop over each row of the data
# check if the character is a *
# if it is, check the adjacent characters for a set of digits
# check the row above, is there a digit in the adjacent area?
# if there is, then find the number associated with that digit
# repeat for all adjacent digits, unconnected digits
# check the current row, is there a digit in the adjacent area?
# if there is, then find the number associated with that digit
# repeat for all adjacent digits, unconnected digits
# check the below row, is there a digit in the adjacent area?
# if there is, then find the number associated with that digit
# repeat for all adjacent digits, unconnected digits
# if two disctinct sets of digits are found, add the product of the two sets to the total

def find_number_from_digit(row, number_index):
    left = number_index
    right = number_index
    print(left)
    while row[left].isdigit():
        left -= 1
        if left == -1:
            break
    left += 1

    while row[right].isdigit():
        right += 1
        if right == len(row):
            break
    
    if row[left:right] == '':
        return None
    else:
        return int(row[left:right])

def remove_duplicate_numbers(left_number, star_number, right_number):
    if left_number == star_number:
        left_number = None
    if star_number == right_number:
        right_number = None
    numbers = [left_number, star_number, right_number]
    return [item for item in numbers if item is not None]

def check_row_for_numbers(row, star_index):
    left = star_index - 1
    right = star_index + 1
    if left == -1:
        left_number = None
        if row[star_index].isdigit():
            star_number = find_number_from_digit(row, star_index)
        else:
            star_number = None

        if row[right].isdigit():
            right_number = find_number_from_digit(row, right)
        else:
            right_number = None
    elif star_index == len(row) - 1:
        right_number = None
        if row[left].isdigit():
            left_number = find_number_from_digit(row, left)
        else:
            left_number = None

        if row[star_index].isdigit():
            star_number = find_number_from_digit(row, star_index)
        else:
            star_number = None
    else:
        if row[left].isdigit():
            left_number = find_number_from_digit(row, left)
        else:
            left_number = None

        if row[star_index].isdigit():
            star_number = find_number_from_digit(row, star_index)
        else:
            star_number = None

        if row[right].isdigit():
            right_number = find_number_from_digit(row, right)
        else:
            right_number = None

    numbers = remove_duplicate_numbers(left_number, star_number, right_number)

    return numbers

def find_adjacent_numbers(row_number, star_index, data) -> List[int]:
    if row_number == 0:
        below = row_number + 1
        row_numbers = check_row_for_numbers(data[row_number], star_index)
        below_numbers = check_row_for_numbers(data[below], star_index)
        return [row_numbers, below_numbers]
    
    elif row_number == len(data) - 1:
        above = row_number - 1
        above_numbers = check_row_for_numbers(data[above], star_index)
        row_numbers = check_row_for_numbers(data[row_number], star_index)
        return [above_numbers, row_numbers]
    
    else:
        above = row_number - 1
        below = row_number + 1
        above_numbers = check_row_for_numbers(data[above], star_index)
        row_numbers = check_row_for_numbers(data[row_number], star_index)
        below_numbers = check_row_for_numbers(data[below], star_index)
        return [above_numbers, row_numbers, below_numbers]

gear_ratio_sum = 0

for i, row in enumerate(data):
    # print(f"row: {row}")
    for j in range(len(row)):
        if row[j] == "*":
            adjacent_numbers = find_adjacent_numbers(i, j, data)
            adjacent_numbers = [lst for lst in adjacent_numbers if lst]
            print(adjacent_numbers)
            if len(adjacent_numbers) == 2:
                product = adjacent_numbers[0][0] * adjacent_numbers[1][0]
                gear_ratio_sum += product
            elif len(adjacent_numbers[0]) == 2:
                product = adjacent_numbers[0][0] * adjacent_numbers[0][1]
                gear_ratio_sum += product

print(gear_ratio_sum)



