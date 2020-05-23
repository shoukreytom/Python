"""
    Find the smallest card. Swap it with the first card.
    Find the second-smallest card. Swap it with the second card.
    Find the third-smallest card. Swap it with the third card.
    Repeat finding the next-smallest card, and swapping it into the correct position until the array is sorted.
"""


def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp
    print(array)


def main():
    arr = [3, 9, 1, 5, 0]
    selection_sort(arr)


if __name__ == '__main__':
    main()
