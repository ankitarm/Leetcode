class Solution(object):
    def longestsubarray(self, nums):
        zero_count = left = max_count =0
        for right in range(len(nums)):
                if nums[right] == 0 :
                    zero_count+=1
                while zero_count > 1:
                    if nums[left] == 0:
                        zero_count-=1
                    left += 1
                max_count = max(max_count,right - left)
        return max_count if zero_count > 0 else max_count
if __name__ == "__main__":
    #nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
    nums = [1,1,1]
    a = Solution()
    k = a.longestsubarray(nums)
    print(k)