class Solution:
    def pivotIndex(self, nums) -> int:
        sumleft = 0
        sumright = sum(nums)
        for index, element in enumerate(nums):
            sumright-=element
            if sumleft == sumright:
                return index
            sumleft += element
        return -1


if __name__ == '__main__':
    nums = [1,7,3,6,5,6]
    a = Solution()
    k = a.pivotIndex(nums)
    print(k)