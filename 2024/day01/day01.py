def part01():
    with open("2024/day01/test.txt", "r") as f:
        input = f.read()

    numbers = input.split()
    left = [int(x) for x in numbers[::2]]
    right = [int(x) for x in numbers[1::2]]

    left = sorted(left)
    right = sorted(right)

    distances = []
    for i in range(len(left)):
        distances.append(abs(left[i] - right[i]))

    print(sum(distances))

def part02():
    with open("2024/day01/input.txt", "r") as f:
        input = f.read()

    numbers = input.split()
    left = [int(x) for x in numbers[::2]]
    right = [int(x) for x in numbers[1::2]]

    sim_score = 0
    for num in left:
        sim_score += num * right.count(num)

    print(sim_score)    


if __name__ == "__main__":
    part01()
    part02()


    