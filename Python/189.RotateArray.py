class Solution(object):
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        l = 0
        r = len(nums) - 1
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        l=0
        r = k-1
        while l <=( r ):
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        r=len(nums)-1
        while k<=r:
            nums[k], nums[r] = nums[r], nums[k]
            k += 1
            r -= 1
        return nums


if __name__=="__main__":
    #nums = [1,2,3,4,5,6,7]
    nums = [-1]
    k = 2
    a=Solution()
    i=a.rotate(nums,k)
    print(i)