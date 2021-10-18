arr = ["01:00:00", "02:30:00", "22:00:00"]
total_h = 0
total_m = 0
for i in range(0, len(arr)):
    arr[i] = arr[i].split(':')
    total_h += int(arr[i][0])
    total_m += int(arr[i][1]) / 60
    total_h += total_m
print(total_h)
if total_h > 24:
    result = False
else:
    result = True