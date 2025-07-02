# binary search tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None



def binary_tree_search(tree, item_to_search):
    if tree is None or tree.key == item_to_search:
        return tree
    
    if tree.key < item_to_search:
        return binary_tree_search(tree.right, item_to_search)
    
    return binary_tree_search(tree.left, item_to_search)



root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)



print("Found" if binary_tree_search(root, 60) else "Not Found")