# 1. 1.1 7  1.2 2


def bin_search(key, array):
    lo = 0
    hi = len(array) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        val = array[mid]
        print(val)
        if key == val:
            return True
        elif key < val:
            hi = mid - 1
        else: # key > val
            lo = mid + 1
    return False

lst = [-2, 9, 11, 12, 13, 14, 15, 22, 142]
print(bin_search(15, lst))