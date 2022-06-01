class Solution(object):
    def sortedSquares(self, nums):
        p1 = 0
        p2 = len(nums) - 1
        result = []
        while p1 <= p2:
            if nums[p1] * nums[p1] > nums[p2] * nums[p2]:
                result.append(nums[p1]*nums[p1])
                p1+=1
            else:
                result.append(nums[p2]*nums[p2])
                p2-=1
        return result[::-1]

if __name__=="__main__":
    nums = [-4,-1,0,3,10]
    a=Solution()
    k=a.sortedSquares(nums)
    print(k)

