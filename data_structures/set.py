"""Functions of set:
    1) add(object)
    2) pop()
    3) remove(object)
    4) copy()
    5) clear()
"""

def main():
    nameList = ["Shoukrey", "Tom", "Shoukrey", "John", "Tom"]
    names = set(nameList)
    nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    even = {2, 4, 6, 8}
    odd = {1, 3, 5, 7, 9}
    copyNames = names.copy()

    names.add("Shoukrey")   # this has no effect because it's already exists
    names.add("Joan")
    removed = names.pop()
    try:
        names.remove("Shoukrey")
    except KeyError:
        print("Key not found")


    print(type(names))
    print(even | odd)
    print(nums & odd)
    print(odd - even)
    print(names)
    print(copyNames)
    print(removed)


if __name__ == "__main__":
    main()
