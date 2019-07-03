# https://leetcode.com/problems/search-insert-position/

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right :
            mid = left + int((right - left)/2)
            if (nums[mid] == target):
                return mid
            elif nums[mid] > target:
                if mid == 0 or mid == len(nums) - 1:
                    return mid
                else:
                    right = mid - 1
            elif nums[mid] < target:
                if mid <= len(nums) - 2 and nums[mid + 1] > target:
                    return mid + 1
                elif mid == len(nums) - 1:
                    return mid + 1
                else:
                    left = mid + 1

        return -1


solution = Solution()
print(solution.searchInsert([1,3,5,6],5))
print(solution.searchInsert([1,3,5,6],2))
print(solution.searchInsert([1,3,5,6],7))
print(solution.searchInsert([1,3,5,6],0))
print(solution.searchInsert([1],2))
print(solution.searchInsert([2],1))
print(solution.searchInsert([1,3],4))
print(solution.searchInsert([5,6],4))
