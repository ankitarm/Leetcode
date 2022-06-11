# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy=ListNode(0,head)
        left=dummy
        right=head
        while n>0 and right:
            right=right.next
            n-=1
        while left and right:
            left=left.next
            right=right.next
        left.next=left.next.next
        return dummy.next

if __name__== "__main__":
    head = [1,2,3,4,5] 
    n = 2
    a=Solution()
    ans=a.removeNthFromEnd(head,n)
    print(ans)  