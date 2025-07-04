from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')
K = TypeVar('K')


class SortedList(ABC, Generic[T]):
    """ Sorted List ADT.
    Defines a generic abstract sorted list with the standard methods.
    Items to store should be of time ListItem.
    """

    @abstractmethod
    def __getitem__(self, index: int) -> T:
        """ Return the element at a given position. """
        pass

    @abstractmethod
    def __len__(self) -> int:
        """ Return the size of the list. """
        pass

    def __str__(self) -> str:
        """ String representation of the list object. """
        result = '['
        for i in range(len(self)):
            if i > 0:
                result += ', '
            result += str(self[i]) if type(self[i]) != str else "'{0}'".format(self[i])
        result += ']'
        return result

    @abstractmethod
    def delete_at_index(self, index: int) -> T:
        """ Delete item at a given position. """
        pass

    @abstractmethod
    def index(self, item: T) -> int:
        """ Find the position of a given item in the list. """
        pass

    def remove(self, item: T) -> None:
        """ Remove an item from the list. """
        index = self.index(item)
        self.delete_at_index(index)

    def is_empty(self) -> bool:
        """ Check if the list of empty. """
        return len(self) == 0

    @abstractmethod
    def clear(self) -> None:
        """ Clear the list. """
        pass

    @abstractmethod
    def add(self, item: T) -> None:
        """ Add new element to the list. """
        pass
