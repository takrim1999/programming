# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

a = [1,2,4]
b = [1,3,4]
new_list = None

for i in a:
    if new_list == None:
        new_list = ListNode(i)
    else:
        new_list.next = ListNode(i)

