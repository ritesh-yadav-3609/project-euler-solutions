
def routes_count(n: int) -> int:
    """
    Return value of number of routes are there through a nxn grid
    """
    grid = [[0]*(n+1) for i in range(0,n+1)]
    for i in range(n, -1, -1):
        for j in range(n, -1, -1):
            if i < j:
                continue
            if i == n:
                grid[i][j] = 1
            elif i == j:
                grid[i][j] = 2 * grid[i+1][j]
            else:
                grid[i][j] = grid[i+1][j] + grid[i][j+1]        
    return grid[0][0]

if __name__ == "__main__":
    print("Number of routes are there through a 20×20 grid is by moveing only to the right and down is", routes_count(20))
