#!/usr/bin/python3
# 100-singly_linked_list.py
# Brennan D Baraban <375@holbertonschool.com>
"""Define classes for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next_node of the new Node.
        """
        if not isinstance(data, int):
            print("data must be an integer")
            self.data = 0
            raise TypeError
        elif not isinstance(next_node, Node) and next_node is not None:
            print("next_node must be a Node object")
            self.next_node = None
            raise TypeError
        else:
            self.data = data
            self.next_node = next_node

        @property
        def data(self):
            """Get/set the data of the node."""
            return (self.__data)

        @data.setter
        def data(self, value):
            if not isinstance(value, int):
                print("data must be an integer")
                raise TypeError
            self.__data = value

        @property
        def next_node(self):
            """Get/set the next_node of the node.

            Args:
                value (Node): The value of the next_node.
            """
            return (self.__next_node)

        @next_node.setter
        def next_node(self, value):
            if not isinstance(value, Node) and value is not None:
                print("next_node must be a Node object")
                raise TypeError
            self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        Args:
            value (Node): The new Node to insert.
        """
        if self.__head is None:
            self.__head = Node(value, None)
        elif self.__head.data > value:
            self.__head = Node(value, self.__head)
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            tmp.next_node = Node(value, tmp.next_node)

    def __str__(self):
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
