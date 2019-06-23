# https://leetcode.com/problems/subsets-ii/

class Solution(object):

    ans = []

    def helper(self, pos, nums, res):
        self.ans.append(list(res))

        for idx in range(pos, len(nums)):
            if idx != pos and nums[idx] == nums[idx - 1]:
                continue
            res.append(nums[idx])
            self.helper(idx + 1, nums, res)
            res.remove(nums[idx])


    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        24ms
        """
        nums.sort()
        self.ans = []
        res = []
        self.helper(0, nums, res)
        return self.ans

class Solution2(object):
    def subsetsWithDup(self, nums):
        nums.sort()

        ans = []
        def dfs(pos, l):
            ans.append(list(l))

            for idx in range(pos, len(nums)):
                if idx != pos and nums[idx - 1] == nums[idx]:
                    continue
                l.append(nums[idx])
                dfs(idx + 1, l)
                l.remove(nums[idx])

        dfs(0, [])

        return ans



solution = Solution()
print(solution.subsetsWithDup([1]))
print(solution.subsetsWithDup([1,2,2]))
print(solution.subsetsWithDup([5,5,5,5,5]))
print(solution.subsetsWithDup([4,4,4,1,4]))

solution2 = Solution2()
print(solution2.subsetsWithDup([1]))
print(solution2.subsetsWithDup([1,2,2]))
print(solution2.subsetsWithDup([5,5,5,5,5]))
print(solution2.subsetsWithDup([4,4,4,1,4]))


# [[], [1], [1, 2], [1, 2, 2], [1, 2], [2], [2, 2], [2]]
# [[], [1], [1, 2], [1, 2, 2], [2], [2, 2], [2]]
# [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

# [4,4,4,1,4]
# [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
# [[], [4], [4, 4], [4, 4, 4], [4, 4, 4, 1], [4, 4, 4, 1, 4], [4, 4, 4, 4], [4, 4, 1], [4, 4, 1, 4], [4, 4, 4], [4, 1], [4, 1, 4], [4, 4], [1], [1, 4], [4]]
