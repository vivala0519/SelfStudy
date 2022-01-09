n = 5
result = str(1) + '\n'
for i in range(2, n+1):
    result += str(1) + '*'*(i-1) + str(i) + '\n'
print(result.rstrip())