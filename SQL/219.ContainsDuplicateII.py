
class Solution:
    def containsNearbyDuplicate(self, nums: [int], k: int) -> bool:
        indices_dic = {}
        for index, value in enumerate(nums):
            if value in indices_dic and index - indices_dic[value] <=k:
                return True
            indices_dic[value] = index


if __name__=="__main__":
    nums = [1,2,3,1]
    a=Solution()
    k=a.containsNearbyDuplicate(nums,3)
    print(k)