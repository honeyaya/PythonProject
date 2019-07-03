# https://leetcode.com/problems/search-a-2d-matrix/

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        row = len(matrix)
        if row == 0:
            return False
        col = len(matrix[0])
        if col == 0:
            return False

        if target < matrix[0][0] or matrix[row - 1][col - 1] < target:
            return False

        r_left = 0
        r_right = row - 1

        while r_left <= r_right:
            r_mid = r_left + int((r_right - r_left)/2)
            if matrix[r_mid][0] <= target and target <= matrix[r_mid][col - 1]:
                #print("r_mid: {}".format(r_mid))
                c_left = 0
                c_right = col - 1
                while c_left <= c_right:
                    c_mid = c_left + int((c_right - c_left)/2)
                    if matrix[r_mid][c_mid] == target:
                        return True
                    elif matrix[r_mid][c_mid] > target:
                        c_right = c_mid - 1
                    elif matrix[r_mid][c_mid] < target:
                        c_left = c_mid + 1
                return False
            elif target < matrix[r_mid][0]:
                r_right = r_mid - 1
            elif target > matrix[r_mid][col - 1]:
                r_left = r_mid + 1


solution = Solution()
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],3))
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],13))
print(solution.searchMatrix([],0))
print(solution.searchMatrix([[]],1))