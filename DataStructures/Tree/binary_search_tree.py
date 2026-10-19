from DataStructures.List import array_list as al

def put(my_bts, key, value):
    if my_bts["root"]==key:
        my_bts["root"]["value"]=value
    
def insert_node(root, key, value):
    if root is None:
        return {"key": key, "value": value, "left": None, "right": None}
    if key > root:
        if root["right"] is None:
            root["right"] = key
            root["right"]["value"] = value
        else:
            insert_node(root["right"],key, value)
    elif key<root:
        if root["left"] is None:
            root["left"] = key
            root["left"]["value"] = value
        else:
            insert_node(root["left"],key,value)
    return root
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