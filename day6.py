'''
Immutable objects (integers, strings, tuples): You can't modify the original object

Mutable objects (lists, dictionaries, sets): You can modify the original object

Rebinding a variable (using =) creates a new reference inside the function

Modifying a mutable object affects the original object outside the function
'''
with open('data6.txt', 'r') as file:
    grid,curr_position = [], (0,0)
    for i, row in enumerate(file):
        row_data = list(row.strip())
        
        #find start character
        if '^' in row_data:
            j = row_data.index('^')
            curr_position = (i,j)
            row_data[j] = '.'
        
        grid.append(row_data)
        
    visited = set((curr_position,))
    rows = len(grid)
    cols = len(grid[0])
    def inbounds(position):
        i,j=position
        return 0<=i<rows and 0<=j<cols

    directions = {
        'up': (-1,0),
        'right': (0,1),
        'down': (1,0),
        'left': (0,-1),
    }
    
    def move_position(position, direction):
        di,dj=directions[direction]
        i,j=position    
        return (i+di,j+dj)
    mode = 'up'
    directions_list = list(directions.keys())
    next_move = move_position(curr_position, mode)
    while inbounds(next_move):
        if grid[next_move[0]][next_move[1]] == "#":
            mode = directions_list[(directions_list.index(mode)+1)%4]
        else: 
            curr_position=next_move
            visited.add(curr_position)
        next_move = move_position(curr_position, mode)
        print(curr_position)
    print(len(visited))
    
    