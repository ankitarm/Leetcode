
#using inbuilt gcd
from math import gcd


class Solution(object):
  def gcd(self, str1, str2):
    if str1+str2 != str2+str1:
      return ""
    gcdlen = gcd(len(str1), len(str2))
    return str1[: gcdlen]

  """euclidean algo to find gcd
      def gcd(a,b):
          while b!=0:
              a=b
              b=a%b
          return a

          """


""""
class Solution(object):
  def gcd(self, str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    for i in range(min(len1,len2), 0, -1):
      if len1%i ==0 and len2%i==0:
        n1, n2 = len1//i, len2//i
        base = str1[:i]
        if str1 == n1*base and str2 == n2*base:
          return base

    return ""

"""



if __name__ == "__main__":
  str1 = "ABABAB"
  str2 = "ABAB"
  a=Solution()
  k = a.gcd(str1, str2)
  print (k)