from pandas import DataFrame

data = {
    'Name': ['Shoukrey', 'John', 'Tom'],
    'Age': [21, 30, 19],
    'Salary': [2000, 3500, 1500]
}


def main():
    # TODO: uncomment all lines
    # frame = DataFrame(data)
    new_frame = DataFrame(data, columns=['Name', 'Salary', 'Age', 'Profile'])
    # print(frame)
    # print(new_frame)
    new_frame['Profile'] = 'Doctor'
    # print(new_frame)

    # assigning to the field which does not exists
    new_frame['Education'] = "EE"
    print(new_frame)
    new_frame = new_frame.T
    print(new_frame)
    new_frame = new_frame.T
    print(new_frame)


if __name__ == "__main__":
    main()
