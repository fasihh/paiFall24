from collections import deque

def jug_problem(x: int, y: int, target: int) -> bool:
    if target > x + y:
        return False
    
    q = deque([(0, 0)])
    visited = set((0, 0))
    while q:
        jug_x, jug_y = q.popleft()
        if jug_x == target or jug_y == target or jug_x + jug_y == target:
            return True

        to_pour_y = min(jug_x, y - jug_y)
        to_pour_x = min(jug_y, x - jug_x)
        neighbors = [
            (x, jug_y),
            (jug_x, y),
            (0, jug_y),
            (jug_x, 0),
            (jug_x - to_pour_y, jug_y + to_pour_y),
            (jug_x + to_pour_x, jug_y - to_pour_x),
        ]

        for neighbor in neighbors:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            q.append(neighbor)

    return False

def test(test_cases):
    errors = []
    def run_test(no, x, y, target):
        try:
            print(f'case #{no+1}: x = {x}, y = {y}, target = {target}')
            assert jug_problem(x, y, target), str(no+1) + ': can\'t get water'
            print('success')
        except AssertionError as error:
            print('failed')
            errors.append(error)

    for i, test_case in enumerate(test_cases):
        run_test(i, *test_case)
    print()
    for error in errors:
        print(error)

print(jug_problem(7, 12, 3))