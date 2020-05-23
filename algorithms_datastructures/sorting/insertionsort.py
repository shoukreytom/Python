def insertion_sort(array):
    for i in range(len(array)):
        current = array[i]
        j = i - 1
        while j >= 0 and current < array[j]:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = current
    print(array)


def main():
    arr = [9, 0, 5, 1, 6, 3]
    insertion_sort(arr)


if __name__ == '__main__':
    main()
