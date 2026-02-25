from collections import deque

def is_valid(m_left, c_left):
    m_right = 3 - m_left
    c_right = 3 - c_left

    if m_left < 0 or c_left < 0 or m_left > 3 or c_left > 3:
        return False
    if (m_left > 0 and m_left < c_left):
        return False
    if (m_right > 0 and m_right < c_right):
        return False

    return True


def bfs_unique():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    moves = [
        (1, 0, "One missionary moves"),
        (2, 0, "Two missionaries move"),
        (0, 1, "One cannibal moves"),
        (0, 2, "Two cannibals move"),
        (1, 1, "One missionary and one cannibal move")
    ]

    queue = deque([(start, [])])
    unique_solutions = set()

    while queue:
        (m_left, c_left, boat), path = queue.popleft()

        if (m_left, c_left, boat) in [p[0] for p in path]:
            continue

        path = path + [((m_left, c_left, boat), "Start" if not path else "")]

        if (m_left, c_left, boat) == goal:
            unique_solutions.add(tuple(path))
            continue

        for m, c, rule in moves:
            if boat == 0:
                new_state = (m_left - m, c_left - c, 1)
            else:
                new_state = (m_left + m, c_left + c, 0)

            if is_valid(new_state[0], new_state[1]):
                queue.append((new_state, path[:-1] + [((m_left, c_left, boat), rule)]))

    return unique_solutions


solutions = bfs_unique()

print(f"Total Solutions: {len(solutions)}\n")

for i, sol in enumerate(solutions, 1):
    print(f"Solution {i}:")
    for state, rule in sol:
        if rule:
            print(rule, state)
        else:
            print(state)
    print()