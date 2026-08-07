class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def removeLeadingZeros(self, head):
        while head and head.data == 0 and head.next:
            head = head.next
        return head

    def addTwoLists(self, head1, head2):
        head1 = self.removeLeadingZeros(head1)
        head2 = self.removeLeadingZeros(head2)

        head1 = self.reverse(head1)
        head2 = self.reverse(head2)

        carry = 0
        dummy = Node(0)
        curr = dummy

        while head1 or head2 or carry:
            s = carry

            if head1:
                s += head1.data
                head1 = head1.next

            if head2:
                s += head2.data
                head2 = head2.next

            carry = s // 10
            curr.next = Node(s % 10)
            curr = curr.next

        ans = self.reverse(dummy.next)
        return self.removeLeadingZeros(ans)