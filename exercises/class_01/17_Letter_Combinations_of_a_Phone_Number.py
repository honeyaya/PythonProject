# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution(object):
    ans = []

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        mapper = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(pos, res):
            if pos == len(digits):
                #print("res: {}".format(res))
                self.ans.append(res)
                return
            for c in mapper[digits[pos]]:
                res = res + c
                dfs(pos + 1, res)
                res = res[:-1]


        self.ans = []
        dfs(0, "")
        return self.ans


solution = Solution()
print(solution.letterCombinations("23"))
print(solution.letterCombinations(""))
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].