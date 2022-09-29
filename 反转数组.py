



nums = ["123ss","345","asd"]

for i in range(len(nums)):
    left = 0
    right = len(nums[i])-1
    # new = [_ for _ in range(right+1)]
    # while left < right:
    #     print(item)
    #     temp = item[left]
    #     new[left] = item[right]
    #     new[right] = temp
    #     left += 1
    #     right -= 1
    item_l = list(nums[i])
    print(item_l[right::-1])
    nums[i] = "".join(i for i in item_l[::-1])
    # print(new)

print(nums)