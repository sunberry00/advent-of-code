import os


def read_input(year: int, day: int) -> str:
    """Reads the input for the given year and day from the input directory."""
    file_path = os.path.join('input', str(year), f'day{day:02d}.txt')

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Input file for {year} day {day:02d} not found.")

    with open(file_path, 'r') as file:
        return file.read()