from typing import List, Tuple


class PageSorter:
    @staticmethod
    def parse_import_file(filename: str) -> tuple[list[tuple[int, ...]], list[list[int]]]:
        """
        Parse a file with two sections of import data.

        :param filename: Path to the input file
        :return: A tuple of rules and pages
        """
        with open(filename, 'r') as file:
            content = file.read().strip()

        pipe_section, comma_section = content.split('\n\n')

        rules = [tuple(map(int, line.split('|'))) for line in pipe_section.split('\n')]
        pages = [list(map(int, line.split(','))) for line in comma_section.split('\n')]

        return rules, pages

    @staticmethod
    def is_page_order_correct(page: List[int], left: int, right: int) -> bool:
        """
        Check if the order of two elements in a page is correct.

        :param page: List of page numbers
        :param left: First element to check
        :param right: Second element to check
        :return: Boolean indicating if the order is correct
        """
        return page.index(left) < page.index(right)

    @staticmethod
    def solve_part1(rules: List[Tuple[int, int]], pages: List[List[int]]) -> List[List[int]]:
        """
        Solve part 1 of the problem by finding incorrect pages.

        :param rules: List of rules (left, right)
        :param pages: List of pages
        :return: List of incorrect pages
        """
        incorrect_pages = []
        correct_pages = pages.copy()

        for page in pages:
            for left, right in rules:
                if left in page and right in page:
                    if not PageSorter.is_page_order_correct(page, left, right):
                        incorrect_pages.append(page)
                        correct_pages.remove(page)
                        break

        # Calculate and print middle page numbers for correct pages
        middle_page_numbers = [page[len(page) // 2] for page in correct_pages]
        print(f"Part 1 solution: {sum(middle_page_numbers)}")

        return incorrect_pages

    @staticmethod
    def correct_page(page: List[int], left: int, right: int) -> List[int]:
        """
        Correct the order of two elements in a page.

        :param page: Original page
        :param left: First element to swap
        :param right: Second element to swap
        :return: Corrected page
        """
        # Create a copy of the page as a list to modify
        page_copy = list(page)
        left_index = page_copy.index(left)
        right_index = page_copy.index(right)
        page_copy[left_index], page_copy[right_index] = page_copy[right_index], page_copy[left_index]
        return page_copy

    @staticmethod
    def solve_part2(pages: List[List[int]], rules: List[Tuple[int, int]]) -> None:
        """
        Solve part 2 by correcting pages according to rules.

        :param pages: List of pages to correct
        :param rules: List of rules to apply
        """

        def is_all_pages_correct(current_pages):
            """Check if all pages are correctly ordered."""
            return all(
                PageSorter.is_page_order_correct(page, left, right)
                for page in current_pages
                for left, right in rules
                if left in page and right in page
            )

        corrected_pages = pages.copy()
        iterations = 0
        max_iterations = 1000  # Prevent infinite loop

        while not is_all_pages_correct(corrected_pages) and iterations < max_iterations:
            new_corrected_pages = []
            for page in corrected_pages:
                page_corrected = False
                for left, right in rules:
                    if left in page and right in page:
                        if not PageSorter.is_page_order_correct(page, left, right):
                            new_page = PageSorter.correct_page(page, left, right)
                            new_corrected_pages.append(new_page)
                            page_corrected = True
                            break
                if not page_corrected:
                    new_corrected_pages.append(page)

            # Remove duplicates and update pages
            corrected_pages = list({tuple(page) for page in new_corrected_pages})
            iterations += 1

        # Calculate middle page numbers
        middle_page_numbers = [page[len(page) // 2] for page in corrected_pages]
        print(f"Part 2 solution: {sum(middle_page_numbers)}")


def main():
    """Main function to run the solution."""
    rules, pages = PageSorter.parse_import_file("input.txt")
    incorrect_pages = PageSorter.solve_part1(rules, pages)
    PageSorter.solve_part2(incorrect_pages, rules)


if __name__ == "__main__":
    main()