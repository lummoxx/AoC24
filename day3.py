
import math

file = open('input_files/3.txt', 'r')
lines = file.read()

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) 


def muls(ls : str) -> int:
    result = 0
    mul =""
    search = True
    idxs = find_all(ls, "mul(")
    for idx in idxs:
        idx2 = ls.find(")", idx)
        mul = ls[idx+4:idx2]
        nums = mul.split(',')
        if all(map(str.isdigit, nums)):
            result = result + math.prod(map(int, nums))
    return result

final = 0

donts = lines.split("don't()")
final = final + muls(donts[0])
for d in donts[1:]:
    dos = d.find("do()")
    final = final + muls(d[dos:])
print(final)
        
    