from ListNode import ListNode

def rotateRight(head:ListNode, k) -> ListNode:
    # def slide(head):


    p = head
    count = 1
    while p.next:
        p = p.next
        count += 1
    p.next = head
    print(count)
    des = count - k % count

    q = head
    while des !=1:
        q = q.next
        des -= 1
    newHead = q.next
    q.next = None
    return newHead



head = [1, 2, 3, 4, 5]
k = 7
temp = ListNode().node(head)
ss = rotateRight(temp, k)
print("sss",ss.val)