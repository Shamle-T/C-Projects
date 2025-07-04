from __future__ import annotations

"""
Basic class implementation of an array of references for FIT units

The code for the init function is a bit cryptic, so I explain it here in
detail. The instance variables holding the physical array is constructed
using the ctypes library to create a py_object (an object that can hold
a reference to any python object). Note that for each value of length we
have that (length * ctypes.py_object) is a type (e.g., if length=5, it
would be a type called py_object_Array_5). Then (length *
ctypes.py_object)() is equivalent to the initialisation in MIPS of the
space to hold the references.

Note that while I do check the precondition in __init__ (noone else
would), I do not check that of getitem or setitem, since that is already
checked by self.array[index].
"""

__author__ = "Julian Garcia for the __init__ code, Maria Garcia de la Banda for the rest"
__docformat__ = 'reStructuredText'

from ctypes import py_object
from typing import Generic, Union, TypeVar

T = TypeVar('T')


class ArrayR(Generic[T]):
    def __init__(self, length: int) -> None:
        """
        Creates an array of references to objects of the given length
        :complexity: O(length) for best/worst case to initialise to None
        :pre: length >= 0
        """
        if length < 0:
            raise ValueError("Array length cannot be negative.")
        self.array = (length * py_object)()  # initialises the space
        self.array[:] = [None for _ in range(length)]

    def __len__(self) -> int:
        """ Returns the length of the array
        :complexity: O(1)
        """
        return len(self.array)

    def __getitem__(self, index: int) -> T:
        """ Returns the object in position index.
        :complexity: O(1)
        :pre: index in between 0 and length - self.array[] checks it
        """
        return self.array[index]

    def __setitem__(self, index: int, value: T) -> None:
        """ Sets the object in position index to value
        :complexity: O(1)
        :pre: index in between 0 and length - self.array[] checks it
        """
        self.array[index] = value

    @classmethod
    def from_list(cls, lst: list) -> Union[ArrayR, None]:
        """ Creates an ArrayR from a list
        :complexity: O(n) where n is the length of the list
        """
        if len(lst) == 0:
            return None
        new_array = cls(len(lst))
        new_array.array[:] = lst
        return new_array

    def to_list(self) -> list:
        """ Returns a list representation of the array
        :complexity: O(n) where n is the length of the array
        """
        return [self.array[i] for i in range(len(self))]

    def __str__(self) -> str:
        """ Returns a string representation of the array
        :complexity: O(n) where n is the length of the array
        """
        return str([self.array[i] for i in range(len(self))])

    def __repr__(self) -> str:
        """ Returns a string representation of the array for debugging purposes
        :complexity: O(n) where n is the length of the array
        """
        return str(self)
