title = 'most profit from stock quotes'
quotes = [ 1, 2, 10, 3, 2, 7, 3, 2 ]
# dif = []
# for i in range(0, quotes.__len__() - 1):
#     buy = sum(quotes[0:i+1])
#     profit = quotes.index(quotes[i+1]) * quotes[i + 1]
#     dif.append(profit - buy)
#     print(i+1, buy, profit)
# print(dif)
# result = max(dif)
# if result < 0:
#     result = 0
# print(result)

profit = max_price = 0
quotes.reverse()
print(quotes)
for quote in quotes:
    print(quote)
    max_price = max(quote, max_price)
    print(max_price)
    profit += max_price - quote
    print('profit:', profit)