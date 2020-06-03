"""
Psuedo Code:
2
PUT:
3
Find the hash index
4
Search the list for the given key,
5
If given key already exists: simply overwrite / repalce the value of that key
6
It it's not: append the new record to the list"""


class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here

        # if capacity < MIN_CAPACITY:  # making sure its not below 8
        #     capacity = MIN_CAPACITY

        if capacity >= MIN_CAPACITY:  # making sure its not below 8
            self.data = [None]*capacity
            self.capacity = capacity
        else:
            [None]*capacity
            MIN_CAPACITY

        # self.data = [None]*capacity
        # self.capacity = capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return(self.data)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        # hash_val = get_num_slots(self)
        # return hash_val % MIN_CAPACITY

        return sum([bool(x)] for x in self.data)/self.get_num_slots()

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        # https://gist.github.com/vaiorabbit/5670985
        hval = 0x811c9dc5
        fnv_32_prime = 0x01000193
        # uint32_max = 2 ** 32
        for s in key:
            hval = hval ^ ord(s)
            hval = (hval * fnv_32_prime) % self.capacity
        return hval

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        # uses num that are prime to each other =>24/5
        # goal: bc they are offset to each other, they are less likely to produce collision
        # hash value

        str_key = str(key).encode()

        # Start from an arbitrary large prime
        hash_value = 5381
        # Bit-shift and sum value for each character
        for b in str_key:
            # << = bitwise operator, left shift by 5 places (multiplying 2^5)
            hash_value = ((hash_value << 5) + hash_value) + b
            hash_value &= 0xffffffff  # DJB2 is a 32-bit hash, only keep 32 bits
        return hash_value 

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        slot = HashTableEntry(key, value)
        # MIN_CAPACITY[slot] = value
        self.data[self.fnv1(key)] = slot

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # put(key, None)
        self.put(key, None)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        return self.data[self.fnv1(key)].value
# resize table when it gets too loaded

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
