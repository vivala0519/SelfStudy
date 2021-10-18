leave = 4
day = 'FRI'
holidays = [6, 21, 23, 27, 28]

weekend = [[6, 7, 13, 14, 20, 21, 27, 28], [5, 6, 12, 13, 19, 20, 26, 27], [4, 5, 11, 12, 18, 19, 25, 26], [3, 4, 10, 11, 17, 18, 24, 25], [2, 3, 9, 10, 16, 17, 23, 24, 30], [1, 2, 8, 9, 15, 16, 22, 23, 29, 30], [1, 7, 8, 14, 15, 21, 22, 28, 29]]

arr = list(range(0, 30))
for i in range(0, len(arr)):
    arr[i] = 0
print(arr)

day_list = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
if day in day_list:
    day = day_list.index(day)
print(day)
for j in range(0, len(weekend[day])):
    arr[weekend[day][j]-1] = 1
print(arr)

for i in range(0, len(holidays)):
    arr[holidays[i]-1] = 1
print(arr)