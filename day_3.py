file_path = "data/day_3_input.txt"

with open(file_path, "r") as file:
    data = file.read().splitlines()

def has_non_digit_or_period(string):
    for char in string:
        if not char.isdigit() and char != ".":
            return True
    return False

def has_number(string):
    number = []
    for char in string:
        if char.isdigit():
            number.append(char)
    return number

def check_row(row_number, left_col_number, right_col_number, data):
    row = data[row_number]
    if left_col_number == 0:
        row_string = row[left_col_number:right_col_number+1]
    elif right_col_number == len(row) - 1:
        row_string = row[left_col_number-1:right_col_number+1]
    else:
        row_string = row[left_col_number-1:right_col_number+1]
    if has_non_digit_or_period(row_string):
        return True
    
def check_row_numbers(row_number, left_col_number, right_col_number, data):
    row = data[row_number]
    if left_col_number == 0:
        row_string = row[left_col_number:right_col_number+1]
    elif right_col_number == len(row) - 1:
        row_string = row[left_col_number-1:right_col_number+1]
    else:
        row_string = row[left_col_number-1:right_col_number+1]
    if has_non_digit_or_period(row_string):
        return True

def check_adjacent(row_number, left_col_number, right_col_number, data):
    if row_number == 0:
        below = row_number + 1
        if check_row(row_number, left_col_number, right_col_number, data):
            return True
        elif check_row(below, left_col_number, right_col_number, data):
            return True
    elif row_number == len(data) - 1:
        above = row_number - 1
        if check_row(row_number, left_col_number, right_col_number, data):
            return True
        elif check_row(above, left_col_number, right_col_number, data):
            return True
    else:
        above = row_number - 1
        below = row_number + 1
        if check_row(above, left_col_number, right_col_number, data):
            return True
        elif check_row(row_number, left_col_number, right_col_number, data):
            return True
        elif check_row(below, left_col_number, right_col_number, data):
            return True
        

part_numbers = 0

for i, row in enumerate(data):
    print(f"row {i}")
    left = 0
    right = 0
    at_digit = False
    for j, char in enumerate(row):
        if char.isdigit():
            if j == len(row) - 1:
                if at_digit == True:
                    if check_adjacent(i, left, right, data):
                        part_numbers += int(row[left:right+1])
                else:
                    left = j
                    right = j+1
                    if check_adjacent(i, left, right, data):
                        part_numbers += int(row[left:right])
            if at_digit == True:
                right += 1
            else:
                left = j
                right = j+1
            at_digit = True
        else:
            if at_digit == True:
                if check_adjacent(i, left, right, data):
                    part_numbers += int(row[left:right])
                at_digit = False
            else:
                at_digit = False
    
print(part_numbers)



# loop over each row of the data
# check if the character is a *
# if it is, check the adjacent characters for a set of digits
# if two disctinct sets of digits are found, add the product of the two sets to the total

for i, row in enumerate(data):
    for i in range(row):
        if row[i] == "*":
            left = i - 1
            right = i + 1
            if check_adjacent(i, left, right, data):
                # part_numbers += int(row[left:right])
                pass



