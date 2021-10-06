a = [4, 3, 57]
b = [2, 4, 49]

result = []
for k in range(0, len(a)):
    temp = 0
    for x in range(0, a[k] + 1):
        for y in range(0, a[k] + 1):
            if x + y == a[k] and y - x == b[k]:
                temp = 2 * x + 3 * y
    result.append(temp)
print(result)


# result = []
# for k in range(0, len(a)):
#     temp = (0, 0)
#     for x in range(0, a[k]+1):
#         for y in range(0, a[k]+1):
#             if x + y == a[k]:
#                 if y >= x:
#                     if y - x == b[k]:
#                         temp = (x, y)
#     print(temp)
#     fun = 2 * temp[0] + 3 * temp[1]
#     print(fun)
#     result.append(fun)
# print(result)