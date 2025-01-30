from collections import defaultdict

class Solution(object):
    def maxnum(self,nums,k ):
        dict = defaultdict(int)
        count = 0
        # track the freq of complement.
        for i in nums:
            if dict[i]>0:
                count+=1
                dict[i]-=1
            else:
                dict[k-i]+=1
        return count

if __name__ == "__main__":
    #nums = [1, 2, 3, 4]
    nums = [2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2]

    k = 3
    a = Solution()
    k = a.maxnum(nums,k)
    print(k)