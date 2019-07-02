# https://leetcode.com/problems/restore-ip-addresses/
# prefix has 0

class Solution(object):
    ans = []
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def dfs(pos, res):
            if pos == len(s):
                if len(res) == 4:
                    ip = ".".join(res)
                    self.ans.append(ip)
                return

            for idx in range(1,4):
                tmpstr = s[pos: pos + idx]
                if len(tmpstr) == 1 or (len(tmpstr) > 1 and tmpstr[0] != '0'):
                    num = int(tmpstr)
                    if num >= 0 and num <= 255:
                        if len(res) < 4:
                            res.append(tmpstr)
                            dfs(pos + idx, res)
                            res.pop()

        self.ans = []
        dfs(0,[])
        return self.ans

solution = Solution()
print(solution.restoreIpAddresses("25525511135"))
print(solution.restoreIpAddresses("0000"))
print(solution.restoreIpAddresses("010010"))
