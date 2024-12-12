
from collections import defaultdict

input_file = open('input_files/12.txt', 'r').read()
lines = input_file.splitlines()

def in_bounds( row : int, col : int) -> bool:
    return (row < len(lines) and col < len(lines[0]) and row > -1 and col > -1)

def find_region(ch : str, row : int, col: int, visited : list):
    if in_bounds(row, col) and lines[row][col] == ch:
        surrounding = [(row+1,col), (row-1, col), (row, col+1),(row, col-1)]
        nert_steps = [(r,c) for (r,c) in surrounding if in_bounds(r, c) and lines[r][c] == ch and (r,c) not in visited]
        if (len(nert_steps) > 0):
            for (r,c) in nert_steps:
                if lines[r][c]==ch:
                    visited.append((r,c))
                    yield from find_region(ch, r, c, visited)
                    yield (r,c)
        yield (row,col)

def find_plots() -> defaultdict:
    plots = defaultdict(list)
    for r in range(0, len(lines)):
        for c in range(0, len(lines[0])):
            foundshape = False
            for s in plots[lines[r][c]]:
                if (r,c) in s:
                    foundshape = True
                    break
            if not foundshape:
                shape = list(set(find_region(lines[r][c], r, c, [(r,c)])))
                plots[lines[r][c]].append(shape)
    return plots

def find_surrounding(coordinates) -> list:
    surrounding = []
    for (r,c) in coordinates:
        surrounding.append((r, c+1))
        surrounding.append((r, c-1))
        surrounding.append((r+1, c))
        surrounding.append((r-1, c))

    return [item for item in surrounding if item not in coordinates]

def all_sides(coordinates) -> int:
    surrounding = find_surrounding(coordinates)
    result = len(surrounding)
    per_col = defaultdict(list)
    per_row = defaultdict(list)
    for (r,c) in surrounding:
        per_col[c].append(r)
        per_row[r].append(c)
    for c in per_col.keys():
        vals = sorted(per_col[c])
        if len(vals) > 1 :
            prev =  vals[0]
            for row in vals[1:]:
                if abs(row-prev) == 1:
                    result -= 1
                prev = row
    for r in per_row.keys():
        vals = sorted(per_row[r])
        if len(vals) > 1 :
            prev = vals[0]
            for c in vals[1:]:
                if abs(c-prev) == 1:
                    result -= 1
                prev = c
    return result

def expand(coordinates:list)-> list:
   return [(x, y) for (r, c) in coordinates for x in [r*3, r*3+1, r*3+2] for y in [c*3, c*3+1, c*3+2]]

result_1 = 0
result_2 = 0
plots = find_plots()
for p in plots.keys():
    for shape in plots[p]:
        ls = all_sides(expand(shape))
        result_1 += len(shape) * len(find_surrounding(shape))
        result_2 += len(shape) * ls
print("Part 1:, ", result_1)
print("Part 2: ", result_2)