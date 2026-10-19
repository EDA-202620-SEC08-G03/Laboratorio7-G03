from DataStructures.List import array_list as al

def size_tree(node):
    if node is None:
        return 0
    else:
        return 1 + size_tree(node.left) + size_tree(node.right)