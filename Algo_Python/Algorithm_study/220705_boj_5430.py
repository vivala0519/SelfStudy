from collections import deque
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(","))

    if '' in arr:
        arr.pop()

    reverse = 0
    error = 0

    for cmd in p:
        if cmd == "R":
            reverse += 1
        else:
            if len(arr) < 1:
                error = 1
                break
            else:
                if reverse % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()

    if error == 1:
        print("error")
    else:
        if reverse % 2 == 0:
            print("[" + ",".join(arr) + "]")
        else:
            arr.reverse()
            print("[" + ",".join(arr) + "]")