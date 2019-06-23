# https://leetcode.com/problems/subsets/

class Solution(object):
    # 16ms
    ans = []

    def findsubsets(self, res, pos, nums):
        self.ans.append(list(res))
        for idx in range(pos, len(nums)):
            res.append(nums[idx])
            self.findsubsets(res, idx + 1, nums)
            res.remove(nums[idx])

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        16ms
        """
        self.ans = []
        res = []
        self.findsubsets(res, 0, nums)
        return self.ans

solution = Solution()
print(solution.subsets([1,2,3]))
print(solution.subsets([1,2,3,4]))


