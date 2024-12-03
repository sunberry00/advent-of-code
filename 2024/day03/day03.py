import re

def part01():
    with open("2024/day03/input.txt", "r") as f:
        input = f.read()
    
    pattern = re.compile(r'mul\(\d+,\d+\)')

    allmatches = re.findall(pattern, input)

    pattern_mul = re.compile(r'\D+(\d+),(\d+)\)')

    grps = [re.search(pattern_mul, match).groups() for match in allmatches]
    print(grps)

    mults = [int(x) * int(y) for x, y in grps]
    print(sum(mults))


if __name__ == "__main__":
    part01()