import argparse


def run(filepath):
    f = open(filepath, "r")
    calibration_numbers = []
    for line in f:
        current_digit = first_digit = None
        for char in line:
            if char.isdigit():
                current_digit = char
                if first_digit is None:
                    first_digit = current_digit
        calibration_numbers.append(int(first_digit + current_digit))
    print(sum(calibration_numbers))



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath')
    args = parser.parse_args()
    run(args.filepath)
