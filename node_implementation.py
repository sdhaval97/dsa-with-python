# implementing a node in python with immutable value and mutable link node

class Node:
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node
    
    # creating a setter for link node
    def set_link_node(self, link_node):
        self.link_node = link_node
    
    # creating getters for value and link node
    def get_value(self):
        return self.value
    
    def get_link_node(self):
        return self.link_node