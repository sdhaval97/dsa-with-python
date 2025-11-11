# Implementing the good old Node, the cell in the world of data structures

# Creating a class node and creating the constructor
class Node:
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node
    
    # Creating getters for link node and value
    def get_value(self):
        return self.value
    
    def get_link_node(self):
        return self.link_node
    
    # We are allowing to update the link node (create a setter)
    def set_link_node(self, link_node):
        self.link_node = link_node
        