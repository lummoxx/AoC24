from collections import namedtuple
input_file = open("input_files/9.txt", "r").read()

def part_1() :
    blocks, id, result = [], 0, 0
    for n,c in enumerate(input_file):
        if n % 2 == 0:
            for i in range(0,int(c)):
                blocks.append(str(id))
            id += 1
        else:
            for i in range(0,int(c)):
                blocks.append(".")
    i, j = 0, len(blocks)-1
    while(j > i):
        if blocks[j] != ".":
            if blocks[i] == ".":
                blocks[i], blocks[j] = blocks[j], blocks[i]
                j -= 1
            i += 1
        else:
            j -= 1
    for i, c in enumerate(blocks):
        if c != ".":
            result += i * int(c) 
    print("Part 1: ", result)


File = namedtuple("File", ["id", "size"])
def parse_files() -> list:
    files = []
    id = 0
    for i,c in enumerate(input_file):
        if i % 2 == 0:
            files.append(File(str(id), int(c)))
            id += 1
        else:
            files.append(File("empty", int(c)))
    return files

def part_2():
    files = parse_files()
    for f in range(len(files)-1, 0, -1):
        move = files[f]
        if move.id != "empty":
            try: 
                slot, val = next(((s, v) for s, v in enumerate(files) if v.id == "empty" and v.size >= move.size and s < f), (None, None))
            except StopIteration: 
                slot, val = None, None
            if slot is not None and val is not None:
                files[f] = File("empty", move.size)
                if val.size > move.size:
                    files.insert(slot+1, File("empty", val.size-move.size))
                files[slot] = move
    result, index = 0, 0
    for file in files:
        if file.id != "empty":
            for i in range(0, file.size):
                result += (index+i) *  int(file.id)
        index += file.size
    print("Part 2: ", result)

part_1()
part_2()

