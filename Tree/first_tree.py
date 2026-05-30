class TreeNode():
    def __init__(self, val) -> None:
        self.left_ = None
        self.right_ = None
        self.val_ = val
def pushTree(root_node ,val):
    
    if root_node.val_ >= val:
        if root_node.left_ is None:
            new_node = TreeNode(val)
            root_node.left_ = new_node
        else:
            pushTree(root_node.left_ , val)
    else:
        if root_node.right_ is None:
            new_node = TreeNode(val)
            root_node.right_ = new_node
        else:
            pushTree(root_node.right_ , val)

root_node = TreeNode(5)

nodes = [7, 3, 9, 1, 5, 8, 10, 0, 2, 4] 

for node in nodes:
    pushTree(root_node, node)

print(root_node.left_.right_.left_.val_)
