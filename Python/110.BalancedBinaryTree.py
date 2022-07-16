class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
       
class Solution(object):
    def isBalanced(self, root):
      def helper(node):
        if not node:
          return (0,True)
        l_height,l_balance=helper(node.left)
        r_height,r_balance=helper(node.right)

        return (max(l_height,r_height)+1,l_balance and r_balance and abs(l_balance-r_balance))
      return helper(root)[-1]
        
      

if __name__ == "__main__":
    root = [3,9,20,null,null,15,7]
    a=Solution()
    i=a.isBalanced(root)
    print(i)