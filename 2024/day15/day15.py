class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0]) if self.height > 0 else 0
        self.__find_initial_state()

    def __find_initial_state(self):
        """Locate the robot's initial position."""
        self.robot_x = -1
        self.robot_y = -1
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == "@":
                    self.robot_x = i
                    self.robot_y = j
                    return
        raise ValueError("No robot (@) found in grid")

    def __is_valid_position(self, x, y):
        """Check if a position is within grid boundaries."""
        return 0 <= x < self.height and 0 <= y < self.width

    def __get_direction_offset(self, command):
        """Convert movement command to coordinate offsets."""
        return {
            '^': (-1, 0),
            'v': (1, 0),
            '<': (0, -1),
            '>': (0, 1)
        }.get(command, (0, 0))

    def __can_push_box(self, start_x, start_y, dx, dy):
        """Check if a box can be pushed in the given direction and return the final position."""
        curr_x, curr_y = start_x, start_y

        # Look ahead until we find either a wall, another box, or an empty space
        while self.__is_valid_position(curr_x + dx, curr_y + dy):
            next_x, next_y = curr_x + dx, curr_y + dy
            next_cell = self.grid[next_x][next_y]

            if next_cell == '#':  # Hit a wall
                return False, curr_x, curr_y
            elif next_cell == 'O':  # Found another box
                curr_x, curr_y = next_x, next_y
                continue
            elif next_cell == '.':  # Found empty space
                return True, next_x, next_y

        return False, curr_x, curr_y

    def move_robot(self, command):
        """Move the robot according to the given command."""
        if command not in {'^', 'v', '<', '>'}:
            return False

        dx, dy = self.__get_direction_offset(command)
        new_x, new_y = self.robot_x + dx, self.robot_y + dy

        # Check if the move is within boundaries
        if not self.__is_valid_position(new_x, new_y):
            return False

        target_cell = self.grid[new_x][new_y]

        if target_cell == '.':  # Moving to empty space
            self.grid[self.robot_x][self.robot_y] = '.'
            self.grid[new_x][new_y] = '@'
            self.robot_x, self.robot_y = new_x, new_y
            return True

        elif target_cell == 'O':  # Trying to push a box
            can_push, final_x, final_y = self.__can_push_box(new_x, new_y, dx, dy)

            if can_push:
                # Move all boxes one step in the direction
                curr_x, curr_y = final_x - dx, final_y - dy
                while curr_x != new_x - dx or curr_y != new_y - dy:
                    self.grid[curr_x + dx][curr_y + dy] = 'O'
                    curr_x -= dx
                    curr_y -= dy

                # Move the first box to its new position
                self.grid[final_x][final_y] = 'O'
                # Move the robot
                self.grid[new_x][new_y] = '@'
                self.grid[self.robot_x][self.robot_y] = '.'
                self.robot_x, self.robot_y = new_x, new_y
                return True

        return False

    def get_box_gps_coordinates(self):
        """
        Calculate GPS coordinates for all boxes in the grid.
        GPS coordinate = 100 * (distance from top) + (distance from left)
        Returns a list of GPS coordinates for all boxes.
        """
        gps_coordinates = []

        # Find all boxes and calculate their GPS coordinates
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == 'O':
                    # Calculate GPS coordinate
                    # Distance from top edge is i
                    # Distance from left edge is j
                    gps_coordinate = 100 * i + j
                    gps_coordinates.append(gps_coordinate)

        return sorted(gps_coordinates)

    def get_grid(self):
        """Return the current state of the grid."""
        return self.grid


def parse_input(puzzle):
    lines = puzzle.split()

    grid = []
    i = 0
    line = lines[i]
    while '^' not in line:
        l = []
        for j, symbol in enumerate(line):
            l.append(symbol)
        grid.append(l)
        line = lines[i + 1]
        i += 1

    commands = []
    for j, line in enumerate(lines[i:]):
        for symbol in line:
            commands.append(symbol)

    return grid, commands


def solve_part1(puzzle, commands):
    warehouse = Grid(puzzle)
    for command in commands:
        warehouse.move_robot(command)
        pass

    print(sum(warehouse.get_box_gps_coordinates()))


def main():
    with open("input.txt", "r") as f:
        puzzle = f.read()

    grid, commands = parse_input(puzzle)
    solve_part1(grid, commands)

if __name__ == "__main__":
    main()