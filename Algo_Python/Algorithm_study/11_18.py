items = ['a', 'b', 'c']
index = -5
default_value = 'd'
try:
    if index < len(items):
        print(items[index])
    else:
        print(default_value)
except:
    print(default_value)