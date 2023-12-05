import argparse

NUMBERS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

MIN_CHARS = 3
MAX_CHARS = 5


def get_digit(starting_pos, line):
    for slice_len in range(3, 6):
         word = line[starting_pos:starting_pos + slice_len]
         number = NUMBERS.get(word)
         if number is not None:
             return number
    return None


def run(filepath):
    f = open(filepath, "r")
    calibration_numbers = []
    for line in f:
        current_digit = first_digit = None
        for index, char in enumerate(line):
            if char.isdigit():
                current_digit = char
            else:
                maybe_digit = get_digit(index, line)
                if maybe_digit:
                    current_digit = maybe_digit
                
            if first_digit is None:
                first_digit = current_digit
        calibration_numbers.append(int(first_digit + current_digit))
    print(sum(calibration_numbers))



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath')
    args = parser.parse_args()
    run(args.filepath)
