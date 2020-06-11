from enum import Enum, unique, auto


@unique
class Days(Enum):
    SUNDAY = 1
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()


def main():
    # iterating over enum elements
    # for day in Days:
    #     print(day.name, day.value)

    # enum element as a key in dic
    activities = dict()
    activities[Days.FRIDAY] = 'sleep all day'
    activities[Days.MONDAY] = 'fix some bugs'

    print(activities[Days.MONDAY])


if __name__ == '__main__':
    main()
