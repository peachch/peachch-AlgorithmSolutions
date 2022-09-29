class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list2link(List):
    head = ListNode(List[0])
    p = head
    for i in range(1, len(List)):
        p.next = ListNode(List[i])
        p = p.next
    return head


class Solution:
    def swap_pairs(self, head: ListNode) -> ListNode:
        # 这里要注意先not head再not head.next，注意一下这个顺序
        if not head or not head.next:
            return head
        newHead = head.next
        print(type(newHead))
        head.next = self.swap_pairs(newHead.next)
        newHead.next = head
        return newHead


l2l = list2link([1, 2, 3, 4])
S = Solution()
result = S.swap_pairs(l2l)
print(result.val)
print(result.next.val)
