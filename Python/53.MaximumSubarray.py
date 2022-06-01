
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Cursum = 0
        maxsub = nums[0]
        for element in nums:
            if Cursum<0:
                Cursum=0
            Cursum = Cursum + element
            maxsub = max(maxsub,Cursum)
        return maxsub
if __name__ == "__main__":
    nums1 = [-2,1,-3,4,-1,2,1,-5,4]
    nums2 =[0]
    nums3 = [5,4,-1,7,8]
    a=Solution()
    i=a.maxSubArray(nums1)
    print(i)



