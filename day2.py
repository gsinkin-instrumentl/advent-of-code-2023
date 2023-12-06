import argparse
import re

def run(filepath):
    f = open(filepath, "r")
    game_powers = []
    for line in f:
        game_id = int(re.findall("Game (\d+):", line)[0])
        max_blues = max([int(color) for color in re.findall("(\d+) blue", line)])
        max_reds = max([int(color) for color in re.findall("(\d+) red", line)])
        max_greens = max([int(color) for color in re.findall("(\d+) green", line)])
        game_powers.append(max_blues * max_reds * max_greens)

    print(sum(game_powers))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath')
    args = parser.parse_args()
    run(args.filepath)
        
