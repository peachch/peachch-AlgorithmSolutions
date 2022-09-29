from ListNode import ListNode

def deleteDuplicates(head:ListNode) -> ListNode:

    if not head or not head.next:
        return head
    if head.val != head.next.val:
        print(head.val)
        head.next = deleteDuplicates(head.next)
    else:
        cur = head.next
        while cur and head.val == cur.val:
            cur = cur.next
            print(cur.val)
        return deleteDuplicates(cur)

    return head

head = [1, 2, 3, 3, 4, 4, 5]
temp = ListNode().node(head)
ss = deleteDuplicates(temp)
print("sss",ss.next.next.val)