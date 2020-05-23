def multiple3_5():
    result = 0
    for i in range(1000):
        if (i % 3) == 0 or (i%5) == 0:
            print(i)
            result += i
    return result

print(multiple3_5())
