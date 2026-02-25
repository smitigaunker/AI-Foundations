import math
def water_jug_dfs(capA, capB, target):

    if target > max(capA, capB):
        print("Target amount is greater than jug capacities.")
        return

    if target % math.gcd(capA, capB) != 0:
        print("No solution possible (fails GCD condition).")
        return

    visited = set()
    solutions = []

    def dfs(a, b, path):
        if (a, b) in visited:
            return

        visited.add((a, b))
        path = path + [(a, b)]

        if a == target or b == target:
            solutions.append(path)
            return

        next_states = [
            (capA, b),
            (a, capB),
            (0, b),
            (a, 0),
        ]

        pour = min(a, capB - b)
        next_states.append((a - pour, b + pour))

        pour = min(b, capA - a)
        next_states.append((a + pour, b - pour))

        for state in next_states:
            dfs(state[0], state[1], path)

    dfs(0, 0, [])

    if solutions:
        print(f"Found {len(solutions)} solution(s):\n")
        for i, solution in enumerate(solutions, 1):
            print(f"Solution {i} ({len(solution)} steps):")
            for step in solution:
                print(f"  JugA={step[0]}L , JugB={step[1]}L")
            print()
    else:
        print("No solution found")


capA = int(input("Enter capacity of Jug A: "))
capB = int(input("Enter capacity of Jug B: "))
target = int(input("Enter target amount: "))

water_jug_dfs(capA, capB, target)