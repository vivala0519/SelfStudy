fizzbuzz = []
n = 15
for i in range(1, n+1):
    fizzbuzz.insert(i, i)

for i in range(0, n):
    if fizzbuzz[i] % 3 == 0 and fizzbuzz[i] % 5 == 0:
        fizzbuzz[i] = 'FizzBuzz'
    elif fizzbuzz[i] % 3 == 0:
        fizzbuzz[i] = 'Fizz'
    elif fizzbuzz[i] % 5 == 0:
        fizzbuzz[i] = 'Buzz'
    else:
        pass
print(fizzbuzz)