from copy import deepcopy
from enum import Enum
from typing import List

class Directions(Enum):
    UP = '^'
    RIGHT = '>'
    DOWN = 'v'
    LEFT = '<'

class Day06:
    def __init__(self, input_str):
        self.grid = [list(line) for line in input_str.strip().splitlines()]
        self.__find_start_coords()
        self.visited_positions = set()
        self.has_loop = False

    def __find_start_coords(self):
        symbols = ['^', '>', 'v', '<']
        for row_index, row in enumerate(self.grid):
            for col_index, col in enumerate(self.grid[row_index]):
                current_symbol = self.grid[row_index][col_index]
                if current_symbol in symbols:
                    self.current_X = row_index
                    self.current_Y = col_index
                    self.__set_direction(current_symbol)

    def __set_direction(self, symbol):
        match symbol:
            case '^':
                self.current_direction = Directions.UP
            case '>':
                self.current_direction = Directions.RIGHT
            case 'v':
                self.current_direction = Directions.DOWN
            case '<':
                self.current_direction = Directions.LEFT

    def is_move_possible(self):
        return self.current_direction == Directions.UP and self.current_X != 0 \
            or self.current_direction == Directions.RIGHT and self.current_Y != len(self.grid[0]) - 1 \
            or self.current_direction == Directions.DOWN and self.current_X != len(self.grid) - 1 \
            or self.current_direction == Directions.LEFT and self.current_Y != 0

    def step_forward(self):
        self.grid[self.current_X][self.current_Y] = 'X'

        if (self.current_X, self.current_Y, self.current_direction) in self.visited_positions:
            self.has_loop = True
            return False

        self.visited_positions.add((self.current_X, self.current_Y, self. current_direction))
        if self.is_move_possible():
            match self.current_direction.value:
                case '^':
                    self.current_X -= 1
                case '>':
                    self.current_Y += 1
                case 'v':
                    self.current_X += 1
                case '<':
                    self.current_Y -= 1
            return True
        else:
            return False


    def move_forward(self):
        current_symbol = self.current_direction.value
        while current_symbol != '#' and current_symbol != 'O':
            has_moved = self.step_forward()
            if has_moved:
                current_symbol = self.grid[self.current_X][self.current_Y]
            else:
                return False
        return True

    def turn_right(self):
        match self.current_direction.value:
            case '^':
                self.current_X += 1
                self.current_direction = Directions.RIGHT
            case '>':
                self.current_Y -= 1
                self.current_direction = Directions.DOWN
            case 'v':
                self.current_X -= 1
                self.current_direction = Directions.LEFT
            case '<':
                self.current_Y += 1
                self.current_direction = Directions.UP

    def move(self):
        while self.is_move_possible():
            has_moved = self.move_forward()
            if has_moved:
                self.turn_right()
            else:
                return

    def get_visited_positions(self):
        visited = set((x, y) for x, y, _ in self.visited_positions)
        return len(visited)

def part01():
    with open("test.txt", 'r') as file:
        content = file.read()

    day06 = Day06(content)
    day06.move()
    print(day06.get_visited_positions())

def part02():
    with open("input.txt", 'r') as file:
        content = file.read()

    count = 0
    for i, symbol in enumerate(content):
        if symbol == '.':
            new_content = content[:i] + 'O' + content[i+1:]
            day06part2 = Day06(new_content)
            day06part2.move()
            if day06part2.has_loop:
                count += 1

    print(count)


def main():
    part01()
    part02()

if __name__ == "__main__":
    main()