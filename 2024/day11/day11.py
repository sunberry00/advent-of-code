def blink(stone_arrangement):
    # Preallocate result list with estimated size to avoid repeated resizing
    result = []
    result_append = result.append  # Local reference for faster append operations

    # Process stones in bulk using list comprehension for better performance
    for stone in stone_arrangement:
        if stone == 0:
            result_append(1)
        elif (stone_len := len(str(stone))) % 2 == 0:
            # Use string slicing with cached length calculation
            str_stone = str(stone)
            half_index = stone_len // 2
            result_append(int(str_stone[:half_index]))
            result_append(int(str_stone[half_index:]))
        else:
            result_append(stone * 2024)

    return result


def solve_part1(puzzle):
    stones = puzzle
    # Use a generator expression to avoid creating intermediate lists
    for _ in range(75):
        stones = blink(stones)

    return len(stones)


def main():
    # Use context manager with explicit encoding
    with open("input.txt", "r", encoding='utf-8') as f:
        # Read and process in one go
        puzzle = [int(x) for x in f.read().split()]

    result = solve_part1(puzzle)
    print(result)


if __name__ == "__main__":
    main()