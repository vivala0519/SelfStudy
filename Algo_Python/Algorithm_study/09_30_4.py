input = [1, 3, 2, 6]
n = input[0]
print(input[n:])
result = []
result = input[n:]
print(result)
rest = input[0:n]
result = result + rest
sdf = ''
for i in result:
    sdf += str(i)
print(sdf)