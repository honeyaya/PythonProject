class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """

        ans = ""
        for add in address:
            if add == '.':
                ans += "[.]"
            else:
                ans += add

        return ans


solution = Solution()
print(solution.defangIPaddr("1.1.1.1"))
print(solution.defangIPaddr("255.100.50.0"))