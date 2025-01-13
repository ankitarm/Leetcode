
'''class Solution(object):
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
        return maxsub'''


class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        cur_sum = 0
        max_sum = float('-inf')
        for num in nums[:]:
            cur_sum +=num
            max_sum = max(cur_sum, max_sum)
            if cur_sum<0:
                 cur_sum=0
        return max_sum


if __name__ == "__main__":
    nums1 = [-2,1,-3,4,-1,2,1,-5,4]
    nums2 =[0]
    nums3 = [5,4,-1,7,8]
    a=Solution()
    i=a.maxSubArray(nums1)
    print(i)



