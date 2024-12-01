import heapq

file = open('input_files/1.txt')
lines, left, right, dists, occurences = file.readlines(),[],[],[],[]
for l in lines :
    line = l.split()
    right.append(int(line[1]))
    left.append(int(line[0]))
left.sort(), right.sort()

def part1() :
    for i in range(len(right)) :
        dists.append(abs(left[i] - right[i]))
    print(sum(dists))

def part2() :
    for l in left :
        times = right.count(l)
        occurences.append(l*times)
    print(sum(occurences))
