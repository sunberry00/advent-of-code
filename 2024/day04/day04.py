def check_N(x, y, puzzle):
    if x < 3:
        return False

    north_slice = ''.join(puzzle[x - i][y] for i in range(4))
    return north_slice == "XMAS"


def check_NE(x, y, puzzle):
    if x < 3 or y > len(puzzle[0]) - 4:
        return False
    northeast_slice = ''.join(puzzle[x - i][y + i] for i in range(4))
    return northeast_slice == "XMAS"


def check_E(x, y, puzzle):
    if y > len(puzzle[0]) - 4:
        return False

    east_slice = ''.join(puzzle[x][y + i] for i in range(4))
    return east_slice == "XMAS"


def check_SE(x, y, puzzle):
    if x > len(puzzle) - 4 or y > len(puzzle[0]) - 4:
        return False

    southeast_slice = ''.join(puzzle[x + i][y + i] for i in range(4))
    return southeast_slice == "XMAS"


def check_S(x, y, puzzle):
    if x > len(puzzle) - 4:
        return False

    south_slice = ''.join(puzzle[x + i][y] for i in range(4))
    return south_slice == "XMAS"


def check_SW(x, y, puzzle):
    if x > len(puzzle) - 4 or y < 3:
        return False

    southwest_slice = ''.join(puzzle[x + i][y - i] for i in range(4))
    return southwest_slice == "XMAS"


def check_W(x, y, puzzle):
    if y < 3:
        return False

    west_slice = ''.join(puzzle[x][y - i] for i in range(4))
    return west_slice == "XMAS"


def check_NW(x, y, puzzle):
    if x < 3 or y < 3:
        return False

    northwest_slice = ''.join(puzzle[x - i][y - i] for i in range(4))
    return northwest_slice == "XMAS"


def part01():
    with open("input.txt", "r") as file:
        puzzle = file.read().split("\n")

    count = 0
    for row, _ in enumerate(puzzle):
        for column, _ in enumerate(puzzle[row]):
            character = puzzle[row][column]
            if character == "X":
                count += check_N(row, column, puzzle)
                count += check_NE(row, column, puzzle)
                count += check_E(row, column, puzzle)
                count += check_SE(row, column, puzzle)
                count += check_S(row, column, puzzle)
                count += check_SW(row, column, puzzle)
                count += check_W(row, column, puzzle)
                count += check_NW(row, column, puzzle)

    print(count)


def check_a(x, y, puzzle):
    rows = len(puzzle)
    cols = len(puzzle[0])
    if x <= 0 or y <= 0 or x >= rows - 1 or y >= cols - 1:
        return 0

    first_diagonal = puzzle[x - 1][y - 1] + "A" + puzzle[x + 1][y + 1]
    second_diagonal = puzzle[x + 1][y - 1] + "A" + puzzle[x - 1][y + 1]

    valid_first = first_diagonal in ["MAS", "SAM"]
    valid_second = second_diagonal in ["MAS", "SAM"]

    return int(valid_first and valid_second)


def part02():
    with open("input.txt", "r") as file:
        puzzle = file.read().split("\n")

    count = 0
    for row, _ in enumerate(puzzle):
        for column, _ in enumerate(puzzle[row]):
            character = puzzle[row][column]
            if character == "A":
                count += check_a(row, column, puzzle)

    print(count)


if __name__ == "__main__":
    part01()
    part02()
