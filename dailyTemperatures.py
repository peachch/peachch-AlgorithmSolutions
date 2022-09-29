class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        i = len(temperatures) - 1
        ans = [0 for _ in range(i+1) ]
        while i >=0:
            # 这里要用while，要一直判断，直到找到比当前大的，确保stack栈是单调的
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            if stack: ans[i] = stack[-1]-i
            stack.append(i)
            i -= 1
        print(stack)
        return ans

sol = Solution()
print(sol.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))