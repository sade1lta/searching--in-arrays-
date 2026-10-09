def seq_search(key, array):
    index = 0
    found = False
    while not found and index < len(array):
        if array[index] == key:
            found = True
        index += 1
    return found