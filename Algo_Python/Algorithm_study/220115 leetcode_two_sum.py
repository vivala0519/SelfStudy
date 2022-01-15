nums = [3, 3]
target = 6

# 풀이2 in을 이용
# for i in range(len(nums)):
#     if target - nums[i] in nums[i+1:]:
#         print(i, nums[i+1:].index(target - nums[i]) + (i + 1))

# 풀이3 딕셔너리 이용
# dic = {}
# for i, num in enumerate(nums):
#     dic[num] = i
#
# for i in range(len(nums)):
#     if target - nums[i] in dic and i != dic[target - nums[i]]:
#         print(i)

# 풀이 5
# temp = sorted(nums)
# left, right = 0, len(nums) - 1
# while left != right:
#     if temp[left] + temp[right] > target:
#         right -= 1
#         print('rigth - 1')
#     elif temp[left] + temp[right] < target:
#         left += 1
#         print('left + 1')
#     else:
#         print(nums.index(temp[left]), nums.index(temp[right]))
#         break