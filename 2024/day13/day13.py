from sympy import symbols, Eq, solve, Rational

def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Returns (gcd, x, y) where gcd is the greatest common divisor of a and b
    and x, y are coefficients where ax + by = gcd
    """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def find_solution(a1: int, a2: int, target: int) -> tuple[int, int] | None:
    """
    Find x, y where a1*x + a2*y = target
    Returns None if no solution exists
    """
    gcd, x0, y0 = extended_gcd(a1, a2)

    if target % gcd != 0:
        return None

    # Scale up the base solution
    x0 *= target // gcd
    y0 *= target // gcd

    # Find the step sizes for the general solution
    step_y = a1 // gcd
    step_x = -a2 // gcd

    # Find a solution with minimum non-negative x and y
    # Move solution until both x and y are non-negative
    k = 0
    while x0 + k * step_x < 0 or y0 + k * step_y < 0:
        k += 1

    return (x0 + k * step_x, y0 + k * step_y)


def solve_claw_machine(button_a, button_b, prize):
    # We need to solve two equations:
    # a_presses * button_a_x + b_presses * button_b_x = prize_x
    # a_presses * button_a_y + b_presses * button_b_y = prize_y

    ax, ay = button_a
    bx, by = button_b
    px, py = prize

    a, b = symbols('a b')
    equation1 = Eq(a * ax + b * bx, px)
    equation2 = Eq(a * ay + b * by, py)

    solution = solve((equation1, equation2), (a, b))
    return solution



def process_input(input_text: str) -> list[dict]:
    machines = []
    current_machine = {}

    for line in input_text.strip().split('\n'):
        if not line:
            if current_machine:
                machines.append(current_machine)
                current_machine = {}
            continue

        if line.startswith('Button A:'):
            x, y = map(int, line.replace('Button A: X+', '').replace(' Y+', '').split(','))
            current_machine['button_a'] = (x, y)
        elif line.startswith('Button B:'):
            x, y = map(int, line.replace('Button B: X+', '').replace(' Y+', '').split(','))
            current_machine['button_b'] = (x, y)
        elif line.startswith('Prize:'):
            x, y = map(int, line.replace('Prize: X=', '').replace(' Y=', '').split(','))
            current_machine['prize'] = (x + 10000000000000, y + 10000000000000)

    if current_machine:
        machines.append(current_machine)

    return machines


def solve_all_machines(input_text: str) -> int:
    machines = process_input(input_text)
    total_tokens = 0

    for i, machine in enumerate(machines, 1):
        solution = solve_claw_machine(
            machine['button_a'],
            machine['button_b'],
            machine['prize']
        )

        if type(list(solution.values())[0]) is Rational or type(list(solution.values())[1]) is Rational:
            continue

        a_presses, b_presses = solution.values()
        tokens = 3 * a_presses + b_presses
        print(f"Machine {i}: {a_presses} A presses, {b_presses} B presses = {tokens} tokens")
        total_tokens += tokens

    return total_tokens

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        puzzle = f.read()

    result = solve_all_machines(puzzle)
    print(f"\nTotal tokens needed: {result}")