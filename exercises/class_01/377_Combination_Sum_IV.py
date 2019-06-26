# https://leetcode.com/problems/combination-sum-iv/

# dfs will timeout

class Solution(object):

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        dp = [0 for idx in range(target + 1)]
        dp[0] = 1
        for idx in range(1, target + 1):
            for num in nums:
                if num <= idx:
                    dp[idx] += dp[idx - num]

        return dp[target]

solution = Solution()
print(solution.combinationSum4([1,2,3], 4))
print(solution.combinationSum4([1,2], 10))
