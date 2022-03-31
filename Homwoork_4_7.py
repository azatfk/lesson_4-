from math import factorial

i = 0
def factorial_gen(n):
    for range(n):
        print(i, end='!=')
        yield factorial(i)
print("Th<<e program for calculatiny the factorial of a nuber>>")   # Программа вычесления факториала числа
for el in factorial_gen(15):
    print(el)
