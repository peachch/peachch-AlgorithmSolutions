
def subarraySum(nums,k):
    sum = [_ for _ in range(len(nums)+1)]
    print(sum)
    for i in range(len(nums)):
        sum[i+1] = sum[i] + nums[i]
    ans = 0
    print(sum)
    for i in range(1,len(nums)+1):
        for j in range(i+1):
            if sum[i] - sum[j] == k:
                ans += 1

    return ans

print(subarraySum([1,1,1],2))