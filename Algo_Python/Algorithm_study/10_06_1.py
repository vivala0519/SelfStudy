# Preprocess Dates
dates = ["20th Oct 2052", "6th Jun 1933", "26th May 1960", "20th Sep 1958", "16th Mar 2068",
         "25th May 1912", "16th Dec 2018", "26th Dec 2061", "4th Nov 2030", "28th Jul 1963"]
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

for i in range(0, len(dates)):
    temp = []
    temp = dates[i].split(' ')
    dates[i] = temp
print(dates)

for i in range(0, len(dates)):
    if len(dates[i][0]) == 3:
        dates[i][0] = '0' + dates[i][0][0]
    else:
        dates[i][0] = dates[i][0][0:2]
print(dates)

for i in dates:
    if len(str(month.index(i[1]) + 1)) == 1:
        i[1] = '0' + str(month.index(i[1]) + 1)
    else:
        i[1] = str(month.index(i[1]) + 1)
print(dates)

for i in dates:
    i.reverse()
print(dates)

for i in range(0, len(dates)):
    dates[i] = dates[i][0] + '-' + dates[i][1] + '-' + dates[i][2]
print(dates)