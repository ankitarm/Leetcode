"""TC:O(n),SC:O(n)"""
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        stack = []
        for i in s:
          stack.append(i)
        k=0
        while stack:
          s[k]=stack.pop()
          k+=1
        return s
      
        
      
if __name__== "__main__":
    s = ["h","e","l","l","o"]
    a=Solution()
    ans=a.reverseString(s)
    print(ans)         