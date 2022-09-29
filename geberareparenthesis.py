class Solution:
    def generateParenthesis(self, n: int):
        def backtrack(left,right,track):
            if left == 0 and right == 0:
                res.append("".join(track))
                return
            # 这里的判断应该优先，basecase，停止条件应该放在最上面，确保可以在进入递归之前跳出
            if left > right:
                return
            if left >0:
                track.append("(")
                backtrack(left-1,right,track)
                track.pop()
            if right > 0:
                track.append(")")
                backtrack(left,right-1,track)
                track.pop()

        res = []
        backtrack(n,n,[])
        return res

sol = Solution()
print(sol.generateParenthesis(2))