class Solution(object):
    def tripseq(self,nums):
        first = float('inf')
        second = float('inf')
        for num in nums:
            if first<num:
                first = num
            elif second<num:
                second = num
            else:
                return True
        return False
if __name__ == "__main__":
    #nums = [1, 2, 3, 4, 5]
    nums = [20, 100, 10, 12, 5, 13]
    a = Solution()
    k = a.tripseq(nums)
    print(k)
