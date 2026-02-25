from collections import deque
import math

def water_jug_bfs(capA, capB, target):
    
    if target > max(capA, capB):
        print("Target amount is greater than jug capacities.")
        return
    
    if target % math.gcd(capA, capB) != 0:
        print("No solution possible (fails GCD condition)")
        return

    queue = deque()
    visited = set()
    queue.append((0, 0, []))
    
    while queue:
        a, b, path = queue.popleft()
        
        if (a, b) in visited:
            continue
        visited.add((a, b))

        path = path + [(a, b)]

        if a == target or b == target:
            print("\nSolution found:")
            for step in path:
                print(f"JugA={step[0]}L , JugB={step[1]}L")
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
            if state not in visited:
                queue.append((state[0], state[1], path))

    print("No solution found")
    

capA = int(input("Enter capacity of Jug A: "))
capB = int(input("Enter capacity of Jug B: "))
target = int(input("Enter target amount: "))

water_jug_bfs(capA, capB, target)