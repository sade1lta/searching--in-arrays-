def bin_search(key, array):
    lo = 0
    hi = len(array) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        val = array[mid]
        if key == val:
            return True
        elif key < val:
            hi = mid - 1
        else: # key > val
            lo = mid + 1
    return False

def time_search(algo, n, /, sort_data=False):
    import random, time

    # n samples with replacement from [0,1,...,n-1]
    data = random.choices(range(n), k=n)
    if sort_data: data.sort()
    key = n # never found, ensures worst case

    start = time.process_time()
    algo(key, data)
    end = time.process_time()
    return end - start

print(time_search(bin_search, 10**5)) 