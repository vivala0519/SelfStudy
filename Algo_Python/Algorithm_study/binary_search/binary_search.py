# 이진탐색
import bisect

# 구현
def binary_search(nums, target):
    def bs(start, end):
        if start > end:
            return -1

        mid = (start + end) // 2

        if nums[mid] < target:
            return bs(mid + 1, end)
        elif nums[mid] > target:
            return bs(start, mid - 1)
        else:
            return mid

    return bs(0, len(nums) - 1)

    
# 내장함수
def binary_search_builtin(nums, target):
    # 찾으려는 타겟이 여러개인 경우: 제일 왼쪽 인덱스 반환
    # [-1, 1, 2, 2, 2, 3]  target : 2
    # bisect_left -> 2

    # 타겟이 없는 경우 : 같거나 큰 값 인덱스 반환
    # [-1, 1, 3, 3, 5]  target : 2
    # bisect_left -> 2
    # [-5, -4, -3, -2, -1]  target: 2
    # bisect_left -> 5
    # [3, 4, 5, 6, 7] target: 2
    # bisect_left -> 0
    idx = bisect.bisect_left(nums, target)
    if idx < len(nums) and nums[idx] == target:
        return idx
    else:
        return -1