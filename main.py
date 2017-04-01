import random
class Location:             # simple coordinate system class. Similar to Vector2 in Unity C#
    def __init__(self, x, y):
        self.x = x
        self.y = y

# modifiable variables
N = 3                       # size of grid (N * N)
M = 0                       # number of obstacles
verbose = False             # print everything that ever happens. debug stuff
printPath = True            # print all the possible paths. takes significantly longer than just calculating the number of paths

# we have already set M and N, but we can alternatively have user set
N = int(input("Size of Grid (N * N): "))            # ask user for size of grid
M = int(input("Number of obstacles: "))             # and number of obstackes

# create the basic array and Location. These are duplicated by each branch of the function
initLocation = Location(0,0)                        # start at 0,0
initPosArray = []                                   # list to store the previous 'moves'
grid = [[0 for x in range(N)] for y in range(N)]    # grid is created based on N
pathCount = 0                                       # global variable for number of possible paths

def can_move_down(currLocation):
    # returns true if the location below is not an obstacle or end of grid
    if (currLocation.x + 1 < N):
        if(grid[currLocation.x + 1][currLocation.y] == 0): return True
        else: return False
    else: return False
        
def can_move_right(currLocation):
    # returns true if the location to the right is not an obstacle or end of grid
    if (currLocation.y + 1 < N):
        if(grid[currLocation.x][currLocation.y + 1] == 0): return True
        else: return False
    else: return False

def generate_grid ():
    # prints grid size and obstacles
    print("\nObstacles (M) =", M)
    # this generates the grid
    for _ in range(M):
        random_x = random.randint(0, N - 1)
        random_y = random.randint(0, N - 1)
        # make sure you dont set two obstacles on the same pos
        while (grid[int(random_x)][int(random_y)] == 1):
            random_x = random.randint(0, N - 1)
            random_y = random.randint(0, N - 1)
        grid[int(random_x)][int(random_y)] = 1
        # print the location of the object
        print ("Obstacle at: [" + str(random_x) + "," + str(random_y) + "]")
    # visualise grid
    print("\nGrid size (N) =", N)
    for row in grid:
        for column in row:
            print(column, end="")
        print(end="\n")
    print("")

def find_next(currLocation, posArray):
    # print current location (only if logging enabled)
    if (verbose): print("Current Location: [" + str(currLocation.x) + "," + str(currLocation.y) + "]")

    # if we are in the bottom right corner, success! Add this path to the global successful path count
    if (currLocation.x == N - 1 and currLocation.y == N - 1):
        if (verbose): print("SUCCESSFULLY REACHED END")
        global pathCount
        pathCount += 1
        posArray.append(currLocation)
        if (printPath):
            print ("Path " + str(pathCount), end= ": ")
            for i in posArray:
                print("(" + str(i.x) + "," + str(i.y) + ")", end=" ")
            print(end="\n")

    # check if we can move down, if so, run this function again, using those new coordinates
    if (can_move_down(currLocation)):
        newArray = list(posArray)
        newArray.append(currLocation)
        find_next(Location(currLocation.x + 1, currLocation.y), newArray)
    else:
        # we can't move down. it's either the bottom of the grid or we have hit an obstacle
        if (currLocation.x + 1 == N):
            if (verbose): print("Hit the bottom")
        else:
            if (verbose): print("Found obstacle at: [" + str(currLocation.x + 1) + "," + str(currLocation.y) + "]")

    # check if we can move right, if so, run this function again, using those new coordinates    
    if (can_move_right(currLocation)):
        newArray = list(posArray)
        newArray.append(currLocation)
        find_next(Location(currLocation.x, currLocation.y + 1), newArray)
    else:
        # we can't move right. it's either the right side of the grid or we have hit an obstacle
        if (currLocation.y + 1 == N):
            if (verbose): print("Hit the right side")
        else:
            if (verbose): print("Found obstacle at: [" + str(currLocation.x) + "," + str(currLocation.y + 1) + "]")
            
# initialize grid, setting up random obstacles     
generate_grid()
# begin the recursive function
find_next(initLocation, initPosArray)
# print the final count of paths
print ("Number of possible paths: " + str(pathCount))
