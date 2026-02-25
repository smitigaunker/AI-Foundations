def is_valid(m_left, c_left):
    m_right = 3 - m_left
    c_right = 3 - c_left

    if m_left < 0 or c_left < 0 or m_left > 3 or c_left > 3:
        return False

    if m_left > 0 and m_left < c_left:
        return False
    if m_right > 0 and m_right < c_right:
        return False

    return True


def dfs_all():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    stack = [(start, [], "Start")]
    solutions = []

    while stack:
        (m_left, c_left, boat), path, move = stack.pop()

        if (m_left, c_left, boat) in [p[:3] for p in path]:
            continue

        path = path + [(m_left, c_left, boat, move)]

        if (m_left, c_left, boat) == goal:
            solutions.append(path)
            continue

        moves = [
            (1, 0, "One missionary moves"),
            (2, 0, "Two missionaries move"),
            (0, 1, "One cannibal moves"),
            (0, 2, "Two cannibals move"),
            (1, 1, "One missionary and one cannibal move")
        ]

        for m, c, text in moves:
            if boat == 0:
                new_state = (m_left - m, c_left - c, 1)
            else:
                new_state = (m_left + m, c_left + c, 0)

            if is_valid(new_state[0], new_state[1]):
                stack.append((new_state, path, text))

    return solutions


solutions = dfs_all()

print("Total Solutions =", len(solutions))
print()

for i, sol in enumerate(solutions, 1):
    print(f"Solution {i}:")
    for m_left, c_left, boat, move in sol:
        print(f"{move}  ({m_left}, {c_left}, {boat})")
    print()