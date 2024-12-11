from re import match


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
    for _ in range(25):
        stones = blink(stones)

    return len(stones)

def solve_part2(puzzle):
    stones = puzzle
    cache = dict()
    for _ in range(75):
        sum = 0
        for stone in stones:
            sum += expand(stone, 75, cache)
    return sum

def expand(stone, num_iterations, cache_dict):
    if num_iterations == 0:
        return 1

    cache = cache_dict.get((stone, num_iterations), 0)
    if cache != 0:
        return cache

    result = 0
    if stone == 0:
        result = expand(1, num_iterations - 1, cache_dict)
    elif (stone_len := len(str(stone))) % 2 == 0:
        str_stone = str(stone)
        half_index = stone_len // 2
        left = int(str_stone[:half_index])
        right = int(str_stone[half_index:])
        result = expand(left, num_iterations - 1, cache_dict) + expand(right, num_iterations - 1, cache_dict)
    else:
        result = expand(stone * 2024, num_iterations - 1, cache_dict)
    cache_dict[(stone, num_iterations)] = result
    return result


def main():
    # Use context manager with explicit encoding
    with open("input.txt", "r", encoding='utf-8') as f:
        # Read and process in one go
        puzzle = [int(x) for x in f.read().split()]

    result = solve_part1(puzzle)
    result_2 = solve_part2(puzzle)
    print(result_2)


if __name__ == "__main__":
    main()