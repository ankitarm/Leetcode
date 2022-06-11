"""TC:O(n),SC:O(n)"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy=ListNode()
        curr=dummy
        carry=0
        while l1 or l2 or carry:
          v1=l1.val if l1 else 0
          v2=l2.val if l2 else 0
          value=v1+v2+carry
          carry=value//10
          value=value%10
          curr.next=ListNode(value)
          curr=curr.next
          l1=l1.next if l1 else None
          l2=l2.next if l2 else None
        return dummy.next
          
          
          

                
if __name__== "__main__":
    l1 = [2,4,3] 
    l2 = [5,6,4]
    a=Solution()
    ans=a.addTwoNumbers(l1,l2)
    print(ans)         