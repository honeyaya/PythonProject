class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        def addX(diffx):
            res = ""
            if diffx > 0:
                res = res + diffx * "D"
            else:
                res = res + abs(diffx) * "U"
            return res

        def addY(diffy):
            res = ""
            if diffy > 0:
                res = res + diffy * "R"
            else:
                res = res + abs(diffy) * "L"
            return res

        def help(originX, originY, nowX, nowY):
            res = ""
            diffx = nowX - originX
            diffy = nowY - originY
            if originX == 5:
                res += addX(diffx)
                res += addY(diffy)
            else:
                res += addY(diffy)
                res += addX(diffx)
            return res

        path = ""
        originX = 0
        originY = 0
        for t in target:
            tmp = ord(t) - ord('a')
            row = int(tmp/5)
            col = int(tmp%5)
            path += help(originX, originY, row, col)
            path += "!"
            originX = row
            originY = col

        return path


solution = Solution()
print(solution.alphabetBoardPath("w"))
print(solution.alphabetBoardPath("leet"))
# "DDR!UURRR!!DDD!"
print(solution.alphabetBoardPath("code"))
# "RR!DDRR!UUL!R!"
print(solution.alphabetBoardPath("afjzu"))
print(solution.alphabetBoardPath("zdz"))
# "DDDDD!UUUUURRR!DDDDLLLD!"
print(solution.alphabetBoardPath("zd"))
