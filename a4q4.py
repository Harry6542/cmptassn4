#Name - Harry Patel
#NSID-ozc189
#course-CMPT145
#Instructor Name-Laurissa Stilling
def read_maze(file_name):
    with open(file_name, 'r') as file:
        maze_data = [list(line.strip().split()) for line in file]
    return maze_data
def print_maze(maze):
    for row in maze:
        print(' '.join(row))
def SolveMaze(m, s, g):
    row, col = s

    if s == g:
        m[row][col] = 'P'
        return True


    if row < 0 or row >= len(m) or col < 0 or col >= len(m[0]) or m[row][col] != '0':
        return False

    m[row][col] = 'P'
    if SolveMaze(m, (row - 1, col), g) or \
            SolveMaze(m, (row, col - 1), g) or \
            SolveMaze(m, (row + 1, col), g) or \
            SolveMaze(m, (row, col + 1), g):
        return True

        # Backtrack by removing current location from path
        m[row][col] = '0'
        return False