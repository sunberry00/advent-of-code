from typing import Tuple, List


class BridgeRepair:
    @staticmethod
    def parse_import_file(filename: str):
        """
        Parse a file with two sections of import data.

        :param filename: Path to the input file
        :return: A tuple of rules and pages
        """
        with open(filename, 'r') as file:
            content = file.read().strip()
        return content.split('\n')

    @staticmethod
    def solve_part1(content: str) -> None:
        sum = 0
        for equation in content:
            test_value, numbers = BridgeRepair.__parse_equation(equation)
            if BridgeRepair.__check_equation(test_value, numbers):
                sum += test_value

        print(sum)

    @staticmethod
    def __parse_equation(equation: str):
        parts = equation.split(':')
        return int(parts[0]), parts[1].strip()

    @staticmethod
    def __split_and_keep_separators(text):
        result = []
        current = []

        for char in text:
            if char in '*+':
                if current:
                    result.append(''.join(current).strip())
                    current = []
                result.append(char)
            else:
                current.append(char)

        # Add remaining characters if any
        if current:
            result.append(''.join(current).strip())

        return [part for part in result if part]

    @staticmethod
    def __evaluate_equation_left_right(equation: str):
        eq = BridgeRepair.__split_and_keep_separators(equation)
        result = 0
        for i, ch in enumerate(eq):
            if i == 0:
                result = int(ch)
                continue
            if ch.isnumeric():
                if eq[i-1] == '+':
                    result += int(ch)
                elif eq[i-1] == '*':
                    result *= int(ch)
        return result

    @classmethod
    def __check_equation(cls, test_value:int, numbers: str) -> bool:
        if numbers.find(" ") == -1:
            return BridgeRepair.__evaluate_equation_left_right(numbers) == test_value

        sum = BridgeRepair.__check_equation(test_value, numbers.replace(" ", "+", 1))
        mult = BridgeRepair.__check_equation(test_value, numbers.replace(" ", "*", 1))
        return sum or mult

    @staticmethod
    def solve_part1(content: str) -> None:



def main():
    """Main function to run the solution."""
    input = BridgeRepair.parse_import_file("input.txt")
    BridgeRepair.solve_part1(input)

if __name__ == "__main__":
    main()