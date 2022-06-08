"""TC:O(n+m),SC:O(m or n)"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict_nary = {}
        result = []
        for num in nums1:
            if num in dict_nary:
                dict_nary[num]=dict_nary[num]+1
            else:
                dict_nary[num]=1
        for num in nums2:
            if num in dict_nary and dict_nary[num]>0:
                result.append(num)
                dict_nary[num]-=1
        return result
      
if __name__== "__main__":
    nums1=[4,9,5]
    nums2=[9,4,9,4,8]
    a=Solution()
    ans=a.intersect(nums1,nums2)
    print(ans)              
                
                
                
        