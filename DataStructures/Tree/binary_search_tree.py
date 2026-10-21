from DataStructures.List import array_list as al
from DataStructures.Tree import bst_node as bnode

def new_map():
    return {"root":None}


def put(my_bts, key, value):

    my_bts["root"] = insert_node(my_bts["root"], key, value)
    return my_bts

def insert_node (root, key, value):
    if root is None:
        return bnode.new_node(key, value)
    
    if key > root["key"]:
        return insert_node(root["right"], key, value)
    elif key < root["key"]:
        return insert_node(root["left"], key, value)
    else:
        root["value"] = value
        
    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
        
    return root


def get_node(root, key):
    
    if root is None:
        return None
    
    if key < root["key"]:
        return get_node(root["left"], key)
    elif key > root["key"]:
        return get_node(root["right"], key)
    else:   
        return bnode.get_value(root)

def get(my_bst, key):
    
    value = get_node(my_bst["root"], key)
    return value
        
        
def remove (my_bst, key):
    my_bst["root"] = remove_node(my_bst["root"], key)
    return my_bst

def remove_node (root, key):
    
    if root is None:
        return None
    
    if key < root["key"]:
        root["left"] = remove_node(root["left"], key)
    elif key > root["key"]:
        root["right"] = remove_node(root["right"], key)
    else:
        if root["right"] is None and root["left"] is None:
            return None
        elif root["right"] is not None and root["left"] is None:
            return root["right"]
        elif root["right"] is None and root["left"] is not None:
            return root["left"]
        else:
            menormayores = root["right"]
            while menormayores["left"] is not None:
                menormayores = menormayores["left"]
                
            root["key"] = menormayores["key"]
            root["value"] = menormayores["value"]
            root["right"] = remove_node(root["right"], root["key"])
            
    return root


def size_tree(node):
    if node is None:
        return 0
    else:
        return size_tree(node["left"]) + size_tree(node["right"]) + 1
    
def size(my_bst):
    return size_tree(my_bst["root"])