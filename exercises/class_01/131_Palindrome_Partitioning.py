# https://leetcode.com/problems/palindrome-partitioning/

class Solution(object):
    ans  = []
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def palindrome(tmpstr):
            reversestr = tmpstr[::-1]
            return reversestr == tmpstr

        def dfs(pos, res):
            if pos == len(s):
                self.ans.append(list(res))
                return

            for idx in range(pos + 1, len(s) + 1):
                tmpstr = s[pos:idx]
                if palindrome(tmpstr) == True:
                    res.append(tmpstr)
                    dfs(idx, res)
                    res.pop()

        if len(s) < 2:
            self.ans.append(list(s))
            return self.ans

        self.ans = []
        dfs(0, [])
        return self.ans

solution = Solution()
print(solution.partition("a"))
print(solution.partition("abc"))
print(solution.partition("aab"))
print(solution.partition("aaa"))
print(solution.partition("aabb"))
print(solution.partition("cbbbcc"))