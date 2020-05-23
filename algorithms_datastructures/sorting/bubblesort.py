def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


def main():
    a = [1, 9, 0, 5, 3, 4, 2, 6]
    bubble_sort(a)
    print(a)


if __name__ == '__main__':
    main()
