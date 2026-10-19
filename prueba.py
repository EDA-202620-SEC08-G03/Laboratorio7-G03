from DataStructures.Tree import bst_node as bst_node

def default_compare(key, element):
   if key == bst_node.get_key(element):
      return 0
   elif key > bst_node.get_key(element):
      return 1
   return -1

def get(my_bst, key):
    
    