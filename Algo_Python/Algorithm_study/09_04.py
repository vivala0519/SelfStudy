
st = 'k(a3(b(a2(c))))'
st = st[::-1]
print(st)
result = ''
for i in st:
    if i.isalpha():
        result += i
        print(result)
    elif i.isdigit():
        result = result * int(i)
        print(result)
result = result[::-1]
print(result)