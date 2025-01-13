class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0  # 0
        high = len(nums) - 1  # 3
        while low <= high:  # 0<=1
            mid = (low + high) // 2  # 0
            if target == nums[mid] :  # 2==1
                return mid
            elif target > nums[mid] :  # 2>1
                low = mid+1
            else:  # 2<1
                high = mid-1  # high=1
        return low


if __name__=="__main__":
    nums=[1,3,5,6]
    target=2
    a=Solution()
    k=a.searchInsert(nums,target)
    print(k)