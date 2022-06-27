class Solution(object):
    def isValid(self, s):
        stack = []
        paranthdict={")":"(","}":"{","]":"["}
        for prth in s:
          if prth in paranthdict:
            if stack and stack[-1]==paranthdict[prth]:
              stack.pop()
            else:
              return False
          else:
            stack.append(prth)
        return True if not stack else False

if __name__ == "__main__":
    s = "{{}))"
    #s="()"
    a=Solution()
    i=a.isValid(s)
    print(i)