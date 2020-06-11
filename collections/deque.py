# deque is like double-ended queue

from collections import deque
import string


def main():
    d = deque(string.ascii_lowercase)

    # counting number of elements
    print(len(d))

    # iterating over deque elements     TODO: uncomment the following code for testing
    # for ele in d:
    #     print(ele, end=' ')

    # removing elements either from right or left   TODO: uncomment the following code for testing
    # d.pop()
    # print(d)
    # d.popleft()
    # print(d)

    # appending elements either from right or left  TODO: uncomment the following code for testing
    # d.append('z')
    # d.appendleft('a')
    # print(d)

    # rotate elements
    d.rotate(10)        # rotates 10 elements to the beginning
    print(d)


if __name__ == '__main__':
    main()
