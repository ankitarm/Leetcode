"""TC:O(logn) SC:O(1)"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        low = 0
        high = len(nums)-1


        while low<=high:
            mid = (low + high) // 2
            if target>nums[mid]:
                low=mid+1
            elif target<nums[mid]:
                high=mid-1
            else:
                return mid
        return -1



if __name__=="__main__":
    nums = [-1,0,3,5,9,12]
    target = 0
    a=Solution()
    k=a.search(nums,target)
    print(k)