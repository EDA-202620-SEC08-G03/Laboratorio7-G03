from platform import node

from DataStructures.List import single_linked_list as sl
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
        root["size"] = size_tree(root["left"]) + size_tree(root["right"]) + 1
        
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
        root["size"] = size_tree(root["left"]) + size_tree(root["right"]) + 1
    elif key > root["key"]:
        root["right"] = remove_node(root["right"], key)
        root["size"] = size_tree(root["left"]) + size_tree(root["right"]) + 1
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
            root["size"] = size_tree(root["left"]) + size_tree(root["right"]) + 1
            
    return root


def size_tree(root):
    if root is None:
        return 0
    else:
        return size_tree(root["left"]) + size_tree(root["right"]) + 1
    
def size(my_bst):
    return size_tree(my_bst["root"])


def contains(my_bst, key):
    busqueda = get(my_bst, key)
    if busqueda is None:
        return False
    else:
        return True


def is_empty(my_bst):
    booleano = my_bst["root"] is None
    return booleano


def key_set_tree(root, keys):
    if root is not None:
        key_set_tree(root["left"], keys)
        sl.add_last(keys, root["key"])
        key_set_tree(root["right"], keys)
        
    return None

def key_set(my_bst):
    keys = sl.new_list()
    key_set_tree(my_bst["root"], keys)
    return keys


def value_set_tree(root, values):
    if root is not None:
        value_set_tree(root["left"], values)
        sl.add_last(values, root["value"])
        value_set_tree(root["right"], values)
    return None
        
def value_set(my_bst):
    values = sl.new_list()
    value_set_tree(my_bst["root"], values)
    return values


def get_min(my_bst):
    if my_bst["root"] is not None:
        
        menor = my_bst["root"]
        while menor["left"] is not None:
            menor = menor["left"]
        return menor["key"], menor["value"]
    
    return None


def get_max(my_bst):
    if my_bst["root"] is not None:
        
        mayor = my_bst["root"]
        while mayor["right"] is not None:
            mayor = mayor["right"]
        return mayor["key"], mayor["value"]
    
    return None
   
    
def delete_min_tree(root):
    if root is not None:
        if root["left"] is None:
            return root["right"]
        
        root["left"] = delete_min_tree(root["left"])
        root["size"] = size_tree(root["left"]) + size_tree(root["right"]) + 1
        return root
    return None

def delete_min(my_bst):
    my_bst["root"] = delete_min_tree(my_bst["root"])
    return my_bst


def delete_max_tree(root):
    if root is not None:
    
        if root["right"] is None:
            return root["left"]
        
        root["right"] = delete_max_tree(root["right"])
        root["size"] = size_tree(root["left"]) + size_tree(root["right"]) + 1
        return root
    return None

def delete_max(my_bst):
    my_bst["root"] = delete_max_tree(my_bst["root"])
    return my_bst
    