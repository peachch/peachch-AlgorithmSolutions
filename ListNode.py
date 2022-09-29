

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    def node(self,List):
        # head在这里设置为头之后，就不要动了，之后用p去代替head移动和赋值
        head = ListNode(List[0])
        p = head

        for i in List[1:]:
            p.next = ListNode(i)
            p = p.next
        return head


# ss = ListNode().node([1, 2, 3])
# print(ss.val)
# print(type(ss))
