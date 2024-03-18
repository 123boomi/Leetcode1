class Solution(object):
    def middleNode(self,head):
            tmp=head
            while tmp and tmp.next:
                head=head.next
                tmp=tmp.next.next
            return head
