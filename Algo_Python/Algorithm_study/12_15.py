import math
mins = 45
if mins <= 65:
    print(30)
else:
    print(30 + math.ceil((mins - 65) / 30) * 10)

