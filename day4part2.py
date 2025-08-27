WORD='xmas'
WORD_LENGTH=4
with open('data4.txt', 'r') as file:
    grid = []
    for l in file:
        grid.append(l.strip().lower())
    rows=len(grid)
    cols=len(grid[0])
    count = 0
    
    def in_bounds(i,j):
        return 0<=i<rows and 0<=j<cols
    
    def is_mas_triplet(a, b, c):
        return (a == 'm' and b == 'a' and c == 's') or (a == 's' and b == 'a' and c == 'm')

    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if grid[i][j] != 'a':
                continue
            if is_mas_triplet(grid[i-1][j-1], grid[i][j], grid[i+1][j+1]) and is_mas_triplet(grid[i-1][j+1], grid[i][j], grid[i+1][j-1]):
                count += 1
    print(count)

