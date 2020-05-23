from pandas import Series

se = Series([1, 2, 3, 4])
se1 = Series([3, 2, 0, 1], index=('a', 'b', 'c', 'd'))
salary = {"Shoukrey": 2000, "John": 2500, "Tom": 4000}
se2 = Series(salary)

"""Access Series' Elements:
    se[0] equals to 1
    se1['b'] equals to 2
    se2['Shoukrey'] equals to 2000
"""
print(se)
print(se1)
print(se2)

print(se[0])
print(se1['b'])
print(se2['Shoukrey'])
