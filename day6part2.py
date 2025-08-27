with open('data6.txt', 'r') as file:
    grid, start_position = [], (0, 0)
    for i, row in enumerate(file):
        row_data = list(row.strip())
        
        if '^' in row_data:
            j = row_data.index('^')
            start_position = (i, j)
            row_data[j] = '.'
        
        grid.append(row_data)
        
rows = len(grid)
cols = len(grid[0])

def inbounds(position):
    i, j = position
    return 0 <= i < rows and 0 <= j < cols

directions = {
    'up': (-1, 0),
    'right': (0, 1),
    'down': (1, 0),
    'left': (0, -1),
}
directions_list = list(directions.keys())

def move_position(position, direction):
    di, dj = directions[direction]
    i, j = position    
    return (i + di, j + dj)

# First, find all positions visited in the normal path
def get_normal_path():
    curr_pos = start_position
    mode = 'up'
    visited_positions = set([start_position])
    
    next_move = move_position(curr_pos, mode)
    
    while inbounds(next_move):
        ni, nj = next_move
        if grid[ni][nj] == "#":
            mode = directions_list[(directions_list.index(mode) + 1) % 4]
        else: 
            curr_pos = next_move
            visited_positions.add(curr_pos)
        
        next_move = move_position(curr_pos, mode)
    
    return visited_positions

normal_path = get_normal_path()

# Now check each position on the normal path (except start)
infinite_loop_count = 0

for test_pos in normal_path:
    if test_pos == start_position:
        continue
        
    # Simulate with this position blocked
    curr_pos = start_position
    mode = 'up'
    visited_states = set()
    
    next_move = move_position(curr_pos, mode)
    cycle_detected = False
    
    while inbounds(next_move) and not cycle_detected:
        current_state = (curr_pos, mode)
        
        # Check for cycle
        if current_state in visited_states:
            cycle_detected = True
            break
            
        visited_states.add(current_state)
        
        ni, nj = next_move
        # Check if this is our test obstacle position
        if (ni, nj) == test_pos or grid[ni][nj] == "#":
            mode = directions_list[(directions_list.index(mode) + 1) % 4]
        else: 
            curr_pos = next_move
        
        next_move = move_position(curr_pos, mode)
        
        # Safety check
        if len(visited_states) > rows * cols * 4:
            cycle_detected = True
            break
    
    if cycle_detected:
        infinite_loop_count += 1

print(infinite_loop_count)