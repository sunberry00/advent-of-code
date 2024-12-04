import typing


class Day04:
    XMAS_PATTERN = "XMAS"

    @staticmethod
    def _is_valid_slice_start(x: int, y: int, rows: int, cols: int, pattern_length: int,
                              directions: typing.Tuple[int, int]) -> bool:
        """
        Check if the starting position is valid for a given direction.

        :param x: Row index
        :param y: Column index
        :param rows: Total number of rows
        :param cols: Total number of columns
        :param pattern_length: Length of the pattern to match
        :param directions: Tuple of row and column direction increments
        :return: Boolean indicating if the starting position is valid
        """
        dx, dy = directions

        # Check bounds in both row and column directions
        return (0 <= x + dx * (pattern_length - 1) < rows and
                0 <= y + dy * (pattern_length - 1) < cols)

    @classmethod
    def _create_slice(cls, x: int, y: int, puzzle: typing.List[str],
                      directions: typing.Tuple[int, int],
                      pattern_length: int = 4) -> str:
        """
        Create a slice of characters based on given directions.

        :param x: Starting row index
        :param y: Starting column index
        :param puzzle: 2D grid of characters
        :param directions: Tuple of row and column direction increments
        :param pattern_length: Length of the slice to create
        :return: Slice of characters
        """
        dx, dy = directions
        return ''.join(
            puzzle[x + dx * i][y + dy * i]
            for i in range(pattern_length)
        )

    @classmethod
    def check_xmas_direction(cls, x: int, y: int, puzzle: typing.List[str],
                             directions: typing.Tuple[int, int]) -> bool:
        """
        Check if a specific direction from (x, y) forms the XMAS pattern.

        :param x: Starting row index
        :param y: Starting column index
        :param puzzle: 2D grid of characters
        :param directions: Tuple of row and column direction increments
        :return: Boolean indicating if XMAS pattern is found
        """
        rows, cols = len(puzzle), len(puzzle[0])

        if not cls._is_valid_slice_start(x, y, rows, cols, 4, directions):
            return False

        slice_chars = cls._create_slice(x, y, puzzle, directions)
        return slice_chars == cls.XMAS_PATTERN

    @classmethod
    def check_a_pattern(cls, x: int, y: int, puzzle: typing.List[str]) -> int:
        """
        Check for the specific 'A' pattern around a given position.

        :param x: Row index
        :param y: Column index
        :param puzzle: 2D grid of characters
        :return: 1 if pattern is valid, 0 otherwise
        """
        rows, cols = len(puzzle), len(puzzle[0])

        # Check bounds
        if x <= 0 or y <= 0 or x >= rows - 1 or y >= cols - 1:
            return 0

        # Check both diagonal directions for 'MAS' or 'SAM'
        first_diagonal = puzzle[x - 1][y - 1] + "A" + puzzle[x + 1][y + 1]
        second_diagonal = puzzle[x + 1][y - 1] + "A" + puzzle[x - 1][y + 1]

        valid_first = first_diagonal in ["MAS", "SAM"]
        valid_second = second_diagonal in ["MAS", "SAM"]

        return int(valid_first and valid_second)

    @classmethod
    def solve_part1(cls, puzzle: typing.List[str]) -> int:
        """
        Solve part 1 by finding XMAS patterns in all 8 directions.

        :param puzzle: 2D grid of characters
        :return: Count of XMAS patterns
        """
        # Directions: N, NE, E, SE, S, SW, W, NW
        directions = [
            (-1, 0),  # North
            (-1, 1),  # Northeast
            (0, 1),  # East
            (1, 1),  # Southeast
            (1, 0),  # South
            (1, -1),  # Southwest
            (0, -1),  # West
            (-1, -1)  # Northwest
        ]

        count = 0
        for row in range(len(puzzle)):
            for col in range(len(puzzle[row])):
                if puzzle[row][col] == "X":
                    count += sum(
                        cls.check_xmas_direction(row, col, puzzle, direction)
                        for direction in directions
                    )
        return count

    @classmethod
    def solve_part2(cls, puzzle: typing.List[str]) -> int:
        """
        Solve part 2 by finding 'A' patterns.

        :param puzzle: 2D grid of characters
        :return: Count of 'A' patterns
        """
        return sum(
            cls.check_a_pattern(row, col, puzzle)
            for row in range(len(puzzle))
            for col in range(len(puzzle[row]))
            if puzzle[row][col] == "A"
        )


def main():
    with open("input.txt", "r") as file:
        puzzle = file.read().split("\n")

    print("Part 1:", Day04.solve_part1(puzzle))
    print("Part 2:", Day04.solve_part2(puzzle))


if __name__ == "__main__":
    main()