#!/usr/bin/python3
"""0-island_perimeter
"""


def island_perimeter(grid):
    """ returns the perimeter of the
        island described in grid
    """
    rows = len(grid)
    cols = len(grid[0])

    perimeter = 0

    # Direction arrays for exploring neighbors (up, down, left, right)
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:

                # Check each neighbor of the land cell
                for k in range(4):
                    ni = i + dx[k]  # Neighbor's row index
                    nj = j + dy[k]  # Neighbor's column index

                    if ni < 0 or ni >= rows or nj < 0 or nj >= \
                            cols or grid[ni][nj] == 0:
                        perimeter += 1

    return perimeter
