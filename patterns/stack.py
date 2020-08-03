class Solution:
    def dailyTemperatures(self, T):
        stack = []
        ans = [0] * len(T)

        for i in range(len(T)):
            print("==========")
            print(stack)
            print("------")
            while stack and T[i] > T[stack[-1]]:
                j = stack.pop()
                ans[j] = i-j
                print(stack)
            stack.append(i)

        return ans

def test():
    l = [73,74,75,71,69,72,76,73]
    ans = Solution().dailyTemperatures(l)
    print(ans)

if __name__ == '__main__':
    test()