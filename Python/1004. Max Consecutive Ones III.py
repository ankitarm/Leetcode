class Solution(object):
    def longestOnes(self,nums, k):
        left = 0
        max_count = 0
        zero_count = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count +=1
            while zero_count>k:
                if nums[left] == 0:
                    zero_count-=1
                left+=1
            max_count = max(max_count,right-left+1)
        return max_count
if __name__ == '__main__' :

    #nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3
    a = Solution()
    i = a.longestOnes(nums, k)
    print(i)