from collections import defaultdict
input_file = open('input_files/15.txt', 'r').read().split("\n\n")

dxdy ={"^":(-1,0), ">":(0,1), "v":(1,0), "<":(0,-1)}
walls = defaultdict(lambda:False)
boxes = defaultdict(lambda:False)
robot = (0,0)
robot_map = input_file[0].splitlines()
moves = input_file[1].replace("\n", "")
length = len(robot_map)
width = len(robot_map[0])

for i,l in enumerate(robot_map):
    for j,c in enumerate(l):
        if c == "@":
            robot = (i,j)
        elif c == "#":
            walls[(i,j)] = True
        elif c == "O":
            boxes[(i,j)] = True

def move_boxes_1(robot : tuple[int, int], box : tuple[int, int], move : tuple[int, int]) -> tuple[int, int]:
    (dx, dy) = move
    (r,c) = box
    to_move = [box]
    next = (r+dx, c+dy)
    while (True):
        if walls[next]:
            to_move = []
            break
        elif boxes[next]:
            to_move.append(next)
            (x,y) = next
            next = (x+dx, y+dy)
        else:
            break
    if len(to_move) > 0:
        (x,y) = to_move[0]
        boxes[(x+dx,y+dy)] = True
        boxes[to_move[0]] = False
        robot = to_move[0]
    for m in to_move[1:]:
        (x,y) = m
        boxes[(x+dx,y+dy)] = True
    return robot

for move in moves:
    (x,y) = dxdy[move]
    (r,c) = robot
    if boxes[((r+x,c+y))]:
        robot = move_boxes_1(robot, (r+x,c+y), (x, y))
    elif not walls[((r+x,c+y))]:
        robot = (r+x,c+y)
        
result = 0
for i in range(length):
    for j in range(width): 
        if boxes[(i,j)]:
            result += 100*i+j
print("Part 1: ", result)

walls = defaultdict(lambda:False)
robot = (0,0)
new_map = [[] for _ in range(len(robot_map))]

for i,l in enumerate(robot_map):
    for j,c in enumerate(l):
        if c == ".":
            new_map[i].append(c)
            new_map[i].append(c)
        if c == "@":
            robot = (i,j*2)
            new_map[i].append(".")
            new_map[i].append(".")
        elif c == "#":
            walls[(i,j*2)] = True
            walls[(i,j*2+1)] = True
            new_map[i].append(c)
            new_map[i].append(c)
        elif c == "O":
            new_map[i].append("[")
            new_map[i].append("]")
length = len(new_map)
width = len(new_map[0])

def connected(move : tuple[int,int]):
    (x,y) = move
    if new_map[x][y] == "[":
        return (x,y+1)
    if new_map[x][y] == "]":
        return (x,y-1)

def affected(moving : list, delta):
    (dx, dy) = delta
    also_moves = []
    for m in moving:
        (x,y)= m
        if x+dx < length and y+dy < width and new_map[x+dx][y+dy] in ["[","]"] and (x+dx, y+dy) not in moving + also_moves:
            also_moves.append((x+dx, y+dy))
            (cx, cy) = connected((x+dx, y+dy))
            also_moves.append((cx, cy))
    return also_moves

def not_clear(delta : tuple[int,int], to_move : list) -> bool:
    (dx, dy) = delta
    return any([walls[(x+dx,y+dy)] for (x,y) in to_move])

def move_boxes_2(robot : tuple[int, int], first : tuple[int, int], delta : tuple[int, int]) -> tuple[int, int]:
    (dx, dy) = delta
    to_move = [first, connected(first)]
    while (True):
        if not_clear(delta, to_move):
            to_move = []
            break
        new = affected(to_move, delta)
        if len(new) != 0:
            to_move = to_move + new
        else:
            break
    tmp = []
    to_move.reverse()
    for m in to_move:
        (x,y) = m
        tmp.append((m, new_map[x][y]))
    for m in tmp:
        ((x,y), c) = m
        new_map[x+dx][y+dy] = c
        new_map[x][y] = "."
    if len(to_move) > 0:
        return first
    return robot


for move in moves:
    (x,y) = dxdy[move]
    (r,c) = robot
    if new_map[r+x][c+y] == "#":
        continue
    if new_map[r+x][c+y] == ".":
        robot = (r+x,c+y)
    else:
        robot = move_boxes_2(robot, (r+x,c+y), (x, y))
    
result = 0
for i,l in enumerate(new_map):
    for j,c in enumerate(l):
        if c == "[":
            result += 100*i+j
print("Part 2: ", result)