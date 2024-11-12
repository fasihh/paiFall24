
def dfs(board: list[list[int]], visited: set, r: int = 0, c: int = 0, idx: int = 0):
    n = len(board)
    if idx == n*n:
        return True

    if (r, c) in visited or r < 0 or c < 0 or c >= n or r >= n:
        return False
    
    board[r][c] = idx
    visited.add((r, c))

    neighbors = [
        (r+1, c+2),
        (r-1, c+2),
        (r+1, c-2),
        (r-1, c-2),
        (r+2, c+1),
        (r-2, c+1),
        (r+2, c-1),
        (r-2, c-1),
    ]

    for nr, nc in neighbors:
        if dfs(board, visited, nr, nc, idx + 1):
            return True

    board[r][c] = -1
    visited.remove((r, c))

    return False

def main():
    n = 6
    board = [[-1] * n for _ in range(n)]
    visited = set()

    print(f'knight\'s tour for {n}x{n}')
    if dfs(board, visited):
        print(*board, sep='\n')
    else:
        print('no solution')

if __name__ == '__main__':
    main()
