import copy
file = open('input_files/9.txt', 'r').read()

blocks = []
id = 0

for n,c in enumerate(file):
    if n % 2 == 0:
        for i in range(0,int(c)):
            blocks.append(str(id))
        id += 1
    else:
        for i in range(0,int(c)):
            blocks.append(".")

reversed_blocks = copy.deepcopy(blocks)
reversed_blocks.reverse()

def part_1(blocks : list) -> list:
    to_remove = 0
    for i,c in enumerate(reversed_blocks):
        if c != "." :
            if blocks.count(".") > 0:
                next = blocks.index(".")
                blocks[next] = c
                to_remove += 1
            else: 
                break
    return blocks[:len(blocks)-to_remove]

def remove_moved_file(f: list, i:int):
    dots = ["."] * len(f) 
    blocks[len(blocks)-i:len(blocks)-i+len(f)] = dots

def find_empty_slot(i : int, last : int)-> tuple[int,int]:
    i = blocks.index(".", i)
    j = i
    while(i < last and blocks[i+1] == "."):
        i += 1
    return (j,i+1)

def next_file(i : int) -> tuple[int, list]:
    while reversed_blocks[i] == ".":
        i += 1
    f = [reversed_blocks[i]]
    i +=1
    while(i < len(reversed_blocks) and reversed_blocks[i] == f[0]):
        f.append(reversed_blocks[i])
        i += 1
    return i, f

def part_2(blocks : list) -> list:
    (x,y) = find_empty_slot(0, len(blocks))
    i, f = next_file(0)
    while (i < len(reversed_blocks)):
        if y-x >= len(f):
            blocks[x:x+len(f)] = f
            remove_moved_file(f, i)
            i, f = next_file(i)
            if blocks[0:len(blocks)-i].count(".")>0:
                (x,y) = find_empty_slot(0,len(blocks)-i)
            else: 
                break
        else:
            if blocks[y:len(blocks)-i].count(".")>0:
                (x,y) = find_empty_slot(y, len(blocks)-i)
            else:
                if (i < len(reversed_blocks)):
                    i, f = next_file(i)
                    (x,y) = find_empty_slot(0, len(blocks)-i)
                else: 
                    break
    return blocks
                
result = 0
for i, c in enumerate(part_1(blocks)):
    if c != ".":
        result += i * int(c) 

print(result)

