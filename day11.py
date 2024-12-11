

from collections import defaultdict
file = open('input_files/11.txt', 'r').read()

def blink(numbers : defaultdict):
    stones = defaultdict(int)
    for n in numbers.keys():
        if n == "0":
            stones["1"] += numbers[n]
        elif len(n) % 2 == 0 and len(n)>1:
            l = int(len(n)/2)
            for s in n[:l], n[l:]:
                while len(s) > 1 and s[0] == "0":
                    s = s[1:]
                if len(s)> 0:
                    stones[s] += numbers[n]
        else:
            stones[(str((int(n)*2024)))] += numbers[n]
    return stones

nums = file.split()
stones = defaultdict(int)
for n in nums:
    stones[n] += 1
for i in range(0,25):
    stones = blink(stones)

    
result = 0
for i in stones.keys():
    result += stones[i]
print("Part 1: ", result)

for i in range(0,50):
    stones = blink(stones)

result = 0
for i in stones.keys():
    result += stones[i]
print("Part 2: ", result)
