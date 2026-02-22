def gridChallenge(grid):
    sorted_grid = []
    for row in grid:
        sorted_grid.append(sorted(row))

    rows = len(sorted_grid)
    cols = len(sorted_grid[0])

    for c in range(cols):
        for r in range(1, rows):
            if sorted_grid[r - 1][c] > sorted_grid[r][c]:
                return "NO"
    return "YES"
