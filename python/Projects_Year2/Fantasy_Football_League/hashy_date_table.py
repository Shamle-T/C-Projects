from __future__ import annotations

from data_structures.hash_table_linear_probing import LinearProbeTable


class HashyDateTable(LinearProbeTable[str]):
    """
    HashyDateTable assumed the keys are strings representing dates, and therefore tries to
    produce a balanced, uniform distribution of keys across the table.

    Conflicts are resolved using Linear Probing.
    
    All values will also be strings.
    """
    def __init__(self) -> None:
        """
        Initialise the Hash Table with increments of 366 as the table size.
        This means, initially we will have 366 slots, once they are full, we will have 4 * 366 slots, and so on.

        No complexity is required for this function.
        Do not make any changes to this function.
        """
        LinearProbeTable.__init__(self, [366, 4 * 366, 16 * 366])



    def hash(self, key: str) -> int:
        """
        Hash a key for insert/retrieve/update into the hashtable.
        The key will always be exactly 10 characters long and can be any of these formats, but nothing else:
        - DD/MM/YYYY
        - DD-MM-YYYY
        - YYYY/MM/DD
        - YYYY-MM-DD

        The function assumes the dates will always be valid i.e. the input will never be something like 66/14/2020.

        Complexity:
        Best Case Complexity: O(1)
            Occurs when the year is closer to 0, Nonetheless the calculation becomes bigger as the timeline increases. Since the function relies on a simple calculation the complexity will remain O(1), hence hash function calculation is instantanious at O(1)

        Worst Case Complexity: O(1)
            Both best and worse case are the same, however having a large date will mean the calculation will be heavy, however the complexity will not change, as the current calculation is still O(1)
        """

        #Returns the table size
        TABLESIZE = self.table_size
        YEAR_SIZE = 366

        #Key design IF -/ form - #DDMMYYYY
        if (key[4] in "-/"):
            day = key[8:10]
            month = key[5:7]
            year = key[:4]

        else:
            day = key[:2]
            month = key[3:5]
            year = key[6:10]

        #Hash function
        hash = ((int(year)*YEAR_SIZE) + (int(month)*self.HASH_BASE) + int(day))
        value = hash % TABLESIZE

        return value
