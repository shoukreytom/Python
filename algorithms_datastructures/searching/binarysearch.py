def binary_search(array, key):
    low = 0
    high = len(array) - 1
    for i in range(len(array)):
        mid = int(low + (high - low) / 2)
        if key > array[mid]:
            low = mid + 1
        elif key < array[mid]:
            high = mid-1
        else:
            return array.index(key)
    return -1


array = [1, 2, 3, 5, 9, 11]
b = binary_search(array, 2)
print(b)
      