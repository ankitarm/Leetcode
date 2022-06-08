"""TC:O(n*m),SC:O(m or n)"""

class Solution(object):
    def matrixReshape(self, mat, r, c):
            arr=[]
            m=len(mat)
            n=len(mat[0])
            if r*c != m*n:
                return mat
            else:
                for i in mat:
                  for j in i:
                     arr.append(j)
                k=0
                col=[]
                row=[]
                for i in range(r):
                    for  j in range(c):
                      #output=[[0 for i in range(c)]for i in range(r)]
                      #output[i][j]=arr[k]
                        col.append(arr[k])
                        k=k+1
                    row.append(col)
                    col=[]
                return row           
 
if __name__== "__main__":
    mat = [[1,2],[3,4]]
    r = 1
    c = 4
    a=Solution()
    ans=a.matrixReshape(mat,r,c)
    print(ans)              
                
                
                
        