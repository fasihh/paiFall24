import numpy as np
from math import sin, cos, radians, ceil, pi
import os
import time

def print_plane(grid: np.array):
    print(*['  '.join(row) for row in grid], sep='\n')

def rotate(vec: tuple, angle: float) -> np.array:
    angle = radians(angle)
    return np.matmul(
        np.array([*vec]),
        np.array([
            [cos(angle), -sin(angle)],
            [sin(angle), cos(angle) ]
        ]
    ))

def generate_square_points(side_length: int, points_per_edge: int) -> dict:
    points = {}
    half_side = side_length // 2

    # Define the corners of the square
    corners = [
        (-half_side, half_side),   # Top-left
        (half_side, half_side),    # Top-right
        (half_side, -half_side),   # Bottom-right
        (-half_side, -half_side)   # Bottom-left
    ]
    
    # Calculate points along the top, right, bottom, and left edges
    for i in range(points_per_edge + 1):
        t = i / points_per_edge  # Interpolation factor between 0 and 1

        # Top edge (left to right)
        points[len(points)] = (corners[0][0] * (1 - t) + corners[1][0] * t, corners[0][1])

        # Right edge (top to bottom)
        points[len(points)] = (corners[1][0], corners[1][1] * (1 - t) + corners[2][1] * t)

        # Bottom edge (right to left)
        points[len(points)] = (corners[2][0] * (1 - t) + corners[3][0] * t, corners[2][1])

        # Left edge (bottom to top)
        points[len(points)] = (corners[3][0], corners[3][1] * (1 - t) + corners[0][1] * t)

    return points

def generate_star_points(num_points: int, radius: float) -> dict:
    points = {}
    center = (0, 0)
    angle_between_points = 2 * pi / num_points

    for i in range(num_points):
        # Use alternating radii for sharp and blunt angles of the star
        r = radius if i % 2 == 0 else radius / 2
        theta = i * angle_between_points
        x = r * cos(theta)
        y = r * sin(theta)
        points[i] = (x, y)
    
    return points

def main():
    m, n = 19, 19
    delay = int(input('delay: '))
    angle = float(input('angle: '))
    num_points = int(input('points: '))
    length = int(input('length: '))
    # points = dict()
    # for i in range(num_points):
    #     points[i] = (np.random.randint(-m//2, m//2), np.random.randint(-n//2, n//2))
    points = generate_square_points(length, num_points)

    while True:
        os.system('cls')
        grid = np.array([' '] * n*m).reshape((m, n))
        for symbol in points:
            new_point = rotate(points[symbol], angle)
            int_point = np.round(new_point).astype(dtype=np.int32)
            if abs(int_point[0]) < n//2 and abs(int_point[1]) < m//2:
                grid[int_point[1] + m//2, int_point[0] + n//2] = symbol
                points[symbol] = new_point
        print_plane(grid)
        time.sleep(delay/1000)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass