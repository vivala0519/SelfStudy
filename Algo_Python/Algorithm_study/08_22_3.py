import math
recipe = {'eggs': 4, 'flour': 400}
available = {}
arr = []
print(available.__len__())
if available is not None:
    for key, value in recipe.items():
        for a_key, a_value in available.items():
            if not available.get(key):
                print(0)
            if key == a_key:
                arr.append(math.trunc(a_value / value))
else:
    print(0)