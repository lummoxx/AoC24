import itertools
from collections import defaultdict

file = open('input_files/8.txt', 'r').read()
lines = file.splitlines()
locations = defaultdict(list)
antinodes_1, antinodes_2 = [], []
length = len(lines)
rs = range(0,length)

def add_if_in_bounds(x : int, y : int):
    if (x < length and y < length and y > -1 and x > -1):
        antinodes_1.append((x,y))

def add_antinodes(locs : tuple[tuple[int, int],tuple[int,int]]):
    ((x1,y1),(x2,y2)) = locs
    dx, dy =  x2-x1, y2-y1
    
    x1 -= dx
    x2 += dx
    y1 -= dy
    y2 += dy
    
    add_if_in_bounds(x1, y1)
    add_if_in_bounds(x2, y2)
    
def line(locs : tuple[tuple[int, int],tuple[int,int]]):
    ((x1, y1), (x2, y2)) = locs
    dx, dy = x1-x2, y1-y2
    x = x1
    y = y1
    while (x < length and y < length and x > -1 and y > -1):
        antinodes_2.append((x,y))
        x += dx
        y += dy
    x = x2
    y = y2
    while (x < length and y < length and x > -1 and y > -1):
        antinodes_2.append((x,y))
        x += dx
        y += dy
     
for r in rs:
    for c in rs:
        if lines[r][c] != ".":
            locations[lines[r][c]].append((c,r))
            
for k,v in locations.items():
    pairs = []
    for pair in itertools.product(v, v):
        if pair[0]!=pair[1]:
            pairs.append(pair)
    for pair in set(pairs):
        add_antinodes(pair)
        line(pair)

print("Part 1: " + str(len(set(antinodes_1))))
print("Part 2: " + str(len(set(antinodes_2))))