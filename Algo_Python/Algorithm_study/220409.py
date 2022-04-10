s = 'apple of banana'
new = []
for string in s.split():
    if len(string) <= 2:
        new.append(string)
    else:
        new.append(string.title())
print(" ".join(new))