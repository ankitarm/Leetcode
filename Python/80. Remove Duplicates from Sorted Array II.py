
class Solution(object):
    def removeDups(self, nums):
        pointer = 2
        for index in range(len(nums)):
            if nums[index] != nums[pointer - 2]:
                nums[pointer] = nums[index]
                pointer +=1
        return pointer, nums



if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    a = Solution()
    k = a.removeDups(nums)
    print(k)


