# https://leetcode.com/problems/combination-sum-ii/

class Solution(object):
    ans = []

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(pos, res, tmpsum, number):
            if pos + 1 < len(candidates) and candidates[pos] == candidates[pos + 1]:
                dfs(pos + 1, res, tmpsum, number + 1)
                return

            if tmpsum == target:
                self.ans.append(list(res))
                return

            if tmpsum > target:
                return

            if pos == len(candidates):
                return

            for idx in range(0,number + 1):
                if idx == 0:
                    dfs(pos + 1, res, tmpsum, 1)
                else:
                    for tmp in range(idx):
                        res.append(candidates[pos])
                    dfs(pos + 1, res, tmpsum + candidates[pos] * idx, 1)
                    for tmp in range(idx):
                        res.remove(candidates[pos])

        candidates.sort()
        self.ans = []
        dfs(0, [], 0, 1)
        return self.ans

solution = Solution()
print(solution.combinationSum2([10,1,2,7,6,1,5], 8))

print(solution.combinationSum2([2,5,2,1,2], 5))

print(solution.combinationSum2([1,1,2], 4))