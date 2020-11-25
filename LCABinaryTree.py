

def LowestCommonAncestorBST(root, p,q):
    if p.val < root.val and q.val < root.val:
        return LowestCommonAncestorBST(root.left,p,q)
    elif p.val > root.val and q.val > root.val:
        return LowestCommonAncestorBST(root.right,p,q)
    else:
        return root


# node = root
def LowestCommonAncestorBT(node, p,q):
    if node == None:
        return None
    
    if node.val==p.val | node.val==q.val: #searching for p/q
        return node
 
    #inorder traversal of tree to find node
    left = LowestCommonAncestorBT(node.left,p,q)
    right = LowestCommonAncestorBT(node.right,p,q)

    #if both are non-null then return the node itself
    if left!=None and right!=None:
        return node
    else:   #one is null and other is not-null, return the not-null node
        if left: return left
        if right: return right

