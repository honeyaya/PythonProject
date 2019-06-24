# https://leetcode.com/problems/combination-sum/

class Solution(object):
    ans = []
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(pos, res, tmpsum):
            #print("tmpsum: {}".format(tmpsum))
            if tmpsum == target:
                self.ans.append(list(res))
                return
            if tmpsum > target:
                return
            if pos == len(candidates):
                return
            #for idx in range(pos, len(candidates)):
            number = int((target - tmpsum) / candidates[pos])
            #print("number: {}".format(number))
            for layer in range(0, number + 1):
                for idl in range(layer):
                    res.append(candidates[pos])
                dfs(pos + 1, res, tmpsum + candidates[pos] * layer)

                for idl in range(layer):
                    res.remove(candidates[pos])
        self.ans = []
        dfs(0, [], 0)
        return self.ans


solution = Solution()
print(solution.combinationSum([2,3,6,7], 7))
print(solution.combinationSum([5,3,2], 8))