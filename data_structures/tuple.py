"""Function of tuple:
    1) count(object)
    2) index(object)
"""

def main():
    empty = tuple()
    tu = (1, 2, 3, 4, 2)

    occur = tu.count(2)
    index = tu.index(2)

    print(type(empty))
    print(type(tu))
    print(tu)
    print(occur)
    print(index)


if __name__ == "__main__":
    main()
