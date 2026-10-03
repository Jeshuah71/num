
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class RecursiveBinarySearchTree:
    def __init__(self):
        self.root = None
    
    
    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        
        if value == current_node.value:
            return True
        
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        
        if value > current_node.value:
            return self.__r_contains(self.root, value)
        
        
    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    # rBST insert

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
            
        if value > current_node.value: 
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        
        self.__r_insert(self.root, value)
    
    def min_value(self, current_node):
            while current_node.left is not None:
                current_node = current_node.left
            
            return current_node.value  
    # delete in a recursiveBinarySearchTree
    def __delete_node(self, current_node, value):
        if current_node == None:
            return None
    
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
            
        else:
            # case is is a leaf node
            if current_node.left == None and current_node.right == None:
                return None 
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                subtree_min = self.min_value(current_node.right)
                current_node.value = subtree_min
                current_node.right = self.__delete_node(current_node.right, subtree_min)
        return current_node
    
