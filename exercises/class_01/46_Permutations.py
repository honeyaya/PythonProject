# https://leetcode.com/problems/permutations/

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        # 20ms
        """

        def helper(pos):
            if pos == 0:
                return [[nums[pos]]]

            ans = []
            res = helper(pos - 1)
            for r in res:
                for idr in range(len(r)):
                    tmp = []
                    tmp = tmp + r[0:idr]
                    tmp.append(nums[pos])
                    tmp = tmp + r[idr:len(r)]
                    ans.append(list(tmp))

                r.append(nums[pos])
                ans.append(r)
            return ans

        return helper(len(nums) - 1)

solution = Solution()
print(solution.permute([1,2,3]))