def possible_moves(puzzle, x, y, current_height):
    result = set()
    if x != 0:
        next_height = puzzle[x - 1][y]
        if next_height == current_height + 1:
            result.add('up')
    elif x != len(puzzle) - 1:
        next_height = puzzle[x + 1][y]
        if next_height == current_height + 1:
            result.add('down')
    elif y != 0:
        next_height = puzzle[x][y - 1]
        if next_height == current_height + 1:
            result.add('left')
    elif y != len(puzzle[0]) - 1:
        next_height = puzzle[x][y + 1]
        if next_height == current_height + 1:
            result.add('right')
    return result

def backtrack(puzzle, x, y, current_height, end_trails):
    if current_height == 9:
        end_trails.add((x, y))
        return

    if x != 0:
        if puzzle[x - 1][y] == current_height + 1:
            backtrack(puzzle, x - 1, y, current_height + 1, end_trails)

    if x != len(puzzle) - 1:
        if puzzle[x + 1][y] == current_height + 1:
            backtrack(puzzle, x + 1, y, current_height + 1, end_trails)

    if y != 0:
        if puzzle[x][y - 1] == current_height + 1:
            backtrack(puzzle, x, y - 1, current_height + 1, end_trails)

    if y != len(puzzle[0]) - 1:
        if puzzle[x][y + 1] == current_height + 1:
            backtrack(puzzle, x, y + 1, current_height + 1, end_trails)

    return




def solve_part1(puzzle):
    trailheads = find_trailheads(puzzle)
    result = dict()
    for start_x, start_y in trailheads:
        end_trails = set()
        backtrack(puzzle, start_x, start_y, 0, end_trails)
        result[(start_x, start_y)] = end_trails

    return sum([len(value) for key, value in result.items()])


def find_trailheads(puzzle):
    trailheads = set()
    for i, row in enumerate(puzzle):
        for j, height in enumerate(row):
            if height == 0:
                trailheads.add((i, j))

    return trailheads

def main():
    with open("input.txt", "r") as f:
        puzzle = f.read()

    puzzle = [[int(num) for num in line] for line in puzzle.split('\n')]
    print(solve_part1(puzzle))

if __name__ == "__main__":
    main()