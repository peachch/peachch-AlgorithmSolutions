from ListNode import ListNode

def reversBetween(head:ListNode, left, right) -> ListNode:

    def reverse(head, n):

        if n == 1:
            # 关于私有变量和全局变量需要巩固一下
            global succ
            succ = head.next

            return head
        # 这里从head的下一位开始，所以当前的head不变，当退出循环之后，这里的head依然是他自己
        last = reverse(head.next, n-1)
        # 一直想不通的就是这里，不要陷入递归中，假设递归要实现的反转已经实现，此时就是最后的拼接，因为递归本来就是子问题，所以同样的 这里的子问题写对就可以完成递归
        # 将此时的head 变成尾巴
        head.next.next = head
        head.next = succ
        return last

    if left == 1:
        last = reverse(head,right)
        return last
    head.next = reversBetween(head.next, left-1, right-1)
    return head



head = [1,2,3,4,5]
left = 2
right = 4
temp = ListNode().node(head)
ss = reversBetween(temp, left, right)
print("sss",ss.next.next.next.next.val)


























head = [1,2,3,4,5]
left = 2
right = 4