numbers = [1, 2, 3]
n = len(numbers) + 1
print(n * (n + 1) // 2 - sum(numbers))

result = 0
for i in range(1, max(numbers) + 1):
    if i not in numbers:
        result = i
if result == 0:
    result = max(numbers) + 1
print(result)