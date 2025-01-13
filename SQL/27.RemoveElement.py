class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while nums.count(val):
            nums.remove(val)
        return len(nums)

        """i=0
        count=0
        while i<len(nums): #2
            if val==nums[i]:
                nums.pop(i)
            else:
                i+=1
        return len(nums)"""




if __name__ == "__main__":
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    a = Solution()
    i=a.removeElement(nums,val)
    print(i)