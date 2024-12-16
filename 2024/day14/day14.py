import re

class Robot:
    def __init__(self, px, py, vx, vy):
        self.__px = px
        self.__py = py
        self.__vx = vx
        self.__vy = vy

    def move(self, steps, grid_x=103, grid_y=101):
        for i in range(steps):
            self.__px = (self.__px + self.__vx) % grid_x
            self.__py = (self.__py + self.__vy) % grid_y

        return self

    def get_px(self):
        return self.__px

    def get_py(self):
        return self.__py

def parse_robot(robot_str):
    pattern = re.compile(r"^p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)$")
    match = pattern.search(robot_str)
    if not match:
        raise ValueError("Invalid robot string format")

    px, py, vx, vy = map(int, match.groups())
    return Robot(px, py, vx, vy)

def solve_part1(puzzle):
    robots = puzzle.split('\n')

    robots = [parse_robot(robot) for robot in robots]

    for robot in robots:
        robot.move(100)

    quadrants = {key: 0 for key in range(1, 5)}
    for robot in robots:
        current_x, current_y = robot.get_px(), robot.get_py()
        if current_x < 51:
            if current_y < 50:
                quadrants[1] += 1
            elif current_y > 50:
                quadrants[2] += 1
        elif current_x > 51:
            if current_y < 50:
                quadrants[3] += 1
            elif current_y > 50:
                quadrants[4] += 1

    result = 1
    for key, value in quadrants.items():
        result *= value

    return result

def main():
    with open("input.txt", "r") as f:
        puzzle = f.read()

    result_part1 = solve_part1(puzzle)
    print(result_part1)

if __name__ == "__main__":
    main()