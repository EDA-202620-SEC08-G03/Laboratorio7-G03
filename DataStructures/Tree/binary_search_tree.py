from DataStructures.List import array_list as al

def put(my_bts, key, value):
    pass  
def insert_node(root, key, value):
    pass
def get(my_bst, key):
    pass
def get_node(root, key):
    pass
def remove(my_bst, key):
    pass
def size(my_bst):
    pass
def size_tree(node):
    if node is None:
        return 0
    else:
        return size_tree(node["left"]) + size_tree(node["right"]) + 1
    
def size(my_bst):
    return size_tree(my_bst["root"])
    
def insert_node(root, key, value):
    if root is None:
        return {"key": key, "value": value, "left": None, "right": None}
    elif key < root["key"]:
        root["left"] = insert_node(root["left"], key, value)
    elif key > root["key"]:
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value
    return root   