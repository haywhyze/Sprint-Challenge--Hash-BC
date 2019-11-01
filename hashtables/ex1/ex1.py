#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    while ht.capacity < length:
        hash_table_resize(ht)

    index = 0
    for item in weights:
        remainder = limit - item
        if hash_table_retrieve(ht, remainder) != None:
            if hash_table_retrieve(ht, remainder) > index:
                return (hash_table_retrieve(ht, remainder), index)
            return (index, hash_table_retrieve(ht, remainder))
        hash_table_insert(ht, item, index)
        index +=1
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
