from utils import lists
file = open('input_files/2.txt', 'r')
lines = file.read().splitlines()


def check(nums : list) -> bool:
    safe, increasing, decreasing = True, nums[1] > nums[0], nums[0] > nums[1]
    for n in range(1,len(nums)):
        gap = nums[n] - nums[n-1]
        if decreasing:
            if not (gap in [-1, -2, -3]):
                return False
        elif increasing:
            if not(gap in [1, 2, 3]):
                return False
        else:
            return False
    return True

count = 0
for l in lines:
    nums = list(map(int, l.split()))
    safe = check(nums)
    if safe:
        count = count + 1 
    else:
        for n in range(0, len(nums)):
            if check(nums[:n] + nums[n+1:]):
                count = count + 1 
                break
print(count)