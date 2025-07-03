from __future__ import annotations

from data_structures.referential_array import ArrayR
from data_structures.abstract_hash_table import HashTable
from typing import TypeVar


V = TypeVar('V')


class LazyDoubleTable(HashTable[str, V]):
    """
    Lazy Double Table uses double hashing to resolve collisions, and implements lazy deletion.

    Feel free to check out the implementation of the LinearProbeTable class if you need to remind
    yourself how to implement the methods of this class.

    Type Arguments:
        - V: Value Type.
    """
    
    # No test case should exceed 1 million entries.
    TABLE_SIZES = (5, 13, 29, 53, 97, 193, 389, 769, 1543, 3079, 6151, 12289, 24593, 49157, 98317, 196613, 393241, 786433, 1572869)
    HASH_BASE = 31
    _DELETED_SENTINEL = object()


    def __init__(self, sizes = None) -> None:
        """
        No complexity analysis is required for this function.
        Do not make any changes to this function.
        """
        if sizes is not None:
            self.TABLE_SIZES = sizes

        self.__size_index = 0
        self.__array: ArrayR[tuple[str, V]] = ArrayR(self.TABLE_SIZES[self.__size_index])
        self.__length = 0
    
    @property
    def table_size(self) -> int:
        return len(self.__array)

    def __len__(self) -> int:
        """
        Returns the number of elements in the hash table
        """
        return self.__length

    def keys(self) -> ArrayR[str]:
        """
        Returns all keys in the hash table.
        :complexity: O(N) where N is the number of items in the table. (old)
        :complexity O(N+S) where N is the number of items in the table and S is the table size.
        """
        res = ArrayR(self.__length)
        i = 0
        for x in range(self.table_size):
            if self.__array[x] is not None or self.__array[x] is self._DELETED_SENTINEL :
                res[i] = self.__array[x][0]
                i += 1
        return res

    def values(self) -> ArrayR[V]:
        """
        Returns all values in the hash table.

        :complexity: O(N) where N is the number of items in the table. (old)
        :complexity O(N+S) where N is the number of items in the table and S is the table size.

        """
        res = ArrayR(self.__length)
        i = 0
        for x in range(self.table_size):
            if self.__array[x] is not None:
                res[i] = self.__array[x][1]
                i += 1
        return res

    def __contains__(self, key: str) -> bool:
        """
        Checks to see if the given key is in the Hash Table

        :complexity: See __getitem__.
        """
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True

    def __getitem__(self, key: str) -> V:
        """
        Get the value at a certain key

        :complexity: See hashy probe.
        :raises KeyError: when the key doesn't exist.
        """
        position = self.__hashy_probe(key, False)
        return self.__array[position][1]
    
    def is_empty(self) -> bool:
        return self.__length == 0
    
    def __str__(self) -> str:
        """
        Returns all they key/value pairs in our hash table (no particular
        order).
        """
        result = ""
        for item in self.__array:
            if item is not None:
                (key, value) = item
                result += "(" + str(key) + "," + str(value) + ")\n"
        return result

    def hash(self, key: str) -> int:
        """
        Hash a key for insert/retrieve/update into the hashtable.
        :complexity: O(len(key))
        """
        value = 0
        a = 31415
        for char in key:
            value = (ord(char) + a * value) % self.table_size
            a = a * self.HASH_BASE % (self.table_size - 1)
        return value

    def hash2(self, key: str) -> int:
        """
        Used to determine the step size for our hash table.

        Complexity:
            Best Case Complexity: O(M)
                Occurs when you have to loop through every character in the key, even if it is 1 STRING value.
                Since each character gets its own value, that will be cumulatively added to receive the final hash.

            Worst Case Complexity: O(M)
                Requires traversing through the characters in key using the for loop.
                Finding the step_increment is instantaneous at O(1)

        Further notes:
            Using the step_increment automatic co primes can be found

        M : length of the key, when finding the step increment (len(key))
        """

        value = 0
        for char in key:
            value = (value * self.HASH_BASE + ord(char)) % self.table_size

        step_increment =  (value % (self.table_size - 1))+1
        return step_increment



    def __hashy_probe(self, key: str, is_insert: bool) -> int:
        """
        Find the correct position for this key in the hash table using hashy probing.

        Raises:
            KeyError: When the key is not in the table, but is_insert is False.
            RuntimeError: When a table is full and cannot be inserted.

        Complexity:
            Best Case Complexity: O(N)
                Occurs when there are no collisions in the hashtable, allowing the loop to iterate only once.
                We receive the hash of the key using the hash() function which will cost us O(N)
                We receive another hash that acts as the step counter using hash2() which will cost us O(N)
                Adding the data into the hashtable with no collisions will result in the Best case scenario.

            Worst Case Complexity: O(N * M)
                Occurs when there are multiple collisions in the hashtable, hence the loop iterates multiple times. (M times)
                If the position of the hash is occupied probing will occur, resulting in calling a 2nd hash value for double hashing (step)
                When the first hash is used to compare the value of the key with the slot, a comparison between the strings occur resulting in the complexity to be O(N)
                Complexity = M * O(N) = O(M*N)

        M : iterations of the for loop due to the collisions in the hash table
        N = average key length (the cost to hash or compare one key) - hashing with probing
        """
        # Initial position
        position = self.hash(key)
        step = self.hash2(key)

        first_sentinel = None

        for _ in range(self.table_size):
            if self.__array[position] is None:
                if is_insert:
                    if first_sentinel is not None:
                        return first_sentinel
                    else:
                        return position
                else:
                    raise KeyError(key)

            elif self.__array[position] is self._DELETED_SENTINEL:
                if is_insert and first_sentinel is None:
                    first_sentinel = position

            else:
                if self.__array[position][0] == key:
                    return position


            # Taken by something else. Time to hashy probe.
            position = (position + step) % self.table_size

        if is_insert and first_sentinel is not None:
            return first_sentinel

        if is_insert:
            raise RuntimeError("Table is full!")
        else:
            raise KeyError(key)

    def __setitem__(self, key: str, data: V) -> None:
        """
        Set a (key, value) pair in our hash table.

        Remember! This is where you will need to call __rehash if the table is full!
        
        Complexity:
            Best Case Complexity: O(N)
                Occurs when The current tables size doesn't exceed the hash table's load capacity(2/3)
                No collisions occur due to probing
                Receiving the hash from the __hashy_probe will incur O(N)

            Worst Case Complexity: O(N * M^2)
                Occurs when the __rehash function has to be called, since the current table size exceeded the load capacity
                If there is a collision with the generated hash of the key, this triggering probing to occur if all the positions of the hash table are filled
                When multiple collisions are detected this will cause double hashing to occur to find the hash value, thereby incuring the worst case scenario in __hashy_probe function
                As M grows due to increasing load factor, we will get a constant making it M^2
        M = iterations of the loop
        N = average key length (the cost to hash or compare one key) - hashing with probing
        """
        position = self.__hashy_probe(key, True)

        if self.__array[position] is None or self.__array[position] == self._DELETED_SENTINEL:
            self.__length += 1

        self.__array[position] = (key, data)

        if (self.__length / self.table_size) >= 2/3:
            self.__rehash()


    def __delitem__(self, key: str) -> None:
        """
        Deletes a (key, value) pair in our hash table.

        Complexity:
            Best Case Complexity: O(N)
                Occurs when a probe can be found successfully in the first try, triggering the best case scenario in __hashy_probe()

            Worst Case Complexity: O(N * M)
                Occurs if there are collisions with the generated hash of the key, triggering probing to occur multiple times, hence the worst case scenario in __hashy_probe()
        M = iterations of the loop
        N = average key length (the cost to hash or compare one key) - hashing with probing
        """
        position = self.__hashy_probe(key, False)
        self.__array[position] = self._DELETED_SENTINEL
        self.__length -= 1


    def __rehash(self) -> None:
        """
        Need to resize table and reinsert all values

        Complexity:
            Best case (O(M))
                Occurs when each value is replaced by a sentinel, so the for loop will not execute further down, it will only iterate through the sentinel values, thereby only M iterations have to be made to traverse this.
            
            Worst case (O(N^2·M))
                If every insertion has to probe through all the slots before finding a home, that’s up to N steps per item. Multiply by N items and the K cost per comparison, and you get N×N×K.

        M = iterations of the loop
        N = average key length (the cost to hash or compare one key) - hashing with probing
        """
        old_array = self.__array
        self.__size_index += 1
        if self.__size_index == len(self.TABLE_SIZES):
            return

        self.__array = ArrayR(self.TABLE_SIZES[self.__size_index])
        self.__length = 0
        for item in old_array:
            if item or item == self._DELETED_SENTINEL:
                key, value = item
                self[key] = value
