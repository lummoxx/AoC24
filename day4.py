 
file = open('input_files/4.txt', 'r').read()
lines = file.splitlines()

next = { "X" : "M", "M":"A", "A":"S", "S":"" }
count = 0

def findVertical(r : int, c : int) -> int:
    # upwards
    if r > 2:
        if lines[r-1][c] == next["X"] and lines[r-2][c] == next["M"] and lines[r-3][c] == next["A"]:
            yield 1
    # downwards
    if r < len(lines)-3:
        if lines[r+1][c] == next["X"] and lines[r+2][c] == next["M"] and lines[r+3][c] == next["A"]:
            yield 1
    return 0

def findDiagonal(r: int, c : int) -> int:
    # upwards
    if r > 2:
        # to the right
        if c < len(lines[0])-3:
            if lines[r-1][c+1] == next["X"] and lines[r-2][c+2] == next["M"] and lines[r-3][c+3] == next["A"]:
                yield 1
        # to the left
        if c > 2:
            if lines[r-1][c-1] == next["X"] and lines[r-2][c-2] == next["M"] and lines[r-3][c-3] == next["A"]:
                yield 1
    # downwards
    if r < len(lines)-3:
        # to the right
        if c < len(lines[0])-3:
            if lines[r+1][c+1] == next["X"] and lines[r+2][c+2] == next["M"] and lines[r+3][c+3] == next["A"]:
                yield 1
        # to the left
        if c > 2:
            if lines[r+1][c-1] == next["X"] and lines[r+2][c-2] == next["M"] and lines[r+3][c-3] == next["A"]:
                yield 1
    return 0
    
for l in lines:
    count = count + l.count("XMAS") + l.count("SAMX")
print(count)

rs = range(0,len(lines))
cs = range(0, len(lines[0]))

for r in rs:
    for c in cs:
        if lines[r][c] == "X":
            count = count + sum(findVertical(r,c)) + sum(findDiagonal(r,c))
print("Part 1: " + str(count))
        
nextR = { "M":"", "A":"M", "S":"A" }

def downRightMAS(r : int, c : int) -> bool:
    if lines[r][c] == "M" :
        if r < len(lines)-2:
            # to the right
            if c < len(lines[0])-2:
                if lines[r+1][c+1] == next["M"] and lines[r+2][c+2] == next["A"]:
                    return True
    return False

def downLeftMAS(r : int, c : int) -> bool:
    if lines[r][c] == "M" :
        if r < len(lines)-2:
            # to the left
            if c > 1:
                if lines[r+1][c-1] == next["M"] and lines[r+2][c-2] == next["A"]:
                    return True
    return False

def downRightSAM(r : int, c : int) -> bool:
    if lines[r][c] == "S" :
        if r < len(lines)-2:
            # to the right
            if c < len(lines[0])-2:
                if lines[r+1][c+1] == nextR["S"] and lines[r+2][c+2] == nextR["A"]:
                    return True
    return False

def downLeftSAM(r : int, c : int) -> bool:
    if lines[r][c] == "S" :
        if r < len(lines)-2:
            # to the left
            if c > 1:
                if lines[r+1][c-1] == nextR["S"] and lines[r+2][c-2] == nextR["A"]:
                    return True
    return False
  
count = 0
rs = range(0,len(lines)-2)
cs = range(0, len(lines[0])-2)

for r in rs:
    for c in cs:
        if lines[r][c] == "M" or lines[r][c] == "S":
            downr = downRightMAS(r,c) or downRightSAM(r,c)
            snddownl = downLeftMAS(r,c+2) or downLeftSAM(r,c+2)

            if downr and snddownl :
                count = count + 1
print("Part 2: " + str(count))

