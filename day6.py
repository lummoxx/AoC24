import sys

file = open('input_files/6.txt', 'r').read()
lines = file.splitlines()

sys.setrecursionlimit(sys.getrecursionlimit()*10)
        
for r, l in enumerate(lines):
    if l.count("^") == 1:
        row = r
        for c, n in enumerate(l):
            if n == "^":
                col = c

visited = [list(l) for l in lines]
visited[row][col] = "X"

directions = {"^" : (-1,0), ">":(0,1), "V": (1,0), "<": (0,-1)}
turn = {"^" : ">", ">":"V", "V": "<", "<": "^"}

def move_step(row : int, col : int, guard : str) -> tuple[int, int, str]:
    (r,c) = directions[guard]
    if lines[row+r][col+c] != "#":
        row += r
        col += c
        visited[row][col] = "X"
        return row, col, guard
    else:
        return row, col, turn[guard]

def move(row : int, col : int, guard : str):
    if row == 0 or col == 0 or row == (len(lines)-1) or col == (len(lines[0])-1):
        print(sum([v.count("X") for v in visited]))
    else: 
        row, col, guard = move_step(row, col, guard)
        move(row,col,guard)
        
# part 1:
move(row,col,"^")

def save_step(row : int, col : int, guard : str, steps : dict, map : list) -> tuple[int, int, list, str, bool]:
    (r,c) = directions[guard]
    new_row, new_col = row+r, col+c

    if map[new_row][new_col] != "#":
        if (row, col, new_row, new_col) in steps:
            return new_row, new_col, steps, guard, True
        else:
            steps[(row, col, new_row, new_col)] = True
            return new_row, new_col, steps, guard, False
    else:
        return row, col, steps, turn[guard], False

def find_loop(row : int, col : int, guard : str, map : list) -> int:
    x, y = len(lines),len(lines[0])
    steps = {}
    loop = False
    while((not loop) and row > 0 and col > 0 and row < x-1 and col < y-1):
        row, col, steps, guard, loop = save_step(row, col, guard, steps, map)
    return 1 if loop else 0

def count_loops():
    map = [list(l) for l in lines]
    loops = 0
    for r, l in enumerate(lines):
        for c, n in enumerate(l):
            if lines[r][c] == ".":
                map[r][c] = "#"
                loops += find_loop(row, col, "^", map)
                map[r][c] = "."
    print(loops)

# part 2:
count_loops()