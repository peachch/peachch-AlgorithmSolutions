class Solution:
    def advantageCount(self, nums1, nums2):
        sort_a = sorted(nums1, reverse=True)
        sort_b = []
        res = [_ for _ in range(len(nums1))]
        for b in range(len(nums2)):
            sort_b.append([b, nums2[b]])

        sorted_b = sorted(sort_b, key=lambda x: -x[1])
        left = 0
        right = len(sort_a) - 1
        i = 0
        while left <= right:
            if sort_a[left] > sorted_b[i][1]:
                res[sorted_b[i][0]] = sort_a[left]
                left += 1
                i += 1
            else:
                res[sorted_b[i][0]] = sort_a[right]
                right -= 1
                i +=1

        return res



sol = Solution()
print(sol.advantageCount([12,24,8,32],[13,25,32,11]))