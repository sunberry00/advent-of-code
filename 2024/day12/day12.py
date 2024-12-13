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

if __name__ == "__main__":
    main()