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

        print(first_int, second_int)
        codes.append(int(first_int + second_int))

    return sum(codes)


print(get_calibration_codes(codes))
print("hello")