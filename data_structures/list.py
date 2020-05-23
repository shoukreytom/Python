"""Functions of list:
    1) append(object)
    2) insert(index, object)
    3) remove(object)
    4) pop(), pop(index)
    5) index()
    6) copy()
    7) reverse()
    8) clear()
    9) count(object)
"""

def main():
    even = [2, 4, 6, 8, 10]
    odd = [1, 3, 5, 7, 9]
    nums = [x for x in range(1, 15)]
    evencopy = even.copy()
    unsorted = [3, 2, 9, 1, 4, 0]

    unsorted.sort()
    odd.pop()
    odd.remove(7)
    even.append(14)
    even.insert(even.index(2)+1, 2)
    even.insert(even.index(10)+1, 12)

    print("evencopy:", evencopy)
    print("even:", even)
    print("odd:", odd)
    print("nums:", nums)
    print("unsorted:", unsorted)
    print(even.count(2))

    # TODO: test all other functions

if __name__ == '__main__':
    main()
