# https://leetcode.com/problems/implement-strstr/
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        24ms
        """
        if len(needle) == 0:
            return 0

        for idh in range(len(haystack) - len(needle) + 1):
            for idn in range(len(needle)):
                if haystack[idh + idn] != needle[idn]:
                    break
            if haystack[idh + idn] == needle[idn] and idn == len(needle) - 1:
                return idh

        return -1

    def strStr2(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        4ms
        """
        if len(needle) == 0:
            return 0

        for idh in range(len(haystack) - len(needle) + 1):
            if haystack[idh : idh + len(needle)] == needle:
                return idh

        return -1

    def strStr3(self, haystack, needle):
        # 20ms
        if len(needle) == 0:
            return 0

        if needle not in haystack:
            return -1
        return len(haystack.split(needle)[0])

solution = Solution()
print(solution.strStr2("hello", "ell"))
print(solution.strStr2("aaaaa", "bba"))
print(solution.strStr2("mississippi", "a"))
print(solution.strStr2("mississippi", "mi"))

