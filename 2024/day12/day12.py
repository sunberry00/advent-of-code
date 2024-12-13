from collections import defaultdict, deque


def solve_part1(input_str):
    # Convert input to grid
    grid = input_str.strip().split('\n')

    # Find all regions
    regions = find_regions(grid)

    total_price = 0

    # Calculate price for each region
    for plant_type, plant_regions in regions.items():
        for region in plant_regions:
            area = len(region)
            perimeter = calculate_perimeter(region, grid)
            price = area * perimeter
            total_price += price

    return total_price


def calculate_perimeter(region, grid) -> int:
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for r, c in region:
        # Check all four sides
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_r, new_c = r + dr, c + dc
            # If outside grid or different plant type, add to perimeter
            if (new_r < 0 or new_r >= rows or
                    new_c < 0 or new_c >= cols or
                    (new_r, new_c) not in region):
                perimeter += 1

    return perimeter

def main():
    with open("input.txt", "r") as f:
        puzzle = f.read()

    print(solve_part1(puzzle))
    print(solve_part2(puzzle))

def find_regions(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    regions = defaultdict(list)

    def get_neighbors(r, c):
        neighbors = []
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < rows and 0 <= new_c < cols:
                neighbors.append((new_r, new_c))
        return neighbors

    def find_region(start_r, start_c):
        plant_type = grid[start_r][start_c]
        region = set()
        queue = deque([(start_r, start_c)])

        while queue:
            r, c = queue.popleft()
            if (r, c) in region:
                continue

            region.add((r, c))
            visited.add((r, c))

            for new_r, new_c in get_neighbors(r, c):
                if (new_r, new_c) not in visited and grid[new_r][new_c] == plant_type:
                    queue.append((new_r, new_c))

        return region

    # Find all regions
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                region = find_region(r, c)
                plant_type = grid[r][c]
                regions[plant_type].append(region)

    return regions


def count_sides(region):
    return count_vertical_sides(region, 'up') + \
        count_vertical_sides(region, 'down') + \
        count_horizontal_sides(region, 'left') + \
        count_horizontal_sides(region, 'right')



def count_vertical_sides(region, direction):
    # Group points by row
    rows = {}
    for row, col in region:
        if row not in rows:
            rows[row] = []
        rows[row].append(col)

    # Take only points that have an exposed side in the specified direction
    new_rows = {}
    for row, cols in rows.items():
        new_cols = []
        check_row = row - 1 if direction == 'up' else row + 1
        for col in cols:
            if (check_row, col) not in region:
                new_cols.append(col)
        if new_cols:  # Only add rows that have exposed sides
            new_rows[row] = new_cols

    # Count regions in each row
    total_sides = 0
    for row, cols in new_rows.items():
        cols = sorted(cols)
        regions = 1
        # Check for gaps in consecutive numbers
        for i in range(1, len(cols)):
            if cols[i] - cols[i - 1] > 1:
                regions += 1
        total_sides += regions

    return total_sides


def count_horizontal_sides(region, direction):
    # Group points by column
    cols = {}
    for row, col in region:
        if col not in cols:
            cols[col] = []
        cols[col].append(row)

    # Take only points that have an exposed side in the specified direction
    new_cols = {}
    for col, rows in cols.items():
        new_rows = []
        check_col = col - 1 if direction == 'left' else col + 1
        for row in rows:
            if (row, check_col) not in region:
                new_rows.append(row)
        if new_rows:  # Only add columns that have exposed sides
            new_cols[col] = new_rows

    # Count regions in each column
    total_sides = 0
    for col, rows in new_cols.items():
        rows = sorted(rows)
        regions = 1
        # Check for gaps in consecutive numbers
        for i in range(1, len(rows)):
            if rows[i] - rows[i - 1] > 1:
                regions += 1
        total_sides += regions

    return total_sides

def solve_part2(input_str):
    # Convert input to grid
    grid = input_str.strip().split('\n')

    # Find all regions
    regions = find_regions(grid)

    total_price = 0

    for plant_type, plant_regions in regions.items():
        for region in plant_regions:
            area = len(region)
            sites = count_sides(region)
            price = area * sites
            total_price += price

    return total_price


if __name__ == "__main__":
    main()