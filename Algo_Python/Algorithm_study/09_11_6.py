def convert_notation(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    return convert_notation(q, base) + T[r] if q else T[r]

n = 110011
k = 10
trans = '0123456789ABCDEF'
text = str(convert_notation(n, k))
text = text.split('0')
text = [v for v in text if v]
print(text)
prime = []
for item in text:
    item = int(item)
    b = 0
    for i in range(2, item):
        if item % i == 0:
            b = 1
    if b == 1 or item == 1:
        pass
    else:
        prime.append(item)
answer = len(prime)
