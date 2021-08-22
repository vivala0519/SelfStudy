card_numbers = '3285-3764-9934-2453'
card_numbers = card_numbers.split('-')
string = ''
for i in card_numbers:
    string += i
arr = []
for i in range(0, string.__len__()):
    arr.append(string[i])
arr = list(reversed(arr))
print(arr)
tot = 0
jjack = 0
hol = 0
for i in range(0, arr.__len__()):
    if i % 2 == 0:
        if int(arr[i]) * 2 > 9:
            trans = sum(map(int, str(int(arr[i]) * 2)))
        jjack += (int(arr[i]) * 2)
    else:
        hol += int(arr[i])
tot = jjack + hol
if tot % 10 == 0:
    result = 1
else:
    result = 0
print(tot)
