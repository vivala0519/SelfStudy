nums = [6,2,6,5,1,2]
nums.sort(reverse=True)
print(nums)
print(min(nums[0], nums[1]) + min(nums[2], nums[3]))

temp = []
sum = 0
for i in range(0, len(nums), 2):
    temp.append(nums[i])
    temp.append(nums[i+1])
    sum += min(temp)
    print(temp)
    temp = []
print(sum)

# sum = 0
# pair = []
# for n in nums:
#     pair.append(n)
#     if len(pair) == 2:
#         sum += min(pair)
#         print(pair)
#         pair = []
#
# print(sum)