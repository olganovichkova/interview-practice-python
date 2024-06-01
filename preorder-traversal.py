def preOrderTraversal(root):
    output = []
        
    if root is None:
        return output 
        
        
    stack = [root]
        
        
    while stack:
        node = stack.pop()
        output.append(node.val)
            
        if node.right:
            stack.append(node.right)
                
        if node.left:
            stack.append(node.left)
            
    return output