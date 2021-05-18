#!/usr/bin/python3
"""defining a square"""


class Node:
    """ represents a square

    Attributes:
        ___size (int): size of a side of the square
        ___position (tuple): pos of the square
    """
    def __init__(self, data, next_node=None):
           self.data = data
           self.next_node = next_node
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        """setter of __data
        Args:
            value (int): data stored insite the node
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value


    @property
    def next_node(self):
        return self.__next_node
        

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value
    
    def __str__(self):
        return str(self.__data)




class SinglyLinkedList:

    def __init__(self):
        self.__head = None
    
    def sorted_insert(self, value):

        new = Node(value)
        tmp = self.__head

        if tmp is None or tmp.data >= value:
            if tmp:
                new.next_node = tmp
            self.__head = new
            return
        while tmp.next_node is not None:
            if tmp.next_node.data >= value:
                break
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new

    def __str__(self):
        string = ""
        tmp = self.__head
        while tmp is not None:
            string += str(tmp)
            if tmp.next_node is not None:
                string += "\n"
            tmp = tmp.next_node
        return string

