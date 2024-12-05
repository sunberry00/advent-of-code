from typing import List, Tuple


class Day05:
    @classmethod
    def parse_import_file(cls, filename: str):
        """
        Parse a file with two sections of import data
        :param filename: path to file
        """
        with open(filename, 'r') as file:
            content = file.read().strip()

        pipe_section, comma_section = content.split('\n\n')

        pipe_pairs = [tuple(map(int, line.split('|'))) for line in pipe_section.split('\n')]
        comma_lists = [list(map(int, line.split(','))) for line in comma_section.split('\n')]

        return pipe_pairs, comma_lists

    @classmethod
    def check_rule(cls, left, right, page: List[int]):
        return page.index(left) < page.index(right)

    @classmethod
    def is_rule_applied(cls, left, right, page):
        return left in page and right in page

    @classmethod
    def solve_part1(cls, rules, pages):
        correct_pages = pages.copy()
        incorrect_pages = []
        for page in pages:
            for left, right in rules:
                if Day05.is_rule_applied(left, right, page):
                    if Day05.check_rule(left, right, page):
                        continue
                    else:
                        incorrect_pages.append(page) # for part 2
                        correct_pages.remove(page)
                        break

        middle_page_numbers = [page[len(page) // 2] for page in correct_pages]

        print(sum(middle_page_numbers))

        return correct_pages

    @classmethod
    def solve_part2(cls, pages, rules):
        print(pages)



def main():
    rules, pages = Day05.parse_import_file("test.txt")
    correct_pages = Day05.solve_part1(rules, pages)
    incorrect_pages = set(pages).difference(set(correct_pages))
    Day05.solve_part2(incorrect_pages, rules)


if __name__ == "__main__":
    main()