class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        for index, value in enumerate(nums):
            if value == 0:
                nums.pop(index)
                nums.append(value)
        print(nums)

if __name__=="__main__":
    nums=[0, 0, 1, 0, 1, 1, 1]
    print(nums)
    a=Solution()
    k=a.moveZeroes(nums)
