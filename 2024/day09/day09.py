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
            return result

        result += int(symbol) * i

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

def main():
    with open("input.txt") as f:
        puzzle = f.read()

    solve_part1(puzzle)



if __name__ == "__main__":
    main()