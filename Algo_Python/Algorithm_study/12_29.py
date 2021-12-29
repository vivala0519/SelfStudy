s = '-+-+-+'

result = len(s) + (len(s) - 1)
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        result += 5
print(result)