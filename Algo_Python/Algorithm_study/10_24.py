bus_stops = [[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]
temp = 0
for i in bus_stops:
    temp += i[0] - i[1]
