
class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(4)
a5 = TreeNode(5)

a1.left = a2
a1.right = a3
a3.left = a4
a3.right = a5

root = a1





def serialize(root):
    """Encodes a tree to a single string.
    :type root: TreeNode
    :rtype: str
    """
    serialized = []
    queue = [[root]]
    while queue:
        level = queue.pop(0)
        nextlevel = []
        while level:
            cur = level.pop(0)
            serialized.append(cur)
            if cur!=None: 
                nextlevel.append(cur.left) 
                nextlevel.append(cur.right) 
        
        if nextlevel:
            queue.append(nextlevel)
    
    while serialized[-1] == None:
        serialized.pop()
    
    [print(node.val,',', end=' ') if node else None for node in serialized]
    return serialized

    
def deserialize(data):
    """Decodes your encoded data to tree.
    :type data: str
    :rtype: TreeNode
    """
    serialized = data
    root = serialized[0]
    queue = [[root]]
    i = 1
    while queue:
        level = queue.pop(0)
        nextlevel = []
        while level:
            cur = level.pop(0)
            if i < len(serialized):
                cur.left = serialized[i]
                if cur.left!=None: nextlevel.append(cur.left) 
                i+=1
            if i < len(serialized):
                cur.right=serialized[i]
                if cur.right!=None: nextlevel.append(cur.right) 
                i += 1
            
        if nextlevel:
            queue.append(nextlevel)
    
    return root

print('Given root: ',a1.val)
serialized = serialize(root)
print('\n\nserialized list from root: ', serialized)
x = deserialize(serialized)
print('\n\ndeseralized into root: ', x.val)
serialized = serialize(x)
print('\n\nserialized list from root_from_above_deserialization: ',serialized)