"""TC:O(m*m),SC:O(m*m)"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        r = [[1]]
        for i in range(numRows-1):
          temp = [0]+r[-1]+[0]
          row = []
          k=len(r[-1])+1
          for j in range(k):
            row.append(temp[j]+temp[j+1])
          r.append(row)
        return r
          

          
      
if __name__== "__main__":
    numRows = 5
    a=Solution()
    ans=a.generate(numRows)
    print(ans)         