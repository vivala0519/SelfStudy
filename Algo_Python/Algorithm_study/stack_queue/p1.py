def is_valid(s):
    pair = {
        '}': '{',
        ')': '(',
        ']': '['
    }
    opener = '{[('
    stack = []
    for char in s:
        if char in opener:
            stack.append(char)
            pass
        else:
            if not stack:
                return False
            top = stack.pop()
            if pair[char] != top:
                return False

    return not stack

assert is_valid("{}()[]")
assert is_valid('{[]}')
assert not is_valid('{{}}}}')