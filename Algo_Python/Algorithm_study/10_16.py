import re

registered_list = ["apple1", "orange", "banana3"]
new_id = 'apple'

if new_id in registered_list:
    if new_id.isalpha() == True:
        new_id += str(1)
    while new_id in registered_list:
        number = int(''.join(re.findall('\d', new_id)))
        number += 1
        new_id = ''.join(re.findall('[a-zA-Z]', new_id)) + str(number)
print(new_id)
