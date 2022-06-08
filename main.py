"""TC:O(n),SC:O(n)"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s.split()
        k=[]
        for word in words:
          k.append((reversed(word)))
          k.append(" ")
        
        return "".join(k).strip()
            

                
if __name__== "__main__":
    s = "Let's take LeetCode contest"
    a=Solution()
    ans=a.reverseWords(s)
    print(ans)         