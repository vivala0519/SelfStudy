_list = [{"name": "aba", "weight": 10, "height": 50, "type": "Gibbon"},
             {"name": "abb", "weight": 15, "height": 60, "type": "Gibbon"},
             {"name": "abc", "weight": 20, "height": 50, "type": "Gibbon"},
             {"name": "abd", "weight": 50, "height": 100, "type": "Chimpanzee"}]

gibbon_arr = []
gibbon_value = 0
gorilla_arr = []
gorilla_value = 0
orangutan_arr = []
orangutan_value = 0
chimpanzee_arr = []
chimpanzee_value = 0
for i in range(len(_list)):
    if _list[i]['type'] == 'Gibbon':
        if gibbon_value < _list[i]['weight'] + _list[i]['height']:
            gibbon_arr = []
            gibbon_value = _list[i]['weight'] + _list[i]['height']
            gibbon_arr.append(_list[i]['name'])
        elif gibbon_value == _list[i]['weight'] + _list[i]['height']:
            gibbon_value = _list[i]['weight'] + _list[i]['height']
            gibbon_arr.append(_list[i]['name'])
    elif _list[i]['type'] == 'Gorilla':
        if gorilla_value < _list[i]['weight'] + _list[i]['height']:
            gorilla_arr = []
            gorilla_value = _list[i]['weight'] + _list[i]['height']
            gorilla_arr.append(_list[i]['name'])
        elif gorilla_value == _list[i]['weight'] + _list[i]['height']:
            gorilla_value = _list[i]['weight'] + _list[i]['height']
            gorilla_arr.append(_list[i]['name'])
    elif _list[i]['type'] == 'Orangutan':
        if orangutan_value < _list[i]['weight'] + _list[i]['height']:
            orangutan_arr = []
            orangutan_value = _list[i]['weight'] + _list[i]['height']
            orangutan_arr.append(_list[i]['name'])
        elif orangutan_value == _list[i]['weight'] + _list[i]['height']:
            orangutan_value = _list[i]['weight'] + _list[i]['height']
            orangutan_arr.append(_list[i]['name'])
    elif _list[i]['type'] == 'Chimpanzee':
        if chimpanzee_value < _list[i]['weight'] + _list[i]['height']:
            chimpanzee_arr = []
            chimpanzee_value = _list[i]['weight'] + _list[i]['height']
            chimpanzee_arr.append(_list[i]['name'])
        elif chimpanzee_value == _list[i]['weight'] + _list[i]['height']:
            chimpanzee_value = _list[i]['weight'] + _list[i]['height']
            chimpanzee_arr.append(_list[i]['name'])
gibbon_arr.sort()
gorilla_arr.sort()
chimpanzee_arr.sort()
orangutan_arr.sort()
result = {}
if not gibbon_arr:
    result['Gibbon'] = None
else:
    result['Gibbon'] = gibbon_arr[0]
if not gorilla_arr:
    result['Gorilla'] = None
else:
    result['Gorilla'] = gorilla_arr[0]
if not orangutan_arr:
    result['Orangutan'] = None
else:
    result['Orangutan'] = orangutan_arr[0]
if not chimpanzee_arr:
    result['Chimpanzee'] = None
else:
    result['Chimpanzee'] = chimpanzee_arr[0]
print(gibbon_arr, gorilla_arr, chimpanzee_arr, orangutan_arr)
print(result)

