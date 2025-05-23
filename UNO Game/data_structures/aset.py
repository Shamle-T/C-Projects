"""
    Array-based implementation of Set ADT.
"""

from __future__ import annotations
from data_structures.set_adt import *
from data_structures.referential_array import ArrayR


class ASet(Set[T]):
    """Simple array-based implementation of the set ADT.

    Attributes:
         size (int): number of elements in the set
         array (ArrayR[T]): array storing the elements of the set

    ArrayR cannot create empty arrays. So default capacity value 1
    is used to avoid this.
    """

    MIN_CAPACITY = 1

    def __init__(self, capacity: int = 1) -> None:
        """Initialization."""
        Set.__init__(self)
        self.array = ArrayR(max(self.MIN_CAPACITY, capacity))

    def __len__(self) -> int:
        """Returns the number of elements in the set."""
        return self.size

    def is_empty(self) -> bool:
        """True if the set is empty."""
        return len(self) == 0

    def __contains__(self, item: T) -> bool:
        """True if the set contains the item."""
        for i in range(self.size):
            if item == self.array[i]:
                return True
        return False

    def clear(self) -> None:
        """Makes the set empty."""
        self.size = 0

    def is_full(self) -> bool:
        """True if the set is full and no element can be added."""
        return len(self) == len(self.array)

    def add(self, item: T) -> None:
        """Adds an element to the set. Note that an element already
        present in the set should not be added.
        :pre: the set is not full
        :raises Exception: if the set is full.
        """
        if item not in self:
            if self.is_full():
                raise Exception("the set if full")

            self.array[self.size] = item
            self.size += 1

    def remove(self, item: T) -> None:
        """Removes an element from the set.
        :pre: the element should be present in the set
        :raises KeyError: if no such element is found.
        """
        for i in range(self.size):
            if item == self.array[i]:
                self.array[i] = self.array[self.size - 1]
                self.size -= 1
                break
        else:
            raise KeyError(item)

    def union(self, other: ASet[T]) -> ASet[T]:
        """Creates a new set equal to the union with another one,
        i.e. the result set should contains the elements of self and other.
        """
        res = ASet(len(self.array) + len(other.array))

        for i in range(len(self)):
            res.array[i] = self.array[i]
        res.size = self.size

        for j in range(len(other)):
            if other.array[j] not in self:
                res.array[res.size] = other.array[j]
                res.size += 1

        return res

    def intersection(self, other: ASet[T]) -> ASet[T]:
        """Creates a new set equal to the intersection with another one,
        i.e. the result set should contain the elements that are both in
        self *and* other.
        """
        res = ASet(min(len(self.array), len(other.array)))

        for i in range(len(self)):
            if self.array[i] in other:
                res.array[res.size] = self.array[i]
                res.size += 1

        return res

    def difference(self, other: ASet[T]) -> ASet[T]:
        """Creates a new set equal to the difference with another one,
        i.e. the result set should contain the elements of self that
        *are not* in other.
        """
        res = ASet(len(self.array))

        for i in range(len(self)):
            if self.array[i] not in other:
                res.array[res.size] = self.array[i]
                res.size += 1

        return res

    def __str__(self):
        """Magic method constructing a string representation of the list object."""
        elems = []
        for i in range(len(self)):
            elems.append(
                str(self.array[i])
                if type(self.array[i]) != str
                else "'{0}'".format(self.array[i])
            )
        return "{" + ", ".join(elems) + "}"
