"""TC:O(logn)"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) -1  #3
        while low<=high :
            mid = (low+high)//2  #1
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high = mid - 1
            else:
                low = mid + 1
        return low





if __name__=="__main__":
    nums = [1,3,5,6]
    target = 7
    a=Solution()
    k=a.searchInsert(nums,target)
    print(k)