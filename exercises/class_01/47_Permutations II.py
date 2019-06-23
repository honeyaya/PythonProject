# https://leetcode.com/problems/permutations-ii/

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        36ms
        with duplicate number situation, can reconsider
        """
        def dfs(nums):
            if len(nums) == 0:
                return [nums]

            ans = []
            for idx in range(len(nums)):
                if idx == 0 or nums[idx] != nums[idx - 1]:
                    res = dfs(nums[0:idx] + nums[idx + 1:])
                    for r in res:
                        ans.append([nums[idx]] + r)
            return ans

        nums.sort()
        return dfs(nums)

solution = Solution()
print(solution.permuteUnique([2,1,1]))