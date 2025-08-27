WORD='xmas'
WORD_LENGTH=4
with open('data4.txt', 'r') as file:
    grid = []
    for l in file:
        grid.append(l.strip().lower())
    rows=len(grid)
    cols=len(grid[0])
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    count = 0
    
    def in_bounds(i,j):
        return 0<=i<rows and 0<=j<cols
    
    def word_matches_in_direction(i, j, di, dj):
        for k in range(len(WORD)):
            ni,nj = i+k*di, j+k*dj
            if not in_bounds(ni, nj) or grid[ni][nj] != WORD[k]:
                return False
        return True
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != WORD[0]:
                continue
            #check each direction
            for di, dj in directions:
                if word_matches_in_direction(i,j,di,dj):
                    count+=1
    print(count)

