# phase 1 plus BONUS

# define the initial maze
maze = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1],
    [0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0,0,0]
    ]

def path(maze, moves):
    '''FIND THE SHORTEST PATH THROUGH THE MAZE'''
    
    'MAZE PROPERTIES'
    num_rows = len(maze)
    num_cols = len(maze[0])
    
    # start and end points can be altered
    end_pt = (num_cols - 1, num_rows - 1)
    start_pt = (0, 0)

    'BREATH FIRST SEARCH'
    # dictionary of visited points
    visited = {end_pt: None}
    
    # queue of next points to visit
    queue = [end_pt]
    
    # positions of removed obstructions
    change = set()
    
    # while loop through the queue
    while queue:
        current = queue.pop(0)
        if current == start_pt:
            shortest_path = []
            while current:
                shortest_path.append(current)
                current = visited[current]
            return shortest_path, change
        
        # initialize the list of adjacent points to the current point
        adj_points = []

        'FIND ADJACENT POINTS'
        # up, right, down, left, and diagonals
        allowed_moves = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        
        # current collumn, current row
        col, row = current
        
        # check if the potential new position is within the boundaries, been seen before or has an obstruction
        for dc, dr in allowed_moves:
            new_c, new_r = col+dc, row+dr

            if 0<= new_c < num_cols and 0<= new_r < num_rows :
                # check that the new position is free of obstructions
                if maze[new_r][new_c] == 0 :
                    adj_points.append((new_c, new_r))
                    
                # check if we are allowed to remove the obstruction
                elif moves > 0:
                    moves -= 1
                    change.add((new_c, new_r))
                    adj_points.append((new_c, new_r))

        'LOOP THROUGH ADJACENT POINTS'
        for point in adj_points:
            # add adjacent point to queue if it has not been visited before
            if point not in visited:
                visited[point] = current
                queue.append(point)

def shortestPath(maze, moves = 0):
    '''DETERMINING THE NUMBER OF OBJECTS THAT NEED TO BE MOVED FOR SHORTEST PATH'''
    # number of objects moved
    obj_moved = moves
    
    # test if such path is possible
    Path = path(maze, obj_moved)
    if Path != None:
        # no moved objects
        if Path[1] == set():
            return "The shortest distance is {} using the following path: {}.".format(len(Path[0])-1,Path[0])
        # with moved objects
        else:
            print("Unable to reach delivery point")
            return "The shortest distance is {} using the following path: {} and with moved objects at {}.".format(len(Path[0])-1, Path[0], [x for x in Path[1] if x in Path[0]])
    
    # recursive step if no such path exists
    else:
        return shortestPath(maze, obj_moved+1)

Path = shortestPath(maze,0)
print(Path)

# phase 2 
def randomizeGrid(maze, blocks):
    '''ADDS RANDOMLY LOCATED OBSTRUCTIONS TO THE MAZE DENOTED BY 1S'''
    import numpy
    import random
    
    'MAZE PROPERTIES'
    num_rows = len(maze)
    num_cols = len(maze[0])
    end_pt = (num_cols - 1, num_rows - 1)
    start_pt = (0, 0)

    # obstruction locations in a set to avoid repeats
    # can be altered if the maze is altered to avoid repeats
    positions = set([(9,7),(8,7),(7,7),(7,8)]) 
    
    'RANDOM OBSTRUCTIONS'
    # number of obstructions previously
    prev_obs = len(positions)
    
    # while loop until the number of obstructions is sufficient
    while len(positions) < blocks + prev_obs:
        rand_row = numpy.random.randint(0, num_rows)
        rand_col = numpy.random.randint(0, num_cols)
        positions.add((rand_col, rand_row))
        
        # remove obstructions if they coincide with the start and/or end points
        positions.discard(start_pt)
        positions.discard(end_pt)
       
    'ALTER THE MAZE'
    for i in positions:
        maze[i[1]][i[0]] = 1
        
    return maze

maze1 = randomizeGrid(maze, 20)

print(shortestPath(maze1,0))
maze1
