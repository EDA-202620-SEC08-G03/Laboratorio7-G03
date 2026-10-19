from DataStructures.List import array_list as al

def put(my_bts, key, value):
    pass 
def insert_node(root, key, value):
    pass

def get(my_bst, key):
    
    value = get_node(my_bst["root"], key)
    return value

def get_node(root, key):
    
    if root is None:
        return None
    else:
        if key == root["key"]:
            return root["value"]
        elif key < root["key"]:
            return get_node(root["left"], key)
        else:
            return get_node(root["right"], key)
        
def remove(my_bst, key):
    pass
def size(my_bst):
    pass
def size_tree(node):
    if node is None:
        return 0
    else: