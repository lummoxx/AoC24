
import copy
import sys
from collections import defaultdict
lines = open('input_files/tst2.txt', 'r').read().splitlines()
sys.setrecursionlimit(sys.getrecursionlimit()*10)

directions = {"^":(-1,0), ">":(0,1), "v":(1,0), "<":(0,-1)}
opposite = {"^": "v", ">":"<", "v":"^", "<":">"}
goal = 0,0
start = 0,0
walls = defaultdict(lambda:False)
start_direction = ">"

for i,l in enumerate(lines):
    for j,c in enumerate(l):
        if c == "E":
            goal = i,j
        elif c == "S":
            start = i,j
        elif c == "#":
            walls[(i,j)] = True

distance_matrix = [[float('inf') for _ in range(len(lines[0]))] for _ in range(len(lines))]
distance_matrix[start[0]][start[1]] = 0

def cost(new_direction : str, old_direction : str):
    if new_direction == old_direction:
        return 1
    return 1001

def add_surrounding_distances(start : tuple[int, int], direction : str):
    new_spots = []
    (x,y) = start
    for d in ["^",">","<", "v"] :
        c = cost(d, direction)
        (dx, dy) = directions[d]
        if not walls[(x+dx, y+dy)] and ((distance_matrix[x][y] + c) < distance_matrix[x+dx][y+dy]):
            distance_matrix[x+dx][y+dy] = distance_matrix[x][y] + c
            new_spots.append(((x+dx,y+dy), d))
    return new_spots
    
def traverse(s : tuple[int, int], d : str):
    new = add_surrounding_distances(s, d)
    for n,d in new:
        traverse(n, d)

def subtract(from_tile : tuple[int, int], direction : str, tiles : defaultdict):
    (x,y) = from_tile
    if tiles[from_tile] >= 0:
        for d in ["^",">","<", "v"] :
            (dx, dy) = directions[d]
            if (x+dx,y+dy) == start:
                if tiles[from_tile] == cost(d, opposite[start_direction]):
                    for p in tiles:
                        if tiles[p] > 0:
                            yield p
            elif not walls[(x+dx, y+dy)] and distance_matrix[x+dx][y+dy] <= tiles[from_tile]: 
                new_tiles = copy.deepcopy(tiles)
                new_tiles[(x+dx,y+dy)] = tiles[from_tile] - cost(d, direction)
                yield from subtract((x+dx,y+dy), d, new_tiles)

def traverse_backwards():
    for d in ["^",">","<", "v"]:
        p = defaultdict(int)
        p[start] = -1
        p[goal] = distance_matrix[goal[0]][goal[1]]
        yield from subtract(goal,d, p)
    yield goal
    yield start

traverse(start, start_direction)
print("Part 1: ", distance_matrix[goal[0]][goal[1]])
distance_matrix[start[0]][start[1]] = 0
print("Part 1: ", len(set(traverse_backwards())))
