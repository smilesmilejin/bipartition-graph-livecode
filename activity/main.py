from collections import deque

def possible_bipartition(dislikes):
    group1 = set()
    group2 = set()
    visited = set()
    queue = deque()

    for puppy in dislikes:
        if puppy in visited:
            continue

        # Start with group1
        group1.add(puppy)
        queue.append((puppy, 1))

        while queue:
            current, group = queue.popleft()

            if group == 1:
                group1.add(current)
            else:
                group2.add(current)

            visited.add(current)

            for enemy in dislikes.get(current, []):
                # Assign enemy to opposite group
                if group == 1:
                    if enemy in group1:
                        return False  # Conflict
                    if enemy not in group2:
                        group2.add(enemy)
                        queue.append((enemy, 2))
                else:
                    if enemy in group2:
                        return False  # Conflict
                    if enemy not in group1:
                        group1.add(enemy)
                        queue.append((enemy, 1))

    return True