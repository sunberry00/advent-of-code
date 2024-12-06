from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import List, Tuple, Optional


class Direction(Enum):
    """Represents possible movement directions with their symbols and coordinate changes."""
    UP = ('^', -1, 0)
    RIGHT = ('>', 0, 1)
    DOWN = ('v', 1, 0)
    LEFT = ('<', 0, -1)

    @property
    def symbol(self) -> str:
        return self.value[0]

    @property
    def delta(self) -> Tuple[int, int]:
        return self.value[1], self.value[2]

    @classmethod
    def from_symbol(cls, symbol: str) -> Optional['Direction']:
        return next((d for d in cls if d.symbol == symbol), None)

    def turn_right(self) -> 'Direction':
        """Returns the direction after turning 90 degrees right."""
        directions = list(Direction)
        current_index = directions.index(self)
        return directions[(current_index + 1) % len(directions)]


@dataclass
class Position:
    """Represents a position on the grid with row and column coordinates."""
    row: int
    col: int

    def move(self, direction: Direction) -> 'Position':
        """Returns a new position after moving in the given direction."""
        delta_row, delta_col = direction.delta
        return Position(self.row + delta_row, self.col + delta_col)

    def __str__(self) -> str:
        return f"{self.col}, {self.row}"  # Note: x = col, y = row


@dataclass
class PathStep:
    """Represents a single step in the path."""
    position: Position
    direction: Direction

    def __str__(self) -> str:
        return f"{self.position}, {self.direction.symbol}"


class GridNavigator:
    """Handles navigation and path marking on a 2D grid."""

    def __init__(self, input_str: str):
        self.grid = [list(line) for line in input_str.strip().splitlines()]
        self.position = self._find_start_position()
        if not self.position:
            raise ValueError("No valid starting position found in grid")
        self.direction = Direction.from_symbol(self.grid[self.position.row][self.position.col])
        if not self.direction:
            raise ValueError(f"Invalid direction symbol at starting position")
        self.path: List[PathStep] = []
        # Record initial position
        self._record_step()

    def _record_step(self):
        """Records current position and direction in path."""
        self.path.append(PathStep(Position(self.position.row, self.position.col), self.direction))

    def _find_start_position(self) -> Optional[Position]:
        """Finds the starting position marked by a direction symbol."""
        for row_idx, row in enumerate(self.grid):
            for col_idx, cell in enumerate(row):
                if cell in (d.symbol for d in Direction):
                    return Position(row_idx, col_idx)
        return None

    def is_within_bounds(self, position: Position) -> bool:
        """Checks if the given position is within grid boundaries."""
        return (0 <= position.row < len(self.grid) and
                0 <= position.col < len(self.grid[0]))

    def can_move_forward(self) -> bool:
        """Checks if movement in current direction is possible and won't hit an obstacle."""
        next_position = self.position.move(self.direction)
        if not self.is_within_bounds(next_position):
            return False
        return self.grid[next_position.row][next_position.col] != '#'

    def step_forward(self) -> bool:
        """Moves one step forward if possible, marking the path."""
        if not self.can_move_forward():
            return False

        # Mark current position as visited
        self.grid[self.position.row][self.position.col] = 'X'

        # Move to next position
        self.position = self.position.move(self.direction)
        self._record_step()
        return True

    def move_forward_until_obstacle(self) -> bool:
        """Moves forward until about to hit a wall or boundary."""
        moved = False
        while self.can_move_forward():
            self.step_forward()
            moved = True
        return moved

    def navigate(self):
        """Main navigation logic: move forward until wall, then turn right."""
        while True:
            if self.move_forward_until_obstacle():
                self.direction = self.direction.turn_right()
                self._record_step()  # Record the turn
            else:
                # Mark final position before stopping
                self.grid[self.position.row][self.position.col] = 'X'
                break

    def count_visited_positions(self) -> int:
        """Counts positions marked as visited ('X')."""
        return sum(row.count('X') for row in self.grid)

    def print_grid(self):
        """Prints the current state of the grid."""
        for row in self.grid:
            print(''.join(row))

    def print_path(self):
        """Prints the full path in x, y, direction format."""
        for step in self.path:
            print(step)


def solve_part1(input_path: str) -> int:
    """Solves part 1 of the puzzle and prints the path."""
    content = Path(input_path).read_text()
    navigator = GridNavigator(content)
    navigator.navigate()
    print("\nPath taken:")
    navigator.print_path()
    return navigator.count_visited_positions()


def main():
    result = solve_part1("input.txt")
    print(f"\nPart 1 solution: {result}")


if __name__ == "__main__":
    main()