
class Solution(object):
    def removeDupElement(self, nums):
        pointer = 1 #kahase change karn he
        for index in range(len(nums)):
            if nums[index] != nums[pointer-1]:
                nums[pointer] = nums[index]
                pointer+=1
        return pointer



if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    a = Solution()
    i=a.removeDupElement(nums)
    print(i)