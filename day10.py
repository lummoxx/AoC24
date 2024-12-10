
file = open('input_files/10.txt', 'r').read()
lines = file.splitlines()

def in_bounds(row : int, col : int) -> bool:
    return (row < len(lines) and col < len(lines[0]) and row > -1 and col > -1)

def follow_trails(row : int, col: int, current : int, found : list):
    if in_bounds(row, col):
        surrounding = [(row+1,col), (row-1, col), (row, col+1),(row, col-1)]
        next_steps = [(r,c) for (r,c) in surrounding if in_bounds(r, c) and int(lines[r][c])==(current+1)]
        if (len(next_steps) > 0):
            for (r,c) in next_steps:
                if (int(lines[r][c])==9):
                    # part 1 additional check and save:
                    # and (r, c) not in found)
                    # found.append((r,c))
                    yield 1
                else:
                    yield from follow_trails(r, c, current+1, found)
        else: yield 0
    else:
        yield 0
    
rs = range(0,len(lines))
cs = range(0, len(lines[0]))
trailheads = 0

for r in rs:
    for c in cs:
        if lines[r][c] == "0":
            trailheads +=  sum(follow_trails(r,c, 0, []))
print(trailheads)
