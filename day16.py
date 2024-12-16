
import copy
import sys
from collections import defaultdict

lines = open('input_files/16.txt', 'r').read().splitlines()
sys.setrecursionlimit(sys.getrecursionlimit()*10)

directions = {"^":(-1,0), ">":(0,1), "v":(1,0), "<":(0,-1)}
opposite = {"^":"v", ">":"<", "v":"^", "<":">"}
goal = 0,0
start = 0,0
walls = defaultdict(lambda:False)
start_direction = ">"

for i,line in enumerate(lines):
    for j,c in enumerate(line):
        if c == "E":
            goal = i,j
        elif c == "S":
            start = i,j
        elif c == "#":
            walls[(i,j)] = True

lowest_cost = [[float('inf') for _ in range(len(lines[0]))] for _ in range(len(lines))]
lowest_cost[start[0]][start[1]] = 0

def step_cost(new_direction : str, old_direction : str):
    if new_direction == old_direction:
        return 1
    return 1001

def find_neighbours(start : tuple[int, int], direction : str):
    neighbours, (x,y) = [], start
    for d, (dx, dy) in directions.items():
        cost = step_cost(d, direction)
        if not walls[(x+dx, y+dy)] and ((lowest_cost[x][y] + cost) < lowest_cost[x+dx][y+dy]):
            lowest_cost[x+dx][y+dy] = lowest_cost[x][y] + cost
            neighbours.append(((x+dx,y+dy), d))
    return neighbours
    
def traverse(s : tuple[int, int], d : str):
    new = find_neighbours(s, d)
    for n,d in new:
        traverse(n, d)

def reverse_and_subtract(start_tile : tuple[int, int], direction : str, tiles : defaultdict):
    (x,y) = start_tile
    for d, (dx, dy) in directions.items():
        next_tile = (x+dx,y+dy)
        if next_tile == start:
            yield from tiles
        elif not walls[next_tile] and lowest_cost[x+dx][y+dy] < tiles[start_tile]: 
            new_tiles = copy.deepcopy(tiles)
            new_tiles[next_tile] = tiles[start_tile] - step_cost(d, direction)
            yield from reverse_and_subtract(next_tile, d, new_tiles)

def traverse_backwards():
    for d in directions:
        p = defaultdict(int)
        p[start] = -1
        p[goal] = lowest_cost[goal[0]][goal[1]]
        yield from reverse_and_subtract(goal,d,p)
    yield goal
    yield start

traverse(start, start_direction)
print("Part 1: ", lowest_cost[goal[0]][goal[1]])
lowest_cost[start[0]][start[1]] = 0
print("Part 2: ", len(set(traverse_backwards())))