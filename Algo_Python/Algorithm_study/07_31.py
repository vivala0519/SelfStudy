def check_vin(number):
    number = number.upper()
    first_number = number
    res = input_validation(number)
    if res == 'true':
        pass
    else:
        return False
    number = cal(number)
    arr = second_cal(number)
    sum = third_cal(arr)
    mod = fourth_cal(sum)
    res = fifth_cal(mod, first_number)
    print(res)
    if res == 'true':
        return True
    else:
        return False

def cal(number):
    print('in first_method')
    print(number)
    table = str.maketrans('ABCDEFGHJKLMNPRSTUVWXYZ', '12345678123457923456789')
    number = number.translate(table)
    print(number)
    return number

def second_cal(number):
    arr = []
    multiply = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]
    for i in range(0, number.__len__()):
        arr.append(number[i])
    for i in range(0, arr.__len__()):
        arr[i] = arr[i].replace(arr[i], str(int(arr[i]) * multiply[i]))
    print(arr)
    return arr

def third_cal(arr):
    sum = 0
    for i in range(0, arr.__len__()):
        sum += int(arr[i])
    print(sum)
    return sum

def fourth_cal(sum):
    mod = sum % 11
    print('mod = ', mod)
    return mod

def fifth_cal(mod, first_number):
    print('in fifth', mod)
    if mod == 10:
        mod = 'X'
        res = fifth_cal(mod, first_number)
        return res
    elif mod == 'X':
        if first_number[8] == 'X':
            print(mod == 'X')
            res = 'true'
            return res
        else:
            res = 'false'
            return res
    else:
        if first_number[8].isdigit() != False:
            if int(first_number[8]) == mod:
                print('true')
                res = 'true'
                return res
            else:
                print('false')
                res = 'false'
                return res


def input_validation(number):
    print('in valid')
    first_number = number
    res = 'true'
    for i in range(number.__len__()):  # I or O or Q 가 있거나 문자열이 17자가 아니면 return false
        if first_number[i] == 'I':
            res = 'false'
            return res
        if first_number[i] == 'O':
            res = 'false'
            return res
        if first_number[i] == 'Q':
            res = 'false'
            return res
        if number.__len__() != 17:
            res = 'false'
            return res
    return res


import codewars_test as test


@test.describe("Tests")
def tests():
    @test.it("Fixed Tests")
    def fixed_tests():
        test.assert_equals(check_vin("5YJ3E1EA7HF000337"), True)
        test.assert_equals(check_vin("5YJ3E1EAXHF000347"), True)
        test.assert_equals(check_vin("5VGYMVUX7JV764512"), True)
        test.assert_equals(check_vin("7WDMMTDV9TG739741"), False)
        test.assert_equals(check_vin("7JTRH08L5EJ234829"), False)