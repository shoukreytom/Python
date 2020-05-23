# solved

def covid19():
    l = []
    n = int(input("Enter the size of array: "))
    for i in range(n):
        l.append(int(input()))
    for j in range(n):
        temp = 0
        if l[j] == 1:
            if j != 0 and abs(j - temp) < 6:
                print("no")
                return
            temp = j
    print("yes")
    print(l)


covid19()
