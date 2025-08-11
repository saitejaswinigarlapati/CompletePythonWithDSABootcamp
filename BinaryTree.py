class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
root=BinaryTreeNode(1)
root.left=BinaryTreeNode(2)
root.right=BinaryTreeNode(3)


def print_binary_tree(root):
    if (root is None):
        return
    print(root.data,end=' : ')

    if(root.left is not None):
        print(f"L -> {root.left.data}",end=",")
    else:
        print("L-> None",end=",")
        
    if(root.right is not None):
            print(f"R -> {root.left.data}")
    else:
        print("R-> None")
        
    print_binary_tree(root.left)
    print_binary_tree(root.right)
    
print_binary_tree(root)


def take_input_binary_tree():
    data=int(input("Enter the data for the Node : "))
    if(data == -1):
        return None
    node=BinaryTreeNode(data)
    
    print(f"Enter the left child of {data}")
    node.left=take_input_binary_tree()
    
    print(f"Enter the right child for {data}")
    node.right=take_input_binary_tree()
    
    return node
        
print("Enter the Binary Tree Data (-1 for No Node )")
root=take_input_binary_tree()

print_binary_tree(root)


from collections import deque

def take_input_level_wise():
    data=int(input("Enter the data of the Root : "))
    if(data ==-1):
        return None
    root=BinaryTreeNode(data)
    queue = deque([root])
    
    while len(queue) != 0:
        current_node=queue.popleft()
        left_child_data=int(input(f"Enter left child for {current_node.data} "))
        if(left_child_data != -1):
            left_node=BinaryTreeNode(left_child_data)
            current_node.left=left_node
            queue.append(left_node)
            
        right_child_data=int(input(f"Enter right child for {current_node.data} "))
        if(right_child_data != -1):
            right_node=BinaryTreeNode(right_child_data)
            current_node.right=right_node
            queue.append(right_node)
            
    return root
root=take_input_level_wise()
print_binary_tree(root)

def print_binary_tree_level_wise(root):
    if (root is None):
        return
    queue=deque([root])
    
    while queue:
        node=queue.popleft()
        print(node.data,end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    
root=take_input_binary_tree()
print_binary_tree_level_wise(root)
