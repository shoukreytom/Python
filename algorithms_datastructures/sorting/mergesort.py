def merge(x, y):
    l1 = l2 = 0
    out = []
    while l1 < len(x) and l2 < len(y):
        if x[l1] < y[l2]:
            out.append(x[l1])
            l1 += 1
        else:
            out.append(y[l2])
            l2 += 1
    out += x[l1:] + y[l2:]
    return out


def merge_sort(A):
    if len(A) <= 1:
        return A
    if len(A) == 2:
        return sorted(A)
    mid = int(len(A) / 2)
    return merge(merge_sort(A[:mid]), merge_sort(A[mid:]))


def main():
    a = [3, 9, 0, 1, 5, 11]
    b = merge_sort(a)
    print(b)


if __name__ == "__main__":
    main()
