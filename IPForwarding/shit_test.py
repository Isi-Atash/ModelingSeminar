def is_path_clear(obstacles, point):
    """ Check if the given point is free of obstacles. """
    return point not in obstacles

def count_paths(m, n, obstacles):
    """ Count all the possible paths the ant can take to reach (m, n) avoiding the obstacles. """
    # Create a 2D list (array) to store the number of ways to reach each cell
    dp = [[0] * (n+1) for _ in range(m+1)]

    # Set the starting point, there is one way to reach (0,0)
    dp[0][0] = 1

    # Fill the dp table
    for i in range(m+1):
        for j in range(n+1):
            # If current cell is blocked, no path is possible
            if not is_path_clear(obstacles, (i, j)):
                dp[i][j] = 0
            else:
                # If moving right is within the grid, add paths from the left cell
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                # If moving up is within the grid, add paths from the bottom cell
                if j > 0:
                    dp[i][j] += dp[i][j-1]

    # The bottom-right cell will have the total number of paths
    return dp[m][n]

# Obstacles on the grid
obstacles = {(1,3), (3,3), (3,6), (4,3), (6,4), (6,6), (14,12)}

# Size of the grid (15x15)
m, n = 17,18

# Count the number of paths
num_paths = count_paths(m, n, obstacles)
print(num_paths)
