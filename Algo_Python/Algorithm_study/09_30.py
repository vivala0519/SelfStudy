input = [5, 6, 1, 2, 8, 9, 7]
input = set(input)
print(input)
longest = 0
for i in input:
    if i-1 not in input:
        current = i
        streak = 0
        while i in input:
            i+=1
            streak+=1
            longest = max(longest, streak)
print(longest)