from _functools import reduce
list = [i for i in range (10, 100, 2)]
print("A list of even numbers in the range [10, 100]: \n", list)   # Список четных чисел в диапозоне [10, , 100]
print("Product of all list items: \n", reduce(lambda x, y: x * y, list))    # Произведение всех элементов списка
