
class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None
        self.prev = None


a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(4)
a5 = TreeNode(5)
a6 = TreeNode(6)
a7 = TreeNode(7)

a1.left = a2
a1.right = a3
a2.left = a4
a2.right = a5
a3.left = a6
a3.right = a7

#def convertBinTreetoDoublyLL(root):

head = a1   
prev = None

queue = [[a1]]

while queue:
    level = queue.pop(0)
    nextlevel = []
    while level:
        current = level.pop(0)
        if current.left:
            nextlevel.append(current.left)
        if current.right:
            nextlevel.append(current.right)
        if level:
            current.next = level[0]
        else:
            if nextlevel:
                current.next = nextlevel[0]
            else:
                current.next = None

        current.prev = prev
        prev = current
    if nextlevel:
        queue.append(nextlevel)

while head:
    if not head.prev or not head.next:
        print('None')
    else:
        print(head.prev.val,' <-',head.val,'->', head.next.val)
    head = head.next
 