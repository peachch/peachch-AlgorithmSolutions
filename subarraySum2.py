
def subarraySum(nums,k):
    sum = {}
    sum[0] =1
    ans = 0
    sum_i = 0
    for i in range(len(nums)):
        sum_i += nums[i]
        sum_j = sum_i - k

        if sum.get(sum_j):
            print(sum_j)
            ans += sum.get(sum_j)
            print(ans)

        # 如果在sum中没找到前缀和则设置其为0，如果找到则用原始的数据+1
        sum[sum_i] =  sum.setdefault(sum_i,0)+1
        print(sum)



    return ans

print(subarraySum([3,5,2,-2,4,1],5))