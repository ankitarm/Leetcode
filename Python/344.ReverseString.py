"""TC:O(n),SC:O(1)"""
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l,r=0,len(s)-1
        while l<r:
          s[l],s[r]=s[r],s[l]
          l+=1
          r-=1
        return s
      
        
      
if __name__== "__main__":
    s = ["h","e","l","l","o"]
    a=Solution()
    ans=a.reverseString(s)
    print(ans)         