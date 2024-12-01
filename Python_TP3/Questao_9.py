class Node:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None  

def in_order_traversal(root):
    if root is None:
        return []

    return in_order_traversal(root.left) + [root.value] + in_order_traversal(root.right)

#Construindo a árvore binária
root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(1)
root.left.right = Node(4)
root.right.left = Node(7)
root.right.right = Node(9)


result = in_order_traversal(root)
print(result)