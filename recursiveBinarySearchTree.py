
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
            return self.__r_contains(current_node.right, value)
        
        
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
    
    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)
    
    # Convert sort a list 
    def __sorted_list_to_bst(self, nums, left, right):
        # Base case
        # if left past right, there are no elements left
        if left > right:
            return None
        
        # Find the middle index 
        mid = (left + right) // 2
        
        # Create a node using the middle value 
        node = Node(nums[mid])
        
        # Recursively build the left subtree 
        node.left = self.__sorted_list_to_bst(nums, left, mid - 1)
        
        # Recursively build the right subtree
        node.right = self.__sorted_list_to_bst(nums, mid + 1, right)
        
        # Return the root of the subtree 
        return node 

# Breadth first search this is binary search tree clas 

    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            
            if current_node.left is not None:
                queue.append(current_node.left)
                
            if current_node.right is not None:
                queue.append(current_node.right)
                
        return results
    
    # Depth first search in binary search tree
    def DFS_pre_order(self):
        results = []
        
        def traverse(current_node):
            results.append(current_node.value)
            
            if current_node.left is not None:
                traverse(current_node.left)
                
            if current_node.right is not None:
                traverse(current_node.right)
                
        traverse(self.root)
        return results
    
    # Depth first search post order in binary search tree
    def DFS_post_order(self):
        results = []
        
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
                
            if current_node.right is not None:
                traverse(current_node.right)
                
            results.append(current_node.value)
            
        traverse(self.root)
        return results
    
    # depth first search in order in binary search tree
    def DFS_in_order(self):
        results = []
        
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
                
            results.append(current_node.value)
            
            if current_node.right is not None:
                traverse(current_node.right)
                
        traverse(self.root)
        return results
    
    
    def __sorted_list_to_bst(self, nums, left, right):
        # Base case:
        # if there are no numbers left in this section, there is no node to create
        if left > right:
            return None
        
        # Find the middle index 
        mid = Node(left + right) // 2
        
        # Create a node using the middle value
        node = Node(nums[mid])
        
        # Build the left subtree using everything before the middle 
        node.left = self.__sorted_list_to_bst(nums, left, mid - 1)
        
        # Build the right subtree using everything after the middle
        node.right = self.__sorted_list_to_bst(nums, mid + 1, right)
        
        return node
    
    
    
    