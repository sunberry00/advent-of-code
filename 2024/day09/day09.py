def parse_input(puzzle):
    id_number = 0
    disc = []
    for index, sector in enumerate(puzzle):
        sector_int = int(sector)
        if index % 2 == 0:
            for i in range(sector_int):
                disc.append(id_number)
            id_number += 1
        else:
            for i in range(sector_int):
                disc.append(".")

    return disc

def find_last_symbol(disc):
    for index, symbol in enumerate(disc[::-1]):
        if symbol != '.':
            return len(disc) - index - 1
    return -1

def calc_checksum(disc):
    result = 0
    for i, symbol in enumerate(disc):
        if symbol == '.':
            continue

        result += int(symbol) * i
    return result

def solve_part1(puzzle):
    disc = parse_input(puzzle)
    for index, symbol in enumerate(disc):
        if symbol == '.':
            index_to_replace = find_last_symbol(disc)
            if index_to_replace < index:
                break
            disc[index], disc[index_to_replace] = disc[index_to_replace], disc[index]

    checksum = calc_checksum(disc)
    print(checksum)


def find_contiguous_space(disc, start_index, size_needed):
    if start_index <= 0:
        return -1

    for i in range(start_index - size_needed + 1):
        # Check if we have enough contiguous space starting at position i
        is_valid = True
        for j in range(size_needed):
            if i + j >= len(disc) or disc[i + j] != '.':
                is_valid = False
                break
        if is_valid:
            return i
    return -1


def get_file_size(disc, file_id):
    return sum(1 for block in disc if block == file_id)


def get_file_start(disc, file_id):
    for i, block in enumerate(disc):
        if block == file_id:
            return i
    return -1


def move_file(disc, file_id, new_start):
    size = get_file_size(disc, file_id)
    old_positions = [i for i, block in enumerate(disc) if block == file_id]

    for i in range(size):
        disc[new_start + i] = file_id

    for pos in old_positions:
        disc[pos] = '.'

    return disc


def solve_part2(puzzle):
    disc = parse_input(puzzle)

    file_ids = sorted(set(x for x in disc if x != '.'), reverse=True)

    for file_id in file_ids:
        file_size = get_file_size(disc, file_id)
        file_start = get_file_start(disc, file_id)

        new_position = find_contiguous_space(disc, file_start, file_size)

        # If we found a valid position, move the file
        if new_position >= 0:
            disc = move_file(disc, file_id, new_position)

    checksum = calc_checksum(disc)
    print(checksum)
    return checksum


def main():
    with open("input.txt") as f:
        puzzle = f.read()

    # solve_part1(puzzle)
    solve_part2(puzzle)



if __name__ == "__main__":
    main()