def postorderTraversal(root):
        #stack implementation
        result = []
        if root is None:
            return result
        
        stack = [root]
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
            
        return result[::-1]

            
        # recursive implementation
        # def postorderTraversal(root):
#         result = []
#         return self.postorder(root, result)
        
#     def postorder(self, node, result):
#         if node is None:
#             return result
        
#         left = self.postorder(node.left, result)
#         right = self.postorder(node.right, result)
        
#         result = left + right + [node.val]
#         return result
        