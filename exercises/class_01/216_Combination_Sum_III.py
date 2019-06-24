# https://leetcode.com/problems/combination-sum-iii/

class Solution(object):
    ans = []
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        def dfs(pos, res, tmpsum):
            if tmpsum == n:
                if len(res) == k:
                    self.ans.append(list(res))
                return

            if tmpsum > n:
                return

            if pos == len(numbers):
                return

            for idx in range(0, 2):
                if idx == 0:
                    dfs(pos + 1, res, tmpsum)
                else:
                    res.append(numbers[pos])
                    dfs(pos + 1, res, tmpsum + numbers[pos])
                    res.remove(numbers[pos])


        numbers = [1,2,3,4,5,6,7,8,9]

        self.ans = []
        dfs(0, [], 0)
        return self.ans


solution = Solution()
print(solution.combinationSum3(3,7))

print(solution.combinationSum3(3,9))