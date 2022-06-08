"""TC:O(n*m),SC:O(m or n)"""

class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        result = [[0 for _ in range(c)]for _ in range(r)]
        if (r*c)!=(len(mat)*len(mat[0])):
          return mat
        else:
          for i in range(r*c):
            result[i//c][i%c]=mat[i//len(mat[0])][i%len(mat[0])]
          return result
            
 
if __name__== "__main__":
    mat = [[1,2],[3,4]]
    r = 1
    c = 4
    a=Solution()
    ans=a.matrixReshape(mat,r,c)
    print(ans)              
                
                
                
        