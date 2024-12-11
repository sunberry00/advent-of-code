def blink(stone_arrangement):
    blink = []
    for stone in stone_arrangement:
        if stone == 0:
            blink.append(1)
        elif len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            half_index = len(str_stone) // 2
            first_stone, second_stone = str_stone[:half_index], str_stone[half_index:]
            first_stone, second_stone = int(first_stone), int(second_stone)
            blink.append(first_stone)
            blink.append(second_stone)
        else:
            blink.append(stone * 2024)

    return blink
def solve_part1(puzzle):
    stones = puzzle
    for i in range(25):
        stones = blink(stones)

    print(len(stones))

def main():
    with open("input.txt", "r") as f:
        puzzle = f.read()

    puzzle = [int(x) for x in puzzle.split(" ")]

    solve_part1(puzzle)

if __name__ == "__main__":
    main()