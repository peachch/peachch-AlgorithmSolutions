class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        """
        :param envelopes:
        :return:
        这道题目的解题思路比较巧妙，从第13行之后就是最长子序列的解法。以dp[i]存储当前节点的最大子序列长度。用两个指针进行遍历。
        巧妙之处是之前对待计算的envelopes的排序，这里的排序是，先对x[0]按照升序排列，然后针对x[0]相等的元素，按照x[1]的降序进行排序。
        这样做的原因是，保证当x[0]相等时，x[1]是降序的，那就不会将相等的x[0]（无论几个）计为可以装入的情况。
        """
        # 这里的排序，按照x[0]升序的同时，按照x[1]降序。如果要同时保证这两点，就是将x[0]相同的数据进行了排序。

        _envelopes = sorted(envelopes,key = lambda x:(x[0],-x[1]))
        print(_envelopes)

        height = [[] for _ in range(len(_envelopes))]
        print(_envelopes)
        for i in range(len(_envelopes)):
            height[i] = _envelopes[i][1]
        print(height)

        dp = [1 for _ in range(len(height))]
        for i in range(1,len(height)):
            for j in range(i):
                if height[i] > height[j]:
                    dp[i] = max(dp[i],dp[j] + 1)
        res = 0
        for i in dp:
            res = max(res,i)
        return res



sol = Solution()
print(sol.maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1]]))