import itertools


def parse_input(puzzle):
    antenna_coords = dict()
    for i, row in enumerate(puzzle):
        for j, symbol in enumerate(row):
            if puzzle[i][j] != '.':
                if symbol not in antenna_coords.keys():
                    antenna_coords[symbol] = set()
                antenna_coords[symbol].add((i, j))
    return antenna_coords

def create_antinodes(first, second, rows, cols):
    vector = first[0] - second[0], first[1] - second[1]
    point_1 = first[0] - vector[0], first[1] - vector[1]
    point_2 = first[0] + vector[0], first[1] + vector[1]
    point_3 = second[0] - vector[0], second[1] - vector[1]
    point_4 = second[0] + vector[0], second[1] + vector[1]
    potental_antinodes = {point_1, point_2, point_3, point_4}
    antenne = {first, second}

    antinodes = set()
    for left, right in potental_antinodes:
        if 0 <= left < rows and 0 <= right < cols:
            antinodes.add((left, right))

    return antinodes.difference(antenne)

def create_antinodes_2(first, second, rows, cols):
    vector = first[0] - second[0], first[1] - second[1]
    potential_antinodes = set()
    for i in range(100):
        point_1 = first[0] - i * vector[0], first[1] - i * vector[1]
        point_2 = first[0] + i * vector[0], first[1] + i * vector[1]
        point_3 = second[0] - i * vector[0], second[1] - i * vector[1]
        point_4 = second[0] + i * vector[0], second[1] + i * vector[1]
        potential_antinodes.update({point_1, point_2, point_3, point_4})

    antenne = {first, second}

    antinodes = set()
    for left, right in potential_antinodes:
        if 0 <= left < rows and 0 <= right < cols:
            antinodes.add((left, right))

    return antinodes

def solve_part1(puzzle):
    rows = len(puzzle)
    cols = len(puzzle[0])
    antenna_coords = parse_input(puzzle)

    all_antinodes = set()
    for antenna, coordinates in antenna_coords.items():
        pairs = list(itertools.combinations(coordinates, 2))
        antenna_antinodes = set()
        for first, second in pairs:
            antinodes = create_antinodes(first, second, rows, cols)
            antenna_antinodes.update(antinodes)
        all_antinodes.update(antenna_antinodes)

    print(len(all_antinodes))

def solve_part2(puzzle):
    rows = len(puzzle)
    cols = len(puzzle[0])
    antenna_coords = parse_input(puzzle)
    all_antinodes = set()
    for antenna, coordinates in antenna_coords.items():
        pairs = list(itertools.combinations(coordinates, 2))
        antenna_antinodes = set()
        for first, second in pairs:
            antinodes = create_antinodes_2(first, second, rows, cols)
            antenna_antinodes.update(antinodes)
        all_antinodes.update(antenna_antinodes)

    print(len(all_antinodes))





def main():
    with open("input.txt", 'r') as file:
        puzzle = file.readlines()

    puzzle = [line.strip() for line in puzzle]
    solve_part1(puzzle)
    solve_part2(puzzle)

if __name__ == "__main__":
    main()