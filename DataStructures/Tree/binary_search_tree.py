from platform import node

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


def size_tree(node):
    if node is None:
        return 0
    else:
        return size_tree(node["left"]) + size_tree(node["right"]) + 1
    
def size(my_bst):
    return size_tree(my_bst["root"])

def contains(my_bst, key):
    booleano = al.get_element(my_bst["root"], key) is not None
    return booleano

def is_empty(my_bst):
    booleano = my_bst["root"] is None
    return booleano

def key_set_tree(node, keys):
    if node is not None:
        key_set_tree(node["left"], keys)
        al.add_last(node["key"], keys)
        key_set_tree(node["right"], keys)
        
    return None

def key_set(my_bst):
    keys = al.new_list()
    key_set_tree(my_bst["root"], keys)
    return keys

def value_set_tree(node, values):
    if node is not None:
        value_set_tree(node["left"], values)
        al.add_last(node["value"], values)
        value_set_tree(node["right"], values)
    return None
        
def value_set(my_bst):
    values = al.new_list()
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
    
def delete_min_tree(node):
    if node is not None:
        if node["left"] is None:
            return node["right"]
        
        node["left"] = delete_min_tree(node["left"])
        node["size"] = size_tree(node["left"]) + size_tree(node["right"]) + 1
        return node
    return None

def delete_min(my_bst):
    my_bst["root"] = delete_min_tree(my_bst["root"])
    return my_bst

def delete_max_tree(node):
    if node is not None:
    
        if node["right"] is None:
            return node["left"]
        
        node["right"] = delete_max_tree(node["right"])
        node["size"] = size_tree(node["left"]) + size_tree(node["right"]) + 1
        return node
    return None

def delete_max(my_bst):
    my_bst["root"] = delete_max_tree(my_bst["root"])
    return my_bst
    