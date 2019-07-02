# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + int((right - left)/2)
            #print("left:{} right:{} mid: {}".format(left, right, mid))
            if nums[mid] == target:
                return mid
            elif nums[mid] <= nums[right]:
                if nums[mid] <= target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

solution = Solution()


print(solution.search([4,5,6,7,0,1,2], 0))
print(solution.search([4,5,6,7,0,1,2], 3))
print(solution.search([4,5,6,7,0,1,2], 9))
print(solution.search([4,5,6,7,0,1,2], 7))
print(solution.search([4,5,6,7,0,1,2], 4))
print(solution.search([3,1],3))
print(solution.search([5,1,3],5))
print(solution.search([4,5,6,7,0,1,2], 2))
print(solution.search([1, 3],2))
