"""Functions of dictionary
    1) items()      returns all items of dictionary
    2) values()     returns values of items in dictionary as a list
    3) keys()       returns keys of items in dictionary as a list
    4) get(key), get(key, ErrorMessage)
    5) pop(key), pop(key, ErrorMessage)     returns removed item's value
    6) popitem()    returns removed item as a tuple (key, value)
    7) clear()      removes all items from dictionary
"""

def main():
    default = {1: "default"}
    countries = {1: "Sudan", 2: "India", 3: "USA",4: "UK"}
    empty = {}

    countCopy = countries.copy()
    hold = countCopy.popitem()
    empty.pop(1, "Key is not found")
    print(default.pop(1, "Key is not found"))
    try:
        empty.popitem()
    except KeyError:
        print("The dictionary is empty")
    values = list(countries.keys())

    print(countries)
    print(countCopy)
    print(hold)
    print(values)
    print(countries.get(2, "Key is not found"))


if __name__ == "__main__":
    main()
