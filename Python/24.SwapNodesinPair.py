# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0,head)
        prev,curr=dummy,head
        while curr and curr.next:
            second=curr.next
            nxtPair=curr.next.next
            second.next=curr
            curr.next=nxtPair
            prev.next=second
            prev=curr
            curr=nxtPair
        return dummy.next


if __name__== "__main__":
    head = [1,2,3,4] 
    a=Solution()
    ans=a.swapPairs(head)
    print(ans)  