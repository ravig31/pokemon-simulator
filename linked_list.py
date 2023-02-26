""" Linked-node based implementation of List ADT. """
from __future__ import annotations

from node import Node, T, Generic
import node
from abstract_list import List, T

__author__ = 'Maria Garcia de la Banda and Brendon Taylor. Modified by Alexey Ignatiev'
__docformat__ = 'reStructuredText'

class LinkedList(Generic[T]):
    """ List ADT implemented with linked nodes. """
    def __init__(self) -> None:
        """ Linked-list object initialiser. """
        self.head = None
        self.length = 0

    def clear(self):
        """ Clear the list. """
        # first call clear() for the base class
        List.clear(self)
        self.head = None

    def __setitem__(self, index: int, item: T) -> None:
        """ Magic method. Insert the item at a given position. """
        # TODO
        node_at_index = self.__get_node_at_index(index)
        node_at_index.item = item        

    def __getitem__(self, index: int) -> T:
        """ Magic method. Return the element at a given position. """
        node_at_index = self.__get_node_at_index(index)
        return node_at_index.item

    def index(self, item: T) -> int:
        """ Find the position of a given item in the list. """
        return node.index(self.head, item)

    def __get_node_at_index(self, index: int) -> Node[T]:
        """ Get node object at a given position. """
        if 0 <= index and index < len(self):
            return node.get_node_at_index(self.head, index)
        else:
            raise ValueError('Index out of bounds')

    def delete_at_index(self, index: int) -> T:
        """ Delete item at a given position. """
        try:
            previous_node = self.__get_node_at_index(index-1)
        except ValueError as e:
            if self.is_empty():
                raise ValueError('List is empty')
            elif index == 0:
                item = self.head.item
                self.head = self.head.next
            else:
                raise e
        else:
            item = previous_node.next.item
            previous_node.next = previous_node.next.next
        self.length -= 1
        return item
        

    def insert(self, index: int, item: T) -> None:
        """ Insert an item at a given position. """
        # TODO
        new_node = Node(item)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            previous_node = self.__get_node_at_index(index - 1)
            new_node.next = previous_node.next
            previous_node.next = new_node
        self.length += 1

    def append(self, item: T) -> None:
        """ Insert an item at a given position. """
        self.head = node.append(self.head, item)

    def __iter__(self) -> LinkedListIterator[T]:
        """ Magic method. Creates and returns an iterator for the list. """
        return LinkedListIterator(self.head)

class LinkedListIterator(Generic[T]):
    """ A full-blown iterator for class LinkedList.

        Attributes:
            current (Node[T]): the node whose item will be returned next
    """
    def __init__(self, node: Node[T]) -> None:
        """ Initialises self.current to the node given as input. """
        self.current = node

    def __iter__(self) -> LinkedListIterator[T]:
        """ Returns itself, as required to be iterable. """
        return self

    def __next__(self) -> T:
        """ Returns the current item and moves to the next node.
            :raises StopIteration: if the current item does not exist
        """
        if self.current is not None:
            item = self.current.item
            self.current = self.current.link
            return item
        else:
            raise StopIteration

if __name__ == '__main__':
    list = LinkedList()
    for i in range(5):
        list.append(2*i)

    for item in list:
        print(item)
