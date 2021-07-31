def check_vin(number):
    first_number = number  # 나중에 유효성 검사를 위한 초기 문자열 저장
    multiply = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]

    # 1번 처리 메소드
    table = str.maketrans('ABCDEFGHJKLMNPRSTUVWXYZ', '12345678123457923456789')
    number = number.translate(table)

    # 2번 처리 메소드
    arr = []
    for i in range(0, number.__len__()):
        arr.append(number[i])
    for i in range(0, arr.__len__()):
        arr[i] = arr[i].replace(arr[i], str(int(arr[i]) * multiply[i]))

    # 3번 처리 메소드
    sum = 0
    for i in range(0, arr.__len__()):
        sum += int(arr[i])

    # 4번 처리 메소드
    mod = sum % 11

    # 5번 처리 메소드
    if first_number[8].isdigit() == False:
        pass
    else:
        if int(first_number[8]) == mod:
            return True

    # 유효성 검사
    if mod == 10:  # mod가 10이면 true
        return True

    for i in range(number.__len__()):  # I or O or P 가 있거나 문자열이 17자가 아니면 return false
        if first_number[i] == 'I':
            return False
        if first_number[i] == 'O':
            return False
        if first_number[i] == 'P':
            return False
        if number.__len__() != 17:
            return False

    return False