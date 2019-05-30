import numpy as np
# import math

memory = np.zeros(128)


def allocate(blocks):
    """
    Allocates memory as specified by the user
    :param blocks: number of blocks to allocate
    :return: modified memory as a list
    """
    np.append(memory, 2)
    np.insert(memory, 0, 2)

    print("Blocks ", blocks)
    for i in range(len(memory)):
        if memory[i] == 0:
            memory[i:blocks] = 1
    return


def free(address):
    """
    Frees up memory as defined by the user.
    :param address: The start address from where to free up memory
    :return: the modified memory as a list
    """
    for i in range(len(memory)):
        if i == address:
            for j in range(len(memory[i:])):
                if j == 0:
                    memory[i:j-1] = 0
    return


def display():
    """
    Iterates through the memory list
    Free spaces are - encoded as 0
    Assigned spaces # encoded as as 1
    Partitions are | encoded as 2
    :return:
    """
    memory_string = ""

    for unit in memory:
        if unit == 0:
            memory_string += "-"
        elif unit == 1:
            memory_string += "#"
        elif unit == 2:
            memory_string += "|"

    print(memory_string)
    return


while True:
    instructions = "Type a [number of blocks to allocate]\n Type f [addresses to free] \n q to quit\n"
    key = input("How many blocks do you want to allocate or free?: \n"+instructions).split()
    if key[0] == 'a':
        allocate(int(key[1]))
        display()
    elif key[0] == 'f':
        free(int(key[1]))
        display()
    elif key[0] == 'q':
        break
