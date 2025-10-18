# implementing a linked list with Nodes

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    # getters for value and next node
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    # setter for next_node
    def set_next_node(self, next_node):
        self.next_node = next_node

# creating the linked list class now that we have created the Node
class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)
    
    # getter for head node
    def get_head_node(self):
        return self.head_node
    
    # inserting a node at the beginning of the list
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    
    # stringify the list
    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list
    