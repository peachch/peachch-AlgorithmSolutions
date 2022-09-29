from ListNode import ListNode

def reverseKGroup(head:ListNode, k) -> ListNode:

    def reverse(head, b):
        cur = head
        pre = None
        while cur != b:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre



    a = b = head
    count = 0
    while count < k:
        # if b == None or b.next == None:
        """ 这里注意下返回条件，不应该加b.next == None"""
        if b == None:
            return head
        b = b.next
        count += 1
    newHead = reverse(a, b)
    print(id(newHead))
    a.next = reverseKGroup(b,k)
    print(id(a))
    print((id(b)))
    return newHead






head = [1,2,3,4,5]
k = 2
temp = ListNode().node(head)
ss = reverseKGroup(temp, k)
print("sss",ss.next.next.next.val)