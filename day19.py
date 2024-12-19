[towel_lines, pattern_lines] = open('input_files/19.txt', 'r').read().split("\n\n")
towel_designs, patterns = towel_lines.split(", "), pattern_lines.split("\n")

def can_create_pattern(designs, pattern):
    dp = [False] * (len(pattern) + 1)
    dp[0] = True 
    for i in range(1, len(pattern) + 1):
        for d in designs:
            if i >= len(d) and pattern[i-len(d):i] == d and dp[i-len(d)]:
                dp[i] = True
                break
    return dp[len(pattern)]

def number_of_ways(designs, pattern):
    dp = [0] * (len(pattern) + 1)
    dp[0] = 1
    for i in range(1, len(pattern) + 1):
        for d in designs:
            if i >= len(d) and pattern[i-len(d):i] == d:
                dp[i] += dp[i-len(d)]
    return dp[len(pattern)]

def num_possible(designs : list, patterns : list) -> int:
    num_possible = 0
    num_ways = 0
    for p in patterns:
        if can_create_pattern(designs, p):
            num_possible += 1
            num_ways += number_of_ways(designs,p)
    return num_possible,num_ways
 
part_1, part_2 = num_possible(towel_designs, patterns)
print("Part 1: ", part_1)
print("Part 2: ", part_2)