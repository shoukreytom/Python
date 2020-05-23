from pandas import Series, DataFrame


def main():
    s = Series([100, 200, 300, 400], index=['a', 'c', 'd', 'b'])
    # print(s)
    i = ['a', 'b', 'c', 'd']
    s = s.reindex(i)
    # print(s)

    d = DataFrame({
        "Age": [23, 30, 21],
        "Name": ["Shoukrey", "Tom", "John"],
        "Salary": [2200, 3200, 6000]
    })
    # print(d)
    col = ["Name", "Age", "Salary"]
    d = d.reindex([2, 1, 0])
    # print(d)
    d = d.reindex(columns=col)
    # print(d)


if __name__ == "__main__":
    main()
