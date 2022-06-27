class Solution(object):
    def lengthOfLastWord(self, s):
      i=len(s)-1  
      llw=0
      while(s[i]):
        a=s[i]
        if a==" " and llw==0:
          i-=1
        elif s[i]!=" " and i>=0:
          llw+=1
          i-=1
        else:
          return llw
      
        
      



if __name__ == "__main__":
    s = "a"
    k="hello world"
    a=Solution()
    i=a.lengthOfLastWord(s)
    print(i)