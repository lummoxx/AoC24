from utils import lists
file = open('input_files/2.txt', 'r')
lines = file.read().splitlines()


def check(nums : list) -> bool :
    safe = True
    increasing = int(nums[1]) > int(nums[0])
    decreasing = int(nums[0]) > int(nums[1])
    for n in range(1,len(nums)):
        gap = int(nums[n]) - int(nums[n-1])
        if decreasing :
            if not (gap in [-1, -2, -3]):
                safe = False
        elif increasing :
            if not(gap in [1, 2, 3]):
                safe = False
        else :
            safe = False
    return safe

count = 0
for l in lines :
    nums = l.split()
    safe = check(nums)
    if (safe) :
        count = count + 1 
    else :
        safe = False
        for n in range(0, len(nums)):
            if check(nums[:n] + nums[n+1:]):
                safe = True
        if (safe) :
            count = count + 1 
print(count)