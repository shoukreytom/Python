def even_fibonacci(num):
    if num == 0 or num == 1:
        return num
    print(num)
    return even_fibonacci(num-1) + even_fibonacci(num-2)

print(even_fibonacci(10))
        
