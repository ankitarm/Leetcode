class Solution(object):
    def movezeros(self, nums):
            nonzeropointer = 0
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[nonzeropointer]=nums[i]
                    nonzeropointer+=1
            for i in range(nonzeropointer, len(nums)):
                nums[i]=0
            return nums

            #fill the first hall of list with nums rest with zero, using pointer to track



if __name__ == "__main__":
    #nums = [0, 1, 0, 3, 12]
    nums = [0, 0, 1]
    a = Solution()
    k = a.movezeros(nums)
    print (k)