
import requests
import json

r = requests.get('https://coderbyte.com/api/challenges/json/json-cleaning').json()

print(r)
for k, v in list(r.items()):
    if type(v) is dict:
        for k2, v2 in list(v.items()):
            # print(k2, v2)
            if v2 == '' or v2 == 'N/A' or v2 == '-':
                v.pop(k2)
    elif type(v) is list:
        for v2 in v:
            if v2 == '' or v2 == 'N/A' or v2 == '-':
                v.remove(v2)
    else:
        if v == '' or v == 'N/A' or v == '-':
            r.pop(k)
print(r)
