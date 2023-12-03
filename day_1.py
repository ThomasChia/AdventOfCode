import typing

codes = open("data/calibration_doc.txt", "r").read().split("\n")

def get_calibration_codes(codes_main: typing.List[str]) -> int:
    codes = []
    for code in codes_main:
        first_int = 0
        second_int = 0
        for char in code:
            if char.isdigit():
                first_int = char
                break
        for char in code[::-1]:
            if char.isdigit():
                second_int = char
                break

        codes.append(int(first_int + second_int))

    return sum(codes)

def get_calibration_codes_part_2(codes_main: typing.List[str]) -> int:
    codes = []
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]
    numbers_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five":"5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0"
    }
    for code in codes_main:
        print(code)
        first_int = 0
        second_int = 0
        left = 0
        right = 0
        while True:
            test_str = code[left:right]
            if test_str in numbers:
                if test_str in numbers_dict:
                    first_int = str(numbers_dict[test_str])
                else:
                    first_int = test_str
                break
            elif right > len(code):
                left += 1
                right = left
            else:
                right += 1
                if right - left > 6:
                    left += 1
                    right = left

        left = len(code)
        right = len(code)
        while True:
            test_str = code[left:right]
            if test_str in numbers:
                if test_str in numbers_dict:
                    second_int = str(numbers_dict[test_str])
                else:
                    second_int = test_str
                break
            elif left < 0:
                right -= 1
                left = right
            else:
                left -= 1
                if right - left > 6:
                    right -= 1
                    left = right

        print(first_int, second_int)
        codes.append(int(first_int + second_int))

    return sum(codes)

# print(get_calibration_codes(codes))
print(get_calibration_codes_part_2(codes))
print("hello")