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
