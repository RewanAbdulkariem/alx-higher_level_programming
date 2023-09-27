#!/usr/bin/python3
class Node:
    """
    Represents a node of a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node): The next node in the linked list.

    Methods:
        __init__(self, data, next_node=None): Initializes a
        new node with the given data and an optional next node.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new node with the given data and an optional next node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): The next node in the
            linked list. Default is None.

        Raises:
            TypeError: If data is not an integer or if next_node
            is not a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for retrieving the data attribute.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for setting the data attribute.

        Args:
            value (int): The new data to set.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method for retrieving the next_node attribute.

        Returns:
            Node: The next node in the linked list
            , or None if there is no next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for setting the next_node attribute.

        Args:
            value (Node): The new next node to set, or None.

        Raises:
            TypeError: If value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.

    Attributes:
        head (Node): The head of the linked list.

    Methods:
        __init__(self): Initializes an empty singly linked list.
        sorted_insert(self, value): Inserts a new Node into
        the correct sorted position in the list (increasing order).
        __str__(self): Returns a string representation of the linked list.
    """
    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list

        Args:
            value (int): The value to insert into the list.

        Description:
            This method inserts a new node with the given value into
            the linked list in such a way that the list remains sorted
            in increasing order.
        """
        node = Node(value)
        cur = self.__head
        if cur is None or value < cur.data:
            node.next_node = cur
            self.__head = node
        else:
            while cur.next_node is not None and cur.next_node.data < value:
                cur = cur.next_node
            node.next_node = cur.next_node
            cur.next_node = node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: A string containing the values of the linked list nodes
            , one per line.
        """
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
